from django.contrib.auth.models import User


def create_three_users():
    User.objects.create_user(username="test_user_1", password="test_pass")
    User.objects.create_user(username="test_user_2", password="test_pass")
    User.objects.create_user(username="test_user_99", password="test_pass")
