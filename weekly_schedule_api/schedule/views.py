from rest_framework import viewsets, permissions
from .models import TimeSlot
from .serializers import TimeSlotSerializer
from rest_framework.response import Response


class TimeSlotViewSet(viewsets.ModelViewSet):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        # Get all timeslots, ordered by day + start ascending
        queryset = self.get_queryset().order_by("day", "start")

        # Group by day
        grouped = {}
        for day_key, _ in dict(
            self.queryset.model._meta.get_field("day").choices
        ).items():
            grouped[day_key] = []

        for timeslot in queryset:
            day = timeslot.day
            # Serialize single timeslot
            serialized = TimeSlotSerializer(timeslot).data
            grouped[day].append(serialized)

        return Response({"schedule": grouped})
