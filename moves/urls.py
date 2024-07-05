from django.urls import path
from moves import views


urlpatterns = [
    path("moves/", views.MoveList.as_view()),
    path("moves/<int:pk>/", views.MoveDetail.as_view()),
]
