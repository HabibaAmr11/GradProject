from django.urls import path

from games.views import GameListCreateAPIView, GameDetailAPIView

urlpatterns = [
    path('game', GameListCreateAPIView.as_view(), name='game-create'),
    path('game/<int:pk>', GameDetailAPIView.as_view(), name='game-detail'),
]
