from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    date_of_birth = models.DateTimeField(auto_now_add=False)
    email = models.EmailField()
    address = models.TextField()

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
