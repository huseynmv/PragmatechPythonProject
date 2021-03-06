from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=127, null=True, blank=True)
    text = models.TextField(help_text='Main info..')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title