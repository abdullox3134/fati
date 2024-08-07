# from django.db import models
# from ckeditor.fields import RichTextField
#
#
# class Category(models.Model):
#     title = models.CharField(max_length=255)
#     STATUS_CHOICES = [
#         ('published', 'Published'),
#         ('not_published', 'Not Published'),
#     ]
#     status = models.CharField(
#         max_length=20,
#         choices=STATUS_CHOICES,
#         default='published',
#     )
#     order = models.IntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = 'Categoriya'
#         verbose_name_plural = 'Categoriyalar'
#
#
# class DissertationsAndAbstracts(models.Model):
#     title = models.CharField(max_length=255)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', blank=True, null=True)
#     content = models.TextField(blank=True, null=True)
#     image = models.ImageField(upload_to='media/archive/image/', blank=True, null=True)
#     file = models.FileField(upload_to='media/archive/files/', blank=True, null=True)
#     STATUS_CHOICES = [
#         ('published', 'Published'),
#         ('not_published', 'Not Published'),
#     ]
#     status = models.CharField(
#         max_length=20,
#         choices=STATUS_CHOICES,
#         default='published',
#     )
#     order = models.IntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = 'Disertatsiya va avtorefarat'
#         verbose_name_plural = 'Disertatsiya va avtorefaratlar'
#
#
# class Editor(models.Model):
#     title = models.CharField(max_length=255)
#     position = models.CharField(max_length=255, blank=True, null=True)
#     degree = models.CharField(max_length=255, blank=True, null=True)
#     sphere = models.CharField(max_length=255, blank=True, null=True)
#     content = RichTextField(blank=True, null=True)
#     email = models.EmailField(unique=True, blank=True, null=True)
#     file = models.FileField(upload_to='media/archive/files/', blank=True, null=True)
#     STATUS_CHOICES = [
#         ('published', 'Published'),
#         ('not_published', 'Not Published'),
#     ]
#     status = models.CharField(
#         max_length=20,
#         choices=STATUS_CHOICES,
#         default='published',
#     )
#     order = models.IntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = 'Tahririyat'
#         verbose_name_plural = 'Taxririyatchilar'
#
#
# class Archive(models.Model):
#     title = models.CharField(max_length=255)
#     content = RichTextField(blank=True, null=True)
#     sub_content = RichTextField(blank=True, null=True)
#     file = models.FileField(upload_to='media/archive/files/', blank=True, null=True)
#     base_file = models.FileField(upload_to='media/archive/base_file/', blank=True, null=True)
#     STATUS_CHOICES = [
#         ('published', 'Published'),
#         ('not_published', 'Not Published'),
#     ]
#     status = models.CharField(
#         max_length=20,
#         choices=STATUS_CHOICES,
#         default='published',
#     )
#     order = models.IntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = 'Arxiv'
#         verbose_name_plural = 'Arxivlar'
#
#
# class Requirements(models.Model):
#     title = models.CharField(max_length=255)
#     content = RichTextField(blank=True, null=True)
#     sub_content = RichTextField(blank=True, null=True)
#     file = models.FileField(upload_to='media/archive/files/', blank=True, null=True)
#     STATUS_CHOICES = [
#         ('published', 'Published'),
#         ('not_published', 'Not Published'),
#     ]
#     status = models.CharField(
#         max_length=20,
#         choices=STATUS_CHOICES,
#         default='published',
#     )
#     order = models.IntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = 'Talab'
#         verbose_name_plural = 'Talablar'
#
#
from ckeditor.fields import RichTextField
from django.db import models

class Tahrirchi(models.Model):
    title = models.CharField(max_length=255)
    ish_joyi = models.CharField(max_length=255)
    lavozimi = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ArxivSon(models.Model):
    content = models.TextField(blank=True, null=True)
    file_url = models.FileField(upload_to='media/arxiv_sonlar/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content[:50] if self.content else 'No Content'


class Maqola(models.Model):
    tahrirchilar = models.ManyToManyField(Tahrirchi, related_name='maqolalar', blank=True)
    content = RichTextField(blank=True, null=True)
    arxiv_sonlar = models.ManyToManyField(ArxivSon, related_name='maqolalar', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content[:50] if self.content else "No Content"


class Avtoreferat(models.Model):
    title = models.CharField(max_length=255)
    cover_img = models.ImageField(upload_to='avtoreferatlar/covers/', blank=True, null=True)
    file = models.FileField(upload_to='avtoreferatlar/files/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ElektronKitob(models.Model):
    title = models.CharField(max_length=255)
    cover_img = models.ImageField(upload_to='elektron_kitoblar/covers/', blank=True, null=True)
    file = models.FileField(upload_to='elektron_kitoblar/files/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Manba(models.Model):
    title = models.CharField(max_length=255)
    cover_img = models.ImageField(upload_to='manbalar/covers/', blank=True, null=True)
    file = models.FileField(upload_to='manbalar/files/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
