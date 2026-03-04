from django.urls import path

from . import views


app_name = "game"

urlpatterns = [
    path("", views.wordle, name="wordle"),
    path("api/guess/", views.submit_guess, name="submit_guess"),
    path("api/new-game/", views.new_game, name="new_game"),
]

