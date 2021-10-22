from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=127, null=True, blank=True)
    text = models.TextField(help_text='Bura esas melumati daxil edin...')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=63, verbose_name='Muellif', )

    def __str__(self):
        return f'Blog {self.title}'