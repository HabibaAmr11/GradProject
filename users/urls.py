from django.urls import path

from users.views import UserListCreateAPIView, UserDetailAPIView, ContactUsListCreateAPIView, ContactUsDetailAPIView

urlpatterns = [
    path('user', UserListCreateAPIView.as_view(), name='user-create'),
    path('user/<int:pk>', UserDetailAPIView.as_view(), name='user-detail'),
    path('contact_us', ContactUsListCreateAPIView.as_view(), name='contact_us-create'),
    path('contact_us/<int:pk>', ContactUsDetailAPIView.as_view(), name='contact_us-detail'),
]
