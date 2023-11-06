from django.urls import path, include
from rest_framework.routers import SimpleRouter
from api.views import news_list, news_id #NewsViewSet, CommentViewSet, 

#router = SimpleRouter()


#router.register(r'news/\d+', NewsViewSet)
#router.register('comments', CommentViewSet)

urlpatterns = [
#    path('', include(router.urls)),
    path('news/', news_list),
    path('news/<int:news_id>', news_id),
]