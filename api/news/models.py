from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='images/', blank=True, null=True)
    content = models.TextField()
    published = models.DateTimeField()
    prediction = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title 