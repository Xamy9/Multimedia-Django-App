from django.db import models

# Create your models here.
class Mediacontent(models.Model):
    title  = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    video  = models.FileField(upload_to='videos/', blank=True, null=True)
    audio  = models.FileField(upload_to='audio/', blank=True, null=True)
    uploaded_at  = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    