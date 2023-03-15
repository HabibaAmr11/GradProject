from rest_framework import serializers

from booking.models import Event, Tour, BookTour, BookTicket


class EventSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ('created_by',)


class TourSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Tour
        fields = '__all__'
        read_only_fields = ('created_by',)


class BookTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookTour
        fields = '__all__'


class BookTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookTicket
        fields = '__all__'
