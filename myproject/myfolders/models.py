from django.db import models
from django.db import models


# Create your models here.
class Files(models.Model):
    file = models.FileField(null=True)
    title = models.CharField(max_length=255, default='sample_title')
    uploaded_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
