from django.urls import path
from . import views

html_files = views.get_names()
app_name = 'hello'


# The page below is article index page, and with some sub links.
urlpatterns = [path('', views.index, name='articles_index')]

urlpatterns += [
    # Generate sub links for links
    # This is using list comprehensions, and all path are using the same view function.
    path(f'{filename}/', views.generic_html_view, {'filename': filename}, name=f'{filename}')
    for filename in html_files
]
