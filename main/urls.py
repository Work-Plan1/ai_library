from django.urls import path
from .views import CategoryList, BookList, BookDetail, AboutList, TeamList, ImageList, SocialMediaList, CommentList
urlpatterns = [
    path('books', BookList.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book_detail'),
    path('about/', AboutList.as_view(), name='about_list'),
    path('category/', CategoryList.as_view(), name='category_list'),
    path('team/', TeamList.as_view(), name='team_list'),
    path('image/', ImageList.as_view(), name='image_list'),
    path('social-media/', SocialMediaList.as_view(), name='social_media'),
    path('comment/', CommentList.as_view(), name='comment_list'),
]