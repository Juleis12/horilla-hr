"""Public recruitment SEO endpoints."""

from django.http import HttpResponse
from django.urls import reverse


def robots_txt(request):
    """Expose crawl rules without blocking public job listings."""
    sitemap_url = request.build_absolute_uri(reverse("sitemap"))
    content = (
        "User-agent: *\n"
        "Allow: /recruitment/open-recruitments/\n"
        "Disallow: /recruitment/application-form/\n"
        "Disallow: /admin/\n"
        f"Sitemap: {sitemap_url}\n"
    )
    return HttpResponse(content, content_type="text/plain; charset=utf-8")


def sitemap_xml(request):
    """Publish the canonical public jobs index; application forms are noindex."""
    location = request.build_absolute_uri(reverse("open-recruitments"))
    content = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"  <url><loc>{location}</loc></url>\n"
        "</urlset>"
    )
    return HttpResponse(content, content_type="application/xml; charset=utf-8")
