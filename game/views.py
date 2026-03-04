from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from .logic import score_guess
from .words import is_valid_word, random_solution


MAX_ATTEMPTS = 6


def _reset_game_session(request: HttpRequest) -> None:
    request.session["solution"] = random_solution()
    request.session["guesses"] = []
    request.session["status"] = "in_progress"
    request.session.modified = True


def _init_game_session(request: HttpRequest) -> None:
    if "solution" not in request.session or request.session.get("status") != "in_progress":
        _reset_game_session(request)


def wordle(request: HttpRequest):
    _init_game_session(request)
    return render(
        request,
        "game/wordle.html",
        {
            "max_attempts": MAX_ATTEMPTS,
            "rows": range(MAX_ATTEMPTS),
            "status": request.session["status"],
            "guesses": request.session["guesses"],
        },
    )


@require_POST
def submit_guess(request: HttpRequest):
    _init_game_session(request)

    if request.session["status"] != "in_progress":
        return JsonResponse(
            {"error": "Game over", "status": request.session["status"]},
            status=400,
        )

    word = request.POST.get("word", "").lower()
    if not is_valid_word(word):
        return JsonResponse(
            {"error": "Guess must be 5 letters (A–Z)."}, status=400
        )

    solution = request.session["solution"]
    feedback = score_guess(word, solution)

    guesses: list[dict] = request.session["guesses"]
    guesses.append({"word": word, "feedback": feedback})

    status = "in_progress"
    if word == solution:
        status = "won"
    elif len(guesses) >= MAX_ATTEMPTS:
        status = "lost"

    request.session["guesses"] = guesses
    request.session["status"] = status
    request.session.modified = True

    return JsonResponse(
        {
            "word": word,
            "feedback": feedback,
            "status": status,
            "attempt": len(guesses),
            "max_attempts": MAX_ATTEMPTS,
            "solution": solution if status != "in_progress" else None,
        }
    )


@require_POST
def new_game(request: HttpRequest):
    _reset_game_session(request)
    return JsonResponse({"status": "in_progress"})


