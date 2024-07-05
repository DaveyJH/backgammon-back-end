from django.urls import path
from winners import views


urlpatterns = [
    path("winners/", views.WinnerList.as_view()),
]
