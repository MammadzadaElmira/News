from django.db import models

# Create your models here.

class Feed(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=3000)
    city = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.title} "




