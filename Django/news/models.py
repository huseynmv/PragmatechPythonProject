from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from core.utils import  unique_slug_generator
# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=63, blank=True, null=True)
    description = models.CharField(max_length=63, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    news_tag = models.ManyToManyField('Tag')
    img = models.ImageField(upload_to="news/", null=True)
    slug = models.SlugField(max_length=255, null=True,unique=True,blank=True)
    
    class Meta:
        verbose_name='news'
        verbose_name_plural='news'
        ordering = (
            'created_at',
        )
        
    def get_absolute_url(self):
        return reverse('news:news-detail', args=[self.slug])
    
    def __str__(self):
        return self.title
    
def slug_generator(sender, instance, *args, **kwargs):
        if not instance.slug:
            instance.slug = unique_slug_generator(instance)
            
pre_save.connect(slug_generator, sender=News)

class Tag(models.Model):
    title = models.CharField(max_length=63, null=True, blank=True)
    def __str__(self):
        return self.title
    
