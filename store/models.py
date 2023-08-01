from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=90, db_index=True)
    slug=models.SlugField(max_length=250, unique=True)

    class Meta:
        verbose_name_plural="categories"

    def __str(self):
        return self.name


