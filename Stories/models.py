from django.db import models


class Story(models.Model):
    title = models.CharField(max_length=64, verbose_name='Heading')
    content = models.TextField(verbose_name='content')
    published = models.DateTimeField(auto_now_add=True, verbose_name='Date of publication')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Category')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'
        ordering = ['-published']


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Category')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
