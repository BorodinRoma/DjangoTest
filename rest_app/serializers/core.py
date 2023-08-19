from rest_framework import serializers
from core.models import Bookmark, Collection


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = '__all__'


class BookmarkCreateSerializer(serializers.Serializer):
    url = serializers.CharField()


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'


class CollectionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["name", "description", "bookmarks"]


class CollectionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["name", "description", "bookmarks"]


class AddBookmarkSerializer(serializers.Serializer):
    collection_id = serializers.IntegerField()
    bookmarks = serializers.ListField(child=serializers.IntegerField())
