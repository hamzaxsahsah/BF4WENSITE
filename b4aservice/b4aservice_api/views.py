from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Article
from .serializers import ArticleSerializer
from .models import Service
from .serializers import ServiceSerializer
from .models import Member
from .serializers import MemberSerializer

class ArticleView(APIView):
  
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response({'status': 'success', 'articles': serializer.data}, status=status.HTTP_200_OK)
  
    def post(self, request, *args, **kwargs):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status': 'error', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)







class ServiceView(APIView):
  
    def get(self, request, *args, **kwargs):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response({'status': 'success', 'services': serializer.data}, status=status.HTTP_200_OK)
  
    def post(self, request, *args, **kwargs):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status': 'error', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        





class MemberView(APIView):
  
    def get(self, request, *args, **kwargs):
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response({'status': 'success', 'members': serializer.data}, status=status.HTTP_200_OK)
  
    def post(self, request, *args, **kwargs):
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status': 'error', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
