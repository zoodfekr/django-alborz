from django.db import models

class Todo(models.Model):
    topic = models.CharField(max_length=100)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)