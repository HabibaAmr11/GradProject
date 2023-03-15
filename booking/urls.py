from django.urls import path

from booking.views import EventListCreateAPIView, EventDetailAPIView, TourListCreateAPIView, TourDetailAPIView, \
    BookTourListCreateAPIView, BookTourDetailAPIView, BookTicketListCreateAPIView, BookTicketDetailAPIView

urlpatterns = [
    path('event', EventListCreateAPIView.as_view(), name='event-create'),
    path('event/<int:pk>', EventDetailAPIView.as_view(), name='event-detail'),
    path('tour', TourListCreateAPIView.as_view(), name='tour-create'),
    path('tour/<int:pk>', TourDetailAPIView.as_view(), name='tour-detail'),
    path('book_tour', BookTourListCreateAPIView.as_view(), name='book_tour-create'),
    path('book_tour/<int:pk>', BookTourDetailAPIView.as_view(), name='book_tour-detail'),
    path('book_ticket', BookTicketListCreateAPIView.as_view(), name='book_ticket-create'),
    path('book_ticket/<int:pk>', BookTicketDetailAPIView.as_view(), name='book_ticket-detail'),
]
