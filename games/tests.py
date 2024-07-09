from rest_framework import status
from rest_framework.test import APITestCase
from backgammon_drf.test_setup import (
    create_three_users,
    create_test_user_1_vs_test_user_2_game,
    create_test_user_1_vs_test_user_99_game,
    create_test_user_2_vs_test_user_99_game,
)


class GameListViewTests(APITestCase):
    """Test the GameListView functionality."""
    def setUp(self):
        create_three_users()

    def test_can_list_games(self):
        response = self.client.get("/games/")
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_game_count_reflects_number_of_games(self):
        response = self.client.get("/games/")
        self.assertEqual(len(response.data["results"]), 0)
        self.assertEqual(response.data["count"], 0)
        create_test_user_1_vs_test_user_2_game()
        response = self.client.get("/games/")
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["count"], 1)

    def test_new_game_has_default_image(self):
        create_test_user_1_vs_test_user_2_game()
        response = self.client.get("/games/")
        self.assertEqual(
            response.data["results"][0]["image"],
            "https://res.cloudinary.com/daveyjh/image/upload/v1/backgammon/"
            "media/../default/backgammon-starting-board-with-direction_jqwtuy"
        )

    def test_new_game_is_active(self):
        create_test_user_1_vs_test_user_2_game()
        response = self.client.get("/games/")
        self.assertTrue(response.data["results"][0]["active"])

    def test_logged_in_user_can_create_game(self):
        self.client.login(username="test_user_1", password="test_pass")
        response = self.client.post("/games/", {"player1": 1, "player2": 2})
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_logged_in_user_cannot_create_game_without_self_as_a_player(self):
        self.client.login(username="test_user_1", password="test_pass")
        response = self.client.post("/games/", {"player1": 2, "player2": 3})
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_logged_in_user_cannot_create_game_against_themself(self):
        self.client.login(username="test_user_1", password="test_pass")
        response = self.client.post("/games/", {"player1": 1, "player2": 1})
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_logged_in_user_cannot_create_game_with_nonexistent_player(self):
        self.client.login(username="test_user_1", password="test_pass")
        response = self.client.post("/games/", {"player1": 1, "player2": 99})
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_logged_in_user_is_player_1_in_appropriate_game(self):
        create_test_user_1_vs_test_user_2_game()
        self.client.login(username="test_user_1", password="test_pass")
        response = self.client.get("/games/")
        self.assertEqual(response.data["results"][0]["player1"], 1)

    def test_logged_in_user_is_not_player_1_in_appropriate_game(self):
        create_test_user_2_vs_test_user_99_game()
        self.client.login(username="test_user_1", password="test_pass")
        response = self.client.get("/games/")
        self.assertNotEqual(response.data["results"][0]["player1"], 1)

    def test_logged_in_user_is_player_2_in_appropriate_game(self):
        create_test_user_1_vs_test_user_2_game()
        self.client.login(username="test_user_2", password="test_pass")
        response = self.client.get("/games/")
        self.assertEqual(response.data["results"][0]["player2"], 2)

    def test_logged_in_user_is_not_player_2_in_appropriate_game(self):
        create_test_user_2_vs_test_user_99_game()
        self.client.login(username="test_user_2", password="test_pass")
        response = self.client.get("/games/")
        self.assertNotEqual(response.data["results"][0]["player2"], 2)

    def test_logged_out_user_cannot_create_game(self):
        response = self.client.post("/games/", {"player1": 1, "player2": 2})
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_player_1_filter_works_as_expected(self):
        create_test_user_1_vs_test_user_2_game()
        create_test_user_1_vs_test_user_99_game()
        create_test_user_2_vs_test_user_99_game()
        response = self.client.get("/games/?player1=1")
        self.assertEqual(len(response.data["results"]), 2)
        self.assertEqual(response.data["count"], 2)
        self.assertEqual(response.data["results"][0]["player1"], 1)
        self.assertEqual(response.data["results"][0]["player1"], 1)

    def test_player_2_filter_works_as_expected(self):
        create_test_user_1_vs_test_user_2_game()
        create_test_user_1_vs_test_user_99_game()
        create_test_user_2_vs_test_user_99_game()
        response = self.client.get("/games/?player2=2")
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["player2"], 2)

    def test_active_filter_works_as_expected(self):
        create_test_user_1_vs_test_user_2_game()
        create_test_user_1_vs_test_user_99_game()
        create_test_user_2_vs_test_user_99_game()
        self.client.login(username="test_user_1", password="test_pass")
        self.client.put("/games/1/", {
            "player1": 1, "player2": 2, "active": False
        })
        response = self.client.get("/games/?is_active=True")
        self.assertEqual(len(response.data["results"]), 2)
        self.assertEqual(response.data["count"], 2)
        response = self.client.get("/games/?is_active=False")
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["count"], 1)

    def test_either_player_filter_works_as_expected(self):
        create_test_user_1_vs_test_user_2_game()
        create_test_user_1_vs_test_user_99_game()
        create_test_user_2_vs_test_user_99_game()
        response = self.client.get("/games/?either_player=3")
        self.assertEqual(len(response.data["results"]), 2)
        self.assertEqual(response.data["count"], 2)


class GameDetailViewTests(APITestCase):
    """Test the GameDetailView functionality."""
    def setUp(self):
        create_three_users()
        create_test_user_1_vs_test_user_2_game()

    def test_logged_in_user_can_view_specific_game(self):
        self.client.login(username="test_user_1", password="test_pass")
        response = self.client.get("/games/1/")
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_logged_in_user_cannot_view_non_existent_game(self):
        self.client.login(username="test_user_1", password="test_pass")
        response = self.client.get("/games/101/")
        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )

    def test_logged_out_user_can_view_specific_game(self):
        response = self.client.get("/games/1/")
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_logged_out_user_cannot_view_non_existent_game(self):
        response = self.client.get("/games/101/")
        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )

    def test_logged_in_user_can_update_owned_game(self):
        self.client.login(username="test_user_1", password="test_pass")
        response = self.client.put("/games/1/", {
            "player1": 1, "player2": 2, "active": False
        })
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertFalse(response.data["active"])

    def test_logged_in_user_cannot_update_other_players_game(self):
        create_test_user_2_vs_test_user_99_game()
        self.client.login(username="test_user_1", password="test_pass")
        response = self.client.put("/games/2/", {
            "player1": 2, "player2": 3, "active": False
        })
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )
        self.assertTrue(self.client.get("/games/2/").data["active"])

    def test_game_players_cannot_be_changed(self):
        self.client.login(username="test_user_1", password="test_pass")
        response = self.client.put("/games/1/", {"player1": 2, "player2": 1})
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )
        response = self.client.get("/games/1/")
        self.assertEqual(response.data["player1"], 1)
        self.assertEqual(response.data["player2"], 2)

    def test_logged_out_user_cannot_update_game(self):
        response = self.client.put("/games/1/", {
            "player1": 1, "player2": 2, "active": False
        })
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_logged_in_user_cannot_delete_owned_game(self):
        self.client.login(username="test_user_1", password="test_pass")
        response = self.client.delete("/games/1/")
        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED
        )
        response = self.client.get("/games/1/")
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_logged_in_user_cannot_delete_other_players_game(self):
        create_test_user_2_vs_test_user_99_game()
        self.client.login(username="test_user_1", password="test_pass")
        response = self.client.delete("/games/2/")
        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED
        )
        response = self.client.get("/games/2/")
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_logged_out_user_cannot_delete_game(self):
        response = self.client.delete("/games/1/")
        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED
        )
        response = self.client.get("/games/1/")
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
