# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Timeline,Tracking
from .serializers import TimelineSerializer,TrackingSerializer
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView

# timeline
class TimelineFormAPIView(APIView):
    def post(self, request, format=None):
        serializer = TimelineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetTimelineFormAPIView(ListAPIView):
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer


class TimelineDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer

# tracking
class TrackingFormAPIView(APIView):
    def post(self, request, format=None):
        serializer = TrackingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetTrackingFormAPIView(ListAPIView):
    queryset = Tracking.objects.all()
    serializer_class = TrackingSerializer


class TrackingDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Tracking.objects.all()
    serializer_class = TrackingSerializer

