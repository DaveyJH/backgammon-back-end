from rest_framework import status
from rest_framework.test import APITestCase
from backgammon_drf.test_setup import create_three_users
from .models import Profile


class ProfileListViewTests(APITestCase):
    """Test the ProfileListView functionality."""
    def setUp(self):
        create_three_users()

    def test_can_list_profiles(self):
        response = self.client.get("/profiles/")
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_cannot_create_profile(self):
        response = self.client.post("/profiles/")
        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def test_profile_count_reflects_number_of_profiles(self):
        response = self.client.get("/profiles/")
        self.assertEqual(len(response.data["results"]), 3)
        self.assertEqual(response.data["count"], 3)

    def test_new_profile_has_default_image(self):
        response = self.client.get("/profiles/")
        self.assertEqual(
            response.data["results"][0]["image"],
            "https://res.cloudinary.com/daveyjh/image/upload/v1/"
            "backgammon/media/../default/two-dice_nv5d5h"
        )

    def test_logged_out_user_is_not_a_profile_owner(self):
        response = self.client.get("/profiles/")
        for i in range(3):
            self.assertFalse(response.data["results"][i]["is_owner"])

    def test_logged_in_user_is_profile_owner(self):
        self.client.login(username="test_user_1", password="test_pass")
        response = self.client.get("/profiles/")
        self.assertTrue(response.data["results"][0]["is_owner"])

    def test_logged_in_user_is_not_other_profile_owner(self):
        self.client.login(username="test_user_1", password="test_pass")
        response = self.client.get("/profiles/")
        for i in range(1, 3):
            self.assertFalse(response.data["results"][i]["is_owner"])


class ProfileDetailViewTests(APITestCase):
    """Test the ProfileDetailView functionality."""
    def setUp(self):
        create_three_users()

    def test_logged_in_user_can_view_specific_profile(self):
        self.client.login(username="test_user_1", password="test_pass")
        response = self.client.get("/profiles/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_cannot_view_non_existent_profile(self):
        self.client.login(username="test_user_1", password="test_pass")
        response = self.client.get("/profiles/101/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_logged_out_user_can_view_specific_profile(self):
        response = self.client.get("/profiles/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_out_user_cannot_view_non_existent_profile(self):
        response = self.client.get("/profiles/101/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_logged_in_user_can_update_owned_profile(self):
        self.client.login(username="test_user_1", password="test_pass")
        response = self.client.put("/profiles/1/", {"info": "test info"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["info"], "test info")

    def test_logged_in_user_cannot_update_other_profile(self):
        self.client.login(username="test_user_1", password="test_pass")
        response = self.client.put("/profiles/2/", {"info": "test info"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Profile.objects.filter(id=2).first().info, "")

    def test_logged_out_user_cannot_update_profile(self):
        response = self.client.put("/profiles/1/", {"info": "test info"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_logged_in_user_cannot_delete_owned_profile(self):
        self.client.login(username="test_user_1", password="test_pass")
        response = self.client.delete("/profiles/1/")
        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED
        )
        self.assertIsNotNone(Profile.objects.filter(id=1).first())

    def test_logged_in_user_cannot_delete_other_profile(self):
        self.client.login(username="test_user_1", password="test_pass")
        response = self.client.delete("/profiles/2/")
        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED
        )
        self.assertIsNotNone(Profile.objects.filter(id=2).first())

    def test_logged_out_user_cannot_delete_profile(self):
        response = self.client.delete("/profiles/1/")
        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED
        )
        self.assertIsNotNone(Profile.objects.filter(id=1).first())
