from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title