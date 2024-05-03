from rest_framework import serializers
from .models import Category, Comment, Book, About, Image, Social_links, Team


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user',)


class BookSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'name', 'mini_description', 'author', 'image', 'book_link', 'category', 'comment']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class Social_linksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social_links
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    social_medias = Social_links()
    images = ImageSerializer()

    class Meta:
        model = About
        fields = ['title','description','images']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
