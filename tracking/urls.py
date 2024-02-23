from django.urls import path
from .views import TimelineDetailAPIView,TimelineFormAPIView,GetTimelineFormAPIView,TrackingDetailAPIView,TrackingFormAPIView,GetTrackingFormAPIView

urlpatterns = [
    # timeline
    path('posttimeline/', TimelineFormAPIView.as_view(), name='post-timeline'),
    path('gettimeline/', GetTimelineFormAPIView.as_view(), name='get-timeline'),
    path('timeline/<int:pk>/', TimelineDetailAPIView.as_view(), name='timeline-detail'),
    # tracking
    path('posttracking/', TrackingFormAPIView.as_view(), name='posttracking'),
    path('gettracking/', GetTrackingFormAPIView.as_view(), name='gettracking'),
    path('tracking/<int:pk>/', TrackingDetailAPIView.as_view(), name='tracking-detail'),
]
