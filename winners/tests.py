from rest_framework import status
from rest_framework.test import APITestCase
from backgammon_drf.test_setup import (
    create_three_users,
    create_test_user_1_vs_test_user_2_game,
)


class WinnerListViewTests(APITestCase):
    def setUp(self):
        create_three_users()

    def test_logged_in_user_can_list_winners(self):
        self.client.login(username="test_user_1", password="test_pass")
        response = self.client.get("/winners/")
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_logged_out_user_can_view_winners(self):
        response = self.client.get("/winners/")
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_logged_out_user_cannot_create_winners(self):
        create_test_user_1_vs_test_user_2_game()
        response = self.client.post("/winners/", {"owner": 1, "game": 1})
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_logged_in_user_can_create_winners_in_their_game(self):
        create_test_user_1_vs_test_user_2_game()
        self.client.login(username="test_user_1", password="test_pass")
        response = self.client.post("/winners/", {"owner": 1, "game": 1})
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(response.data["owner"], 1)
        self.assertEqual(response.data["game"], 1)

    def test_logged_in_user_cannot_create_winners_in_other_game(self):
        create_test_user_1_vs_test_user_2_game()
        self.client.login(username="test_user_99", password="test_pass")
        response = self.client.post("/winners/", {"owner": 1, "game": 1})
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_logged_in_user_cannot_create_winners_in_non_existent_game(self):
        self.client.login(username="test_user_1", password="test_pass")
        response = self.client.post("/winners/", {"owner": 1, "game": 1})
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_logged_in_user_cannot_update_winners(self):
        create_test_user_1_vs_test_user_2_game()
        self.client.login(username="test_user_1", password="test_pass")
        self.client.post("/winners/", {"owner": 1, "game": 1})
        response = self.client.put("/winners/1/", {"game": 1, "value1": 6})
        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )

    def test_logged_in_user_cannot_delete_winners(self):
        create_test_user_1_vs_test_user_2_game()
        self.client.login(username="test_user_1", password="test_pass")
        self.client.post("/winners/", {"owner": 1, "game": 1})

        response = self.client.delete("/winners/1/")
        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )

    def test_logged_in_user_cannot_create_winner_on_game_with_winner(self):
        create_test_user_1_vs_test_user_2_game()
        self.client.login(username="test_user_1", password="test_pass")
        self.client.post("/winners/", {"owner": 1, "game": 1})
        response = self.client.post("/winners/", {"owner": 1, "game": 1})
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
