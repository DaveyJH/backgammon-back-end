from django.contrib.auth.models import User
from games.models import Game


def create_three_users():
    User.objects.create_user(username="test_user_1", password="test_pass")
    User.objects.create_user(username="test_user_2", password="test_pass")
    User.objects.create_user(username="test_user_99", password="test_pass")


def create_test_user_1_vs_test_user_2_game():
    user1 = User.objects.get(username="test_user_1")
    user2 = User.objects.get(username="test_user_2")
    Game.objects.create(player1=user1, player2=user2)


def create_test_user_1_vs_test_user_99_game():
    user1 = User.objects.get(username="test_user_1")
    user2 = User.objects.get(username="test_user_99")
    Game.objects.create(player1=user1, player2=user2)


def create_test_user_2_vs_test_user_99_game():
    user1 = User.objects.get(username="test_user_2")
    user2 = User.objects.get(username="test_user_99")
    Game.objects.create(player1=user1, player2=user2)
