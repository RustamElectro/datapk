from django.urls import path
from api.views import news_list, news_id


urlpatterns = [
    path('news/', news_list),
    path('news/<int:news_id>', news_id),
]