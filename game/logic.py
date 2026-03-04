from typing import Literal, List


Feedback = Literal["correct", "present", "absent"]


def score_guess(guess: str, solution: str) -> List[Feedback]:
    guess = guess.lower()
    solution = solution.lower()
    result: List[Feedback] = ["absent"] * 5

    remaining: dict[str, int] = {}
    for i, (g, s) in enumerate(zip(guess, solution)):
        if g == s:
            result[i] = "correct"
        else:
            remaining[s] = remaining.get(s, 0) + 1

    for i, g in enumerate(guess):
        if result[i] == "correct":
            continue
        if remaining.get(g, 0) > 0:
            result[i] = "present"
            remaining[g] -= 1

    return result

