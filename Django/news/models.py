from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=63, blank=True, null=True)
    description = models.CharField(max_length=63, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='news'
        verbose_name_plural='news'
        ordering = (
            'created_at',
        )
    def __str__(self):
        return self.title
    
    
