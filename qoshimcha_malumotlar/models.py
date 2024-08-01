from django.db import models
from ckeditor.fields import RichTextField


class Institut_tarixi(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    subcontent = RichTextField(blank=True, null=True)
    file = models.FileField(upload_to='media/institut_tarixi/files/', blank=True, null=True)
    base_file = models.FileField(upload_to='media/institut_tarixi/base_files/', blank=True, null=True)
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
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Institut tarixi'
        verbose_name_plural = 'Institut tarixi'


# class Memory_hujjatlar(models.Model):
#     title = models.CharField(max_length=255)
#     file = models.FileField(upload_to='media/memory_hujjatlar/files/', blank=True, null=True)
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
#         verbose_name = 'Memory hujjat'
#         verbose_name_plural = 'Memory hujjatlar'
#
#
# class Elonlar(models.Model):
#     title = models.CharField(max_length=255)
#     content = RichTextField(blank=True, null=True)
#     file = models.FileField(upload_to='media/elonlar/files/', blank=True, null=True)
#     STATUS_CHOICES = [
#         ('published', 'Published'),
#         ('not_published', 'Not Published'),
#     ]
#     status = models.CharField(
#         max_length=20,
#         choices=STATUS_CHOICES,
#         default='published',
#     )
#     TYPE_CHOICES = [
#         ('KENGASH', 'Kengash'),
#         ('DOKTORANTURA', 'Doktorantura'),
#         ('SEMINAR', 'Seminar'),
#     ]
#     type = models.CharField(
#         max_length=20,
#         choices=TYPE_CHOICES,
#         default='KENGASH',
#     )
#     order = models.IntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = 'Elon'
#         verbose_name_plural = 'Elonlar'
#

class Aloqa(models.Model):
    faks = models.CharField(max_length=255, verbose_name='Faks', blank=True, null=True)
    email = models.EmailField(blank=True, null=True, verbose_name='Email')
    phone = models.CharField(max_length=255, verbose_name='Telefon', blank=True, null=True)
    adress = models.CharField(max_length=255, verbose_name='Manzil', blank=True, null=True)
    lat = models.FloatField(blank=True, null=True, verbose_name='Latitude')
    long = models.FloatField(blank=True, null=True, verbose_name='Longitude')
    youtube = models.CharField(max_length=255, verbose_name='Youtube', blank=True, null=True)
    telegram = models.CharField(max_length=255, verbose_name='Telegram', blank=True, null=True)
    instagram = models.CharField(max_length=255, verbose_name='Instagram', blank=True, null=True)
    facebook = models.CharField(max_length=255, verbose_name='Facebook', blank=True, null=True)
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
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = 'Aloqa'
        verbose_name_plural = 'Aloqalar'


class Karusel(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    file = models.FileField(upload_to='media/karusel/files/', blank=True, null=True)
    STATUS_CHOICES = [
        ('published', 'Published'),
        ('not_published', 'Not Published'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='published',
    )
    link = models.URLField(blank=True, null=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Karusel'
        verbose_name_plural = 'Karusel'


class Rahbariyat(models.Model):
    title = models.CharField(max_length=255)
    position = models.CharField(max_length=255, blank=True, null=True)
    degree = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    days = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='media/rahbariyat/images/', blank=True, null=True)
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
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Rahbariyat'
        verbose_name_plural = 'Rahbariyat'


class Tashkiliy_tuzulma(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    file = models.FileField(upload_to='media/tashkiliy_tuzulma/files/', blank=True, null=True)
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
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tashkiliy tuzulma'
        verbose_name_plural = 'Tashkiliy tuzulma'


class Yangiliklar(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    subcontent = RichTextField(blank=True, null=True)
    file = models.FileField(upload_to='media/yangiliklar/files/', blank=True, null=True)
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
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'


class Havolalar(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='media/havolalar/files/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
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
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Havola'
        verbose_name_plural = 'Havolalar'
