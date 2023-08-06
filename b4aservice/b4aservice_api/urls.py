from .views import ArticleView
from .views import ServiceView
from .views import MemberView
# Update the import
from django.urls import path

urlpatterns = [
    path('articles/', ArticleView.as_view()) ,
    path('services/', ServiceView.as_view()),
    path('members/', MemberView.as_view())
 # Update the URL pattern
]
