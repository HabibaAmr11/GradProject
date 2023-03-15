from django.urls import path

from museums.views import MuseumListCreateAPIView, MuseumDetailAPIView, CollectionListCreateAPIView, \
    CollectionDetailAPIView, TimelineListCreateAPIView, TimelineDetailAPIView, FavoriteListCreateAPIView, \
    FavoriteDetailAPIView

urlpatterns = [
    path('museum', MuseumListCreateAPIView.as_view(), name='museum-create'),
    path('museum/<int:pk>', MuseumDetailAPIView.as_view(), name='museum-detail'),
    path('collection', CollectionListCreateAPIView.as_view(), name='collection-create'),
    path('collection/<int:pk>', CollectionDetailAPIView.as_view(), name='collection-detail'),
    path('timeline', TimelineListCreateAPIView.as_view(), name='timeline-create'),
    path('timeline/<int:pk>', TimelineDetailAPIView.as_view(), name='timeline-detail'),
    path('favorite', FavoriteListCreateAPIView.as_view(), name='favorite-create'),
    path('favorite/<int:pk>', FavoriteDetailAPIView.as_view(), name='favorite-detail'),
]
