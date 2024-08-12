from django.db import models
from ckeditor.fields import RichTextField
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
from ckeditor.fields import RichTextField
from django.db import models


class Talablar(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    sub_content = RichTextField(blank=True, null=True)
    file = models.FileField(upload_to='media/archive/files/', blank=True, null=True)
    STATUS_CHOICES = [
        ('published', 'Published'),
        ('not_published', 'Not Published'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='published',
    )
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Talab'
        verbose_name_plural = 'Talablar'


class Tahrirchi(models.Model):
    title = models.CharField(max_length=255)
    ish_joyi = models.CharField(max_length=255)
    lavozimi = models.CharField(max_length=255)
    STATUS_CHOICES = [
        ('published', 'Published'),
        ('not_published', 'Not Published'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='published',
    )
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tahrirchi'
        verbose_name_plural = 'Tahrirchilar'


class ArxivSon(models.Model):
    content = models.TextField(blank=True, null=True)
    file_url = models.FileField(upload_to='media/arxiv_sonlar/', blank=True, null=True)
    STATUS_CHOICES = [
        ('published', 'Published'),
        ('not_published', 'Not Published'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='published',
    )
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content[:50] if self.content else 'No Content'

    class Meta:
        verbose_name = 'ArxivSon'
        verbose_name_plural = 'ArxivSon'


class Maqola(models.Model):
    tahrirchilar = models.ManyToManyField(Tahrirchi, related_name='maqolalar', blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    arxiv_sonlar = models.ManyToManyField(ArxivSon, related_name='maqolalar', blank=True, null=True)
    STATUS_CHOICES = [
        ('published', 'Published'),
        ('not_published', 'Not Published'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='published',
    )
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content[:50] if self.content else "No Content"

    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'


class Avtoreferat(models.Model):
    title = models.CharField(max_length=255)
    cover_img = models.ImageField(upload_to='media/avtoreferatlar/covers/', blank=True, null=True)
    file = models.FileField(upload_to='media/avtoreferatlar/files/', blank=True, null=True)
    STATUS_CHOICES = [
        ('published', 'Published'),
        ('not_published', 'Not Published'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='published',
    )
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Avtoreferat'
        verbose_name_plural = 'Avtoreferat'


class ElektronKitob(models.Model):
    title = models.CharField(max_length=255)
    cover_img = models.ImageField(upload_to='media/elektron_kitoblar/covers/', blank=True, null=True)
    file = models.FileField(upload_to='media/elektron_kitoblar/files/', blank=True, null=True)
    STATUS_CHOICES = [
        ('published', 'Published'),
        ('not_published', 'Not Published'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='published',
    )
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ElektronKitob'
        verbose_name_plural = 'ElektronKitoblar'


class Manba(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    cover_img = models.ImageField(upload_to='media/manbalar/covers/', blank=True, null=True)
    file = models.FileField(upload_to='media/manbalar/files/', blank=True, null=True)
    STATUS_CHOICES = [
        ('published', 'Published'),
        ('not_published', 'Not Published'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='published',
    )
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Manba'
        verbose_name_plural = 'Manbalar'


class ArxivMenu(models.Model):
    davr_oraligi = models.CharField(max_length=50)
    content = RichTextField(blank=True, null=True)
    STATUS_CHOICES = [
            ('published', 'Published'),
            ('not_published', 'Not Published'),
        ]
    status = models.CharField(
            max_length=20,
            choices=STATUS_CHOICES,
            default='published',
        )
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.davr_oraligi

    class Meta:
        verbose_name = 'ArxivMenu'
        verbose_name_plural = 'ArxivMenu'


class Arxiv(models.Model):
    yil = models.CharField(max_length=255, blank=True, null=True)
    nashr_raqami = models.CharField(max_length=255, blank=True, null=True)
    file_url = models.FileField(upload_to='media/Arxiv/files', blank=True, null=True)
    arxiv_list = models.ManyToManyField(ArxivMenu, related_name='arxiv_list', blank=True, null=True)

    STATUS_CHOICES = [
        ('published', 'Published'),
        ('not_published', 'Not Published'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='published',
    )

    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.yil} - {self.nashr_raqami}"

    class Meta:
        verbose_name = 'Arxiv'
        verbose_name_plural = 'Arxivlar'
