from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from schedule.models import TimeSlot


class TimeSlotAPITestCase(APITestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username="testuser", password="testpass")
        # Obtain JWT token
        response = self.client.post(
            reverse("token_obtain_pair"),
            {"username": "testuser", "password": "testpass"},
            format="json",
        )
        self.token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)

    def test_create_valid_timeslot(self):
        data = {
            "day": "monday",
            "start": "09:00",
            "stop": "10:00",
            "ids": [1, 2, 3],
        }
        response = self.client.post("/api/timeslots/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TimeSlot.objects.count(), 1)

    def test_reject_overlapping_timeslot(self):
        # Create initial timeslot
        TimeSlot.objects.create(
            day="monday",
            start="09:00",
            stop="10:00",
            ids=[1, 2],
        )
        # Try to create overlapping timeslot
        data = {
            "day": "monday",
            "start": "09:30",
            "stop": "10:30",
            "ids": [3],
        }
        response = self.client.post("/api/timeslots/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Overlapping TimeSlot ID", str(response.data))

    def test_reject_invalid_timeslot_cross_midnight(self):
        data = {"day": "monday", "start": "23:00", "stop": "01:00", "ids": [4, 5]}
        response = self.client.post("/api/timeslots/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("start time must be before stop time", str(response.data))

    def test_list_grouped_schedule(self):
        # Create multiple timeslots
        TimeSlot.objects.create(
            day="monday",
            start="08:00",
            stop="09:00",
            ids=[1],
        )
        TimeSlot.objects.create(
            day="tuesday",
            start="10:00",
            stop="11:00",
            ids=[2],
        )
        TimeSlot.objects.create(
            day="monday",
            start="09:00",
            stop="10:00",
            ids=[3],
        )

        response = self.client.get("/api/timeslots/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        schedule = response.data["schedule"]
        self.assertIn("monday", schedule)
        self.assertIn("tuesday", schedule)
        self.assertEqual(len(schedule["monday"]), 2)
        self.assertEqual(len(schedule["tuesday"]), 1)

    def test_update_timeslot_valid(self):
        # Create initial timeslot
        timeslot = TimeSlot.objects.create(
            day="monday", start="08:00", stop="09:00", ids=[1]
        )

        url = f"/api/timeslots/{timeslot.id}/"

        # Update with valid new timeslot
        data = {"day": "monday", "start": "09:00", "stop": "10:00", "ids": [1, 2, 3]}

        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify update happened
        timeslot.refresh_from_db()
        self.assertEqual(str(timeslot.start), "09:00:00")
        self.assertEqual(str(timeslot.stop), "10:00:00")
        self.assertEqual(timeslot.ids, [1, 2, 3])

    def test_update_timeslot_reject_overlap(self):
        # Create two timeslots
        t1 = TimeSlot.objects.create(day="monday", start="08:00", stop="09:00", ids=[1])
        t2 = TimeSlot.objects.create(day="monday", start="09:00", stop="10:00", ids=[2])

        url = f"/api/timeslots/{t2.id}/"

        # Try to update t2 to overlap with t1
        data = {
            "day": "monday",
            "start": "08:30",  # Overlaps with t1
            "stop": "09:30",
            "ids": [2],
        }

        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Overlapping TimeSlot ID", str(response.data))

    def test_delete_timeslot(self):
        # Create timeslot
        timeslot = TimeSlot.objects.create(
            day="wednesday", start="11:00", stop="12:00", ids=[5, 6]
        )

        url = f"/api/timeslots/{timeslot.id}/"

        # Delete it
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verify it is gone
        self.assertEqual(TimeSlot.objects.filter(id=timeslot.id).count(), 0)
