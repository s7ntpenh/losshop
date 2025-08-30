from typing import Dict, Any


def site_settings(request) -> Dict[str, Any]:
    """Injects site-wide settings (e.g., background video URL) into context."""
    try:
        from .models import SiteSettings
        settings = SiteSettings.objects.first()
        bg_url = settings.background_video.url if settings and settings.background_video else None
    except Exception:
        # Be defensive if DB isn't migrated yet or storage errors occur
        bg_url = None
    return {
        'background_video_url': bg_url,
    }

