from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from .models import News, Comment
from .serializers import NewsSerializer, CommentSerializer, NewsWithCommentsSerializer



from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import datetime as dt
import pytz

utc=pytz.UTC


@api_view(('GET',))
def news_list(request):
    news = News.objects.all()
    serializer = NewsSerializer(news, many=True)
    return Response({'news': serializer.data, 'news_count': news.count()})


@api_view(('GET',))
def news_id(request, news_id):
    news = get_object_or_404(News, id=news_id)
    time = utc.localize(dt.datetime.now())
    
    if news.deleted or news.date > time:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = NewsWithCommentsSerializer(news, context={'request': request})
    return Response(serializer.data, status=status.HTTP_200_OK)
