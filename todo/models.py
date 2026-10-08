from django.db import models

# Create your models here.
class Task(models.Model):
    Title = models.CharField()
    Description = models.TextField(blank=True)
    Completed = models.BooleanField(default=False)
    Created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title
    
