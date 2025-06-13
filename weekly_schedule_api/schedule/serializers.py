from rest_framework import serializers
from .models import TimeSlot
from django.db.models import Q


class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = ("id", "day", "start", "stop", "ids")

    def validate(self, data):
        day = data["day"]
        start = data["start"]
        stop = data["stop"]

        # Validate timeslot is valid within the day
        if start >= stop:
            raise serializers.ValidationError(
                "Invalid TimeSlot: start time must be before stop time (cannot cross midnight)."
            )

        # When updating, exclude current instance
        instance_id = self.instance.id if self.instance else None

        # Overlap within same timestamp
        overlapping = (
            TimeSlot.objects.filter(
                day=day,
            )
            .exclude(id=instance_id)
            .filter(Q(start__lt=stop) & Q(stop__gt=start))
        )

        if overlapping.exists():
            overlapping_ids = list(overlapping.values_list("id", flat=True))
            raise serializers.ValidationError(
                f"TimeSlot overlaps with existing timeslot(s) in the schedule. Overlapping TimeSlot ID(s): {overlapping_ids}"
            )

        return data
