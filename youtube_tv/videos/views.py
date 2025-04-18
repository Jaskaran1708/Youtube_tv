from rest_framework import viewsets
from .models import YouTubeVideo
from .serializers import YouTubeVideoSerializer

class YouTubeVideoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = YouTubeVideo.objects.order_by('-published_at')
    serializer_class = YouTubeVideoSerializer
