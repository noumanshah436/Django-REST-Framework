from django.db import models


DAYS_OF_WEEK = [
    ("monday", "Monday"),
    ("tuesday", "Tuesday"),
    ("wednesday", "Wednesday"),
    ("thursday", "Thursday"),
    ("friday", "Friday"),
    ("saturday", "Saturday"),
    ("sunday", "Sunday"),
]


class TimeSlot(models.Model):
    day = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    start = models.TimeField()
    stop = models.TimeField()
    ids = models.JSONField(default=list)

    def __str__(self):
        return f"{self.id} {self.day} {self.start}-{self.stop}"
