from rest_framework import serializers, validators
from rest_framework.relations import SlugRelatedField
from .models import Comment, News


class CommentSerializer(serializers.ModelSerializer):
    news_id = serializers.IntegerField(source='news.id', read_only=True)

    class Meta:
        fields = (
            'id',
            'news_id',
            'title',
            'date',
            'comment'
        )
        model = Comment


class NewsSerializer(serializers.ModelSerializer):
    comments_count = serializers.SerializerMethodField(
        method_name='get_comments_count',
    )

    def get_comments_count(self, obj):
        return obj.comments.all().count()
    

    class Meta:
        fields = (
            'id',
            'title',
            'date',
            'body',
            'deleted',
            'comments_count'
        )
        model = News


class NewsWithCommentsSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField(
        method_name='get_comments',
    )
    comments_count = serializers.SerializerMethodField(
        method_name='get_comments_count',
    )


    def get_comments(self, obj):
        comments = obj.comments.all()
        return CommentSerializer(comments, many=True).data
    

    def get_comments_count(self, obj):
        return obj.comments.all().count()


    class Meta:
        fields = (
            'id',
            'title',
            'date',
            'body',
            'deleted',
            'comments',
            'comments_count'
        )
        model = News
