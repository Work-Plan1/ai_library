from django.db import models

from accounts.models import User


# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Book(TimeStampedModel):
    name = models.CharField(max_length=212)
    author = models.CharField(max_length=212)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='books/')
    book_link = models.URLField(blank=True, null=True)
    mini_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Comment(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='comments/')
    name = models.CharField(max_length=212)
    message = models.TextField()

    def __str__(self):
        return self.name


class Image(TimeStampedModel):
    image = models.ImageField(upload_to='about_images/')




class Social_links(TimeStampedModel):
    social_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.social_link


class About(TimeStampedModel):
    title = models.CharField(max_length=212)
    description = models.TextField()
    images = models.ForeignKey(Image, on_delete=models.CASCADE)
    video = models.FileField(upload_to='about_videos/')
    social_medias = models.ManyToManyField(Social_links)

    def __str__(self):
        return self.title

class Team(TimeStampedModel):
    full_name = models.CharField(max_length=212)
    image = models.ImageField(upload_to='teams/')
    occupation = models.CharField(max_length=212)
    portfolio_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.full_name
