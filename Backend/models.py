from django.db import models

# Create your models here.
class tasks(models.Model):
    Time =models.DateField()
    Description = models.TextField(max_length=1000)
    Completed = models.BooleanField(default=True)
    Marked = models.BooleanField(default=False)
    def __str__(self):
        return self.Description