from django.db import models
from tinymce.models import HTMLField
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField
# Create your models here.


class Category(MPTTModel):
    title = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['title']

    #def __str__(self):
    #   return self.title


class News(models.Model):
    title = models.CharField(max_length=100)
    content = HTMLField(blank=True)
    category = TreeManyToManyField(Category, blank=True)
    created_at = models.DateTimeField()

