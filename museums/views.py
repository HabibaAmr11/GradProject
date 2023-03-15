from rest_framework import generics, permissions

from museums.models import Museum, Collection, Timeline, Favorite
from museums.serializers import MuseumSerializer, CollectionSerializer, TimelineSerializer, FavoriteSerializer


class MuseumListCreateAPIView(generics.ListCreateAPIView):
    queryset = Museum.objects.all()
    serializer_class = MuseumSerializer


class MuseumDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Museum.objects.all()
    serializer_class = MuseumSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CollectionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class CollectionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = (permissions.IsAuthenticated,)


class TimelineListCreateAPIView(generics.ListCreateAPIView):
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer


class TimelineDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer
    permission_classes = (permissions.IsAuthenticated,)


class FavoriteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer


class FavoriteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = (permissions.IsAuthenticated,)
