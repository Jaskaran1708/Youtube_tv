from django.contrib import admin
from .models import YouTubeVideo

@admin.register(YouTubeVideo)
class YouTubeVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_id', 'published_at')
    readonly_fields = ('video_id', 'thumbnail_url')  # Optional: prevent editing
    search_fields = ('title', 'video_id')
