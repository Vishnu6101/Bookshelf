from django.db import models
from django.contrib.auth.models import User
from gdstorage.storage import GoogleDriveStorage

# Create your models here.

gd_storage = GoogleDriveStorage()

class Author(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return f"{self.name}"

class Book(models.Model):
    title = models.CharField(max_length=256, null=True)
    pageCount = models.IntegerField(default=0)
    thumbnailUrl = models.CharField(max_length=256, null=True)
    shortDescription = models.CharField(max_length=1024, null=True)
    longDescription = models.TextField(null=True)
    category = models.CharField(max_length=256, null=True)
    publishedOn = models.DateTimeField(null=True)
    isbn = models.CharField(max_length=256, null=True)
    authors = models.ManyToManyField(Author)
    book = models.FileField(upload_to='books', storage=gd_storage, null=True)
    bookURL = models.URLField(null=True)
    # image = models.ImageField(upload_to='images', null=True)

    def __str__(self) -> str:
        return f"{self.id}. {self.title}"


class Review(models.Model):
    body = models.TextField()
    userId = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    createdAt = models.DateTimeField(auto_now=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.id}. {self.createdAt}"