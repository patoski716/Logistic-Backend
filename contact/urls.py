# urls.py
from django.urls import path
from .views import ContactFormAPIView,GetContactFormAPIView

urlpatterns = [
    path('postcontact/', ContactFormAPIView.as_view(), name='post-contact'),
    path('getcontact/', GetContactFormAPIView.as_view(), name='get-contact'),

]
