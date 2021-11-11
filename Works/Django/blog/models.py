from django.db import models

# Create your models here.

class Blog(models.Model):
    blog_title = models.CharField(max_length=127, null=True, blank=True)
    blog_subtitle = models.CharField(max_length=127,null=True,blank=True)
    blog_desc = models.CharField(max_length=127,null=True,blank=True)
    
    def __str__(self) :
        return self.blog_title
    
    class Meta:
        verbose_name='blog'
        verbose_name_plural='blogs'
