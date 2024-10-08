from ckeditor.fields import RichTextField
from django.db import models


class Fotogalereya(models.Model):
    img_url = models.ImageField(upload_to='media/Markazlar_bolimlar/fotogalereya/')

    def __str__(self):
        return str(self.img_url)

    class Meta:
        verbose_name = 'Fotogalereya'
        verbose_name_plural = 'Fotogalereya'


class Slider(models.Model):
    img_url = models.ImageField(upload_to='media/Markazlar_bolimlar/slider/')

    def __str__(self):
        return str(self.img_url)

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Slider'


class Xodimlar(models.Model):
    name = models.CharField(max_length=255)
    lavozim = models.CharField(max_length=255)
    ilmiy_daraja = models.CharField(max_length=255)
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
        return f'{self.name} ({self.lavozim})'

    class Meta:
        verbose_name = 'Xodim'
        verbose_name_plural = 'Xodimlar'


class MarkazlarBolimlar(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    tarix = RichTextField(blank=True, null=True)
    xodimlar = models.ManyToManyField(Xodimlar, related_name='markazlar_bolimlar', )
    fotogalereya = models.ManyToManyField(Fotogalereya, related_name='markazlar_bolimlar',)
    slider = models.ManyToManyField(Slider, related_name='markazlar_bolimlar',)

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

    class Meta:
        verbose_name = 'Markazlar bo\'limi'
        verbose_name_plural = 'Markazlar bo\'limlari'









































# class Markazlar_bolimlar(models.Model):
#     title = models.CharField(max_length=255)
#     content = RichTextField(blank=True, null=True)
#     file = models.FileField(upload_to='media/Markazlar_bolimlar/files/', blank=True, null=True)
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
#     class Meta:
#         verbose_name = 'Markazlar bolimlar'
#         verbose_name_plural = 'Markazlar bolimlar'
#
#     def __str__(self):
#         return self.title or ''
#
#
# class Bolimlar_tarix(models.Model):
#     title = models.CharField(max_length=255)
#     content = RichTextField(blank=True, null=True)
#     center_id = models.ForeignKey(Markazlar_bolimlar, on_delete=models.CASCADE, related_name='tarix', blank=True,
#                                   null=True)
#     file = models.FileField(upload_to='media/Bolimlar_tarix/files/', blank=True, null=True)
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
#     class Meta:
#         verbose_name = 'Bolimlar tarix'
#         verbose_name_plural = 'Bolimlar tarix'
#
#     def __str__(self):
#         return self.title or ''


# class Tadqiqot(models.Model):
#     title = models.CharField(max_length=255)
#     content = RichTextField(blank=True, null=True)
#     center_id = models.ForeignKey(Markazlar_bolimlar, on_delete=models.CASCADE, related_name='tadqiqot', blank=True,
#                                   null=True)
#     file = models.FileField(upload_to='media/Tadqiqot/files/', blank=True, null=True)
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
#     class Meta:
#         verbose_name = 'Tadqiqot'
#         verbose_name_plural = 'Tadqiqot'
#
#     def __str__(self):
#         return self.title or ''


# class Azolar(models.Model):
#     title = models.CharField(max_length=255)
#     content = RichTextField(blank=True, null=True)
#     birth = models.DateField()
#     sphere = models.CharField(max_length=255)
#     position = models.CharField(max_length=255)
#     academic_degree = models.CharField(max_length=255)
#     email = models.EmailField()
#     center_id = models.ForeignKey(Markazlar_bolimlar,on_delete=models.CASCADE, related_name='azolar',blank=True,
#                                   null=True)
#     file = models.FileField(upload_to='media/Azolar/files/', blank=True, null=True)
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
#     class Meta:
#         verbose_name = 'Azolar'
#         verbose_name_plural = 'Azolar'
#
#     def __str__(self):
#         return self.title or ''
#
#
# class Azolarsub(models.Model):
#     link = models.URLField(verbose_name='link', blank=True, null=True)
#     title = models.CharField(max_length=60)
#     name = models.ForeignKey(Azolar, on_delete=models.CASCADE, related_name='azolarsub')
#
#
# class Rasm(models.Model):
#     title = models.CharField(max_length=255)
#     content = RichTextField(blank=True, null=True)
#     image = models.ImageField(upload_to='images')
#     center_id = models.ForeignKey(Markazlar_bolimlar, on_delete=models.CASCADE, related_name='rasm', blank=True,
#                                   null=True)
#     file = models.FileField(upload_to='media/Rasm/files/', blank=True, null=True)
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
#     class Meta:
#         verbose_name = 'Rasm'
#         verbose_name_plural = 'Rasm'
#
#     def __str__(self):
#         return self.title or ''


# class Video(models.Model):
#     title = models.CharField(max_length=255)
#     content = RichTextField(blank=True, null=True)
#     link = models.URLField(verbose_name='link', blank=True, null=True)
#     center_id = models.ForeignKey(Markazlar_bolimlar,on_delete=models.CASCADE, related_name='video', blank=True,
#                                   null=True)
#     file = models.FileField(upload_to='media/Rasm/files/', blank=True, null=True)
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
#     class Meta:
#         verbose_name = 'Video'
#         verbose_name_plural = 'Videos'
#
#     def __str__(self):
#         return self.title or ''

