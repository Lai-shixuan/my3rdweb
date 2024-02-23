# your_app/sitemaps.py

from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from . import views


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        # List of names of your static views
        html_files = views.get_names()
        return html_files

    def location(self, item):
        return reverse(f"hello:{item}")
