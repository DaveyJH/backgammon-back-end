from rest_framework import status
from rest_framework.test import APITestCase
from backgammon_drf.test_setup import (
    create_three_users,
    create_test_user_1_vs_test_user_2_game,
)


class DiceRollListViewTests(APITestCase):
    def setUp(self):
        create_three_users()

    def test_logged_in_user_can_list_dice_rolls(self):
        self.client.login(username="test_user_1", password="test_pass")
        response = self.client.get("/dice/")
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_logged_out_user_can_view_dice_rolls(self):
        response = self.client.get("/dice/")
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_logged_out_user_cannot_create_dice_roll(self):
        response = self.client.post("/dice/", {"game": 1})
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_logged_in_user_can_create_dice_roll_in_their_game(self):
        create_test_user_1_vs_test_user_2_game()
        self.client.login(username="test_user_1", password="test_pass")
        response = self.client.post("/dice/", {"game": 1})
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_logged_in_user_cannot_create_dice_roll_in_other_game(self):
        create_test_user_1_vs_test_user_2_game()
        self.client.login(username="test_user_99", password="test_pass")
        response = self.client.post("/dice/", {"game": 1})
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_logged_in_user_can_only_create_dice_roll_on_their_turn(self):
        create_test_user_1_vs_test_user_2_game()
        self.client.login(username="test_user_1", password="test_pass")
        response = self.client.post("/dice/", {"game": 1})
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        response = self.client.post("/dice/", {"game": 1})
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_logged_in_user_cannot_create_dice_roll_in_non_existent_game(self):
        self.client.login(username="test_user_1", password="test_pass")
        response = self.client.post("/dice/", {"game": 1})
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_logged_in_user_cannot_update_dice_roll(self):
        self.client.login(username="test_user_1", password="test_pass")
        response = self.client.put("/dice/", {"game": 1, "value1": 6})
        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def test_dice_roll_cannot_be_set_by_user(self):
        create_test_user_1_vs_test_user_2_game()
        self.client.login(username="test_user_1", password="test_pass")
        response = self.client.post("/dice/", {"game": 1, "value1": 7})
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertNotEqual(response.data["value1"], 7)

    def test_dice_roll_is_random_value_1_to_6(self):
        create_test_user_1_vs_test_user_2_game()
        number_of_dice_rolls = 25
        # required to allow alternate players to roll dice
        for i in range(number_of_dice_rolls):
            self.client.login(
                username=f"test_user_{i % 2 + 1}",
                password="test_pass"
            )
            self.client.post("/dice/", {"game": 1})

        response = self.client.get("/dice/")
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        # theoretically, this test could fail if all dice rolls are the same
        self.assertEqual(response.data["count"], number_of_dice_rolls)
        value1s = [dice["value1"] for dice in response.data["results"]]
        value2s = [dice["value2"] for dice in response.data["results"]]

        any_dice_differ = any(
            value1 != value2 for value1, value2 in zip(value1s, value2s)
        )
        self.assertTrue(any_dice_differ)

        all_dice_are_the_same = all(
            value1 == value2 for value1, value2 in zip(value1s, value2s)
        )
        self.assertFalse(all_dice_are_the_same)

        for dice in [*value1s, *value2s]:
            self.assertTrue(dice in range(1, 7))
