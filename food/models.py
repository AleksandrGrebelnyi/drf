from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(unique=True, max_length=50, db_index=True)

    def __str__(self):
        return f'{self.name}'


class Food(models.Model):
    title = models.CharField(max_length=225)
    recipe = models.TextField(max_length=1500)
    is_published = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='food/%Y/%m/%d/')
    cat = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('-is_published', )