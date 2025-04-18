from django.db import models
from urllib.parse import urlparse, parse_qs
from datetime import datetime

class YouTubeVideo(models.Model):
    title = models.CharField(max_length=255)
    video_url = models.URLField(help_text="Paste full YouTube URL here", blank=True, null=True)  # New field
    video_id = models.CharField(max_length=20, unique=True, editable=False)
    thumbnail_url = models.URLField(blank=True)
    published_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        # Extract video ID from URL
        parsed_url = urlparse(self.video_url)
        if parsed_url.hostname in ["www.youtube.com", "youtube.com"]:
            query = parse_qs(parsed_url.query)
            self.video_id = query.get("v", [""])[0]
        elif parsed_url.hostname == "youtu.be":
            self.video_id = parsed_url.path.lstrip("/")

        # Optional: Auto-generate thumbnail URL if blank
        if not self.thumbnail_url and self.video_id:
            self.thumbnail_url = f"https://img.youtube.com/vi/{self.video_id}/hqdefault.jpg"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
