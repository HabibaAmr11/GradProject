from rest_framework import generics, permissions

from booking.models import Event, Tour, BookTour, BookTicket
from booking.serializers import EventSerializer, TourSerializer, BookTourSerializer, BookTicketSerializer


class EventListCreateAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticated,)


class TourListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer


class TourDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = (permissions.IsAuthenticated,)


class BookTourListCreateAPIView(generics.ListCreateAPIView):
    queryset = BookTour.objects.all()
    serializer_class = BookTourSerializer


class BookTourDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookTour.objects.all()
    serializer_class = BookTourSerializer
    permission_classes = (permissions.IsAuthenticated,)


class BookTicketListCreateAPIView(generics.ListCreateAPIView):
    queryset = BookTicket.objects.all()
    serializer_class = BookTicketSerializer


class BookTicketDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookTicket.objects.all()
    serializer_class = BookTicketSerializer
    permission_classes = (permissions.IsAuthenticated,)
