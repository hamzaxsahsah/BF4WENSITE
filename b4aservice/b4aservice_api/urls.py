from .views import ArticleView
from .views import ServiceView
# Update the import
from django.urls import path

urlpatterns = [
    path('articles/', ArticleView.as_view()) ,
     path('services/', ServiceView.as_view()) # Update the URL pattern
]
