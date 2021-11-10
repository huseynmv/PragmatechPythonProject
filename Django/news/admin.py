from django.contrib import admin
from .models import News, Tag
# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    fields = ('title','description','news_tag','img','slug')
admin.site.register(Tag)

