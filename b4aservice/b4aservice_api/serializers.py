from rest_framework import serializers
from .models import Article
from .models import Service
class ArticleSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200, required=True)
    article_text = serializers.CharField(max_length=500,required=True)
    photos = serializers.ImageField()
    location = serializers.CharField(max_length=100, required=True)
    event_date = serializers.DateField()

    class Meta:
        model = Article
        fields = ('title', 'article_text', 'photos', 'location', 'event_date')






class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('service_name', 'service_description', 'bootstrap_icon')