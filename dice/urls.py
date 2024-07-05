from django.urls import path
from dice import views


urlpatterns = [
    path("dice/", views.DiceList.as_view()),
]
