from rest_framework import status
from rest_framework.test import APITestCase
from backgammon_drf.test_setup import (
    create_three_users,
    create_test_user_1_vs_test_user_2_game,
    create_test_user_1_vs_test_user_99_game
)


class MoveListViewTests(APITestCase):
    def setUp(self):
        create_three_users()

    def test_can_list_moves(self):
        response = self.client.get("/moves/")
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_logged_out_user_cannot_create_move(self):
        create_test_user_1_vs_test_user_2_game()
        response = self.client.post("/moves/", {"game": 1})
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_logged_in_user_can_create_move(self):
        create_test_user_1_vs_test_user_2_game()
        self.client.login(username="test_user_1", password="test_pass")
        response = self.client.post("/moves/", {"game": 1})
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_logged_in_user_can_create_move_with_content(self):
        create_test_user_1_vs_test_user_2_game()
        self.client.login(username="test_user_1", password="test_pass")
        response = self.client.post("/moves/", {
            "game": 1, "content": "test content"
        })
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(response.data["content"], "test content")

    def test_logged_in_user_cannot_create_move_in_other_game(self):
        create_test_user_1_vs_test_user_2_game()
        self.client.login(username="test_user_99", password="test_pass")
        response = self.client.post("/moves/", {"game": 1})
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_game_filter_works_as_expected(self):
        create_test_user_1_vs_test_user_2_game()
        create_test_user_1_vs_test_user_99_game()
        self.client.login(username="test_user_1", password="test_pass")
        self.client.post("/moves/", {"game": 1, "content": "test content"})
        response = self.client.get("/moves/?game=1")
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["game"], 1)
        self.assertEqual(
            response.data["results"][0]["content"],
            "test content"
        )
        response = self.client.get("/moves/?game=2")
        self.assertEqual(response.data["count"], 0)

    def test_player_filter_works_as_expected(self):
        create_test_user_1_vs_test_user_2_game()
        create_test_user_1_vs_test_user_99_game()
        self.client.login(username="test_user_1", password="test_pass")
        self.client.post("/moves/", {"game": 1, "content": "test content"})
        response = self.client.get("/moves/?player=1")
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["game"], 1)
        self.assertEqual(
            response.data["results"][0]["content"],
            "test content"
        )
        response = self.client.get("/moves/?player=2")
        self.assertEqual(response.data["count"], 0)


class MoveDetailViewTests(APITestCase):
    def setUp(self):
        create_three_users()

    def test_logged_in_user_can_view_specific_move(self):
        create_test_user_1_vs_test_user_2_game()
        self.client.login(username="test_user_1", password="test_pass")
        self.client.post("/moves/", {"game": 1, "content": "test content"})

        response = self.client.get("/moves/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_cannot_view_non_existent_move(self):
        self.client.login(username="test_user_1", password="test_pass")
        response = self.client.get("/moves/101/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_logged_out_user_can_view_specific_move(self):
        create_test_user_1_vs_test_user_2_game()
        self.client.login(username="test_user_1", password="test_pass")
        self.client.post("/moves/", {"game": 1, "content": "test content"})
        self.client.logout()

        response = self.client.get("/moves/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["content"], "test content")

    def test_logged_out_user_cannot_view_non_existent_move(self):
        response = self.client.get("/moves/101/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_logged_in_user_can_update_owned_move(self):
        create_test_user_1_vs_test_user_2_game()
        self.client.login(username="test_user_1", password="test_pass")
        self.client.post("/moves/", {"game": 1, "content": "test content"})

        response = self.client.put("/moves/1/", {
            "game": 1, "content": "revised content"
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["content"], "revised content")

    def test_logged_in_user_can_delete_owned_move(self):
        create_test_user_1_vs_test_user_2_game()
        self.client.login(username="test_user_1", password="test_pass")
        self.client.post("/moves/", {"game": 1, "content": "test content"})

        response = self.client.delete("/moves/1/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get("/moves/1/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_logged_in_user_cannot_update_other_move(self):
        create_test_user_1_vs_test_user_2_game()
        self.client.login(username="test_user_2", password="test_pass")
        self.client.post("/moves/", {"game": 1, "content": "test content"})

        self.client.login(username="test_user_1", password="test_pass")
        response = self.client.put("/moves/1/", {
            "game": 1, "content": "revised content"
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        response = self.client.get("/moves/1/")
        self.assertEqual(response.data["content"], "test content")

    def test_logged_out_user_cannot_update_move(self):
        create_test_user_1_vs_test_user_2_game()
        self.client.login(username="test_user_1", password="test_pass")
        self.client.post("/moves/", {"game": 1, "content": "test content"})
        self.client.logout()

        response = self.client.put("/moves/1/", {
            "game": 1, "content": "revised content"
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        response = self.client.get("/moves/1/")
        self.assertEqual(response.data["content"], "test content")

    def test_logged_in_user_cannot_update_move_that_is_not_latest(self):
        create_test_user_1_vs_test_user_2_game()
        self.client.login(username="test_user_1", password="test_pass")
        self.client.post("/moves/", {"game": 1, "content": "test content"})
        self.client.post("/moves/", {"game": 1, "content": "new move"})
        response = self.client.put("/moves/1/", {
            "game": 1, "content": "revised content"
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        response = self.client.get("/moves/1/")
        self.assertEqual(response.data["content"], "test content")

    def test_logged_in_user_cannot_delete_move_that_is_not_latest(self):
        create_test_user_1_vs_test_user_2_game()
        self.client.login(username="test_user_1", password="test_pass")
        self.client.post("/moves/", {"game": 1, "content": "test content"})
        self.client.post("/moves/", {"game": 1, "content": "new move"})

        response = self.client.delete("/moves/1/")
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )
        self.assertEqual(
            response.data["detail"],
            "This is not the most recent move."
        )

        response = self.client.get("/moves/1/")
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(response.data["content"], "test content")

    def test_logged_out_user_cannot_delete_move(self):
        create_test_user_1_vs_test_user_2_game()
        self.client.login(username="test_user_1", password="test_pass")
        self.client.post("/moves/", {"game": 1, "content": "test content"})
        self.client.logout()

        response = self.client.delete("/moves/1/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
