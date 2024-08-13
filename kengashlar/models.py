from ckeditor.fields import RichTextField
from django.db import models


class Institut_ken_azolari(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='media/institut_ken_azolari/files/', blank=True, null=True)
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
        verbose_name = 'Institut ken. azolari'
        verbose_name_plural = 'Institut ken. azolari'


class Ilmiy_kengash_majlis(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    subcontent = RichTextField(blank=True, null=True)
    file = models.FileField(upload_to='media/ilmiy_kengash_majlis/files/', blank=True, null=True)
    date = models.DateField(blank=True, null=True)
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
        verbose_name = 'Ilmiy kengash majlis'
        verbose_name_plural = 'Ilmiy kengash majlis'

#
# class Qabul_korib_gan_dissertatsiya(models.Model):
#     title = models.CharField(max_length=255)
#     content = RichTextField(blank=True, null=True)
#     file = models.FileField(upload_to='media/qabul_korib_gan_dissertatsiya/files/', blank=True, null=True)
#     STATUS_CHOICES = [
#         ('accepted', 'Accepted'),
#         ('not_accepted', 'Not Accepted'),
#     ]
#     status = models.CharField(
#         max_length=20,
#         choices=STATUS_CHOICES,
#         default='accepted',
#     )
#     order = models.IntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = 'Qabul korib.gan dissertatsiya'
#         verbose_name_plural = 'Qabul korib.gan dissertatsiya'
#
#
# class Shifr_va_passport(models.Model):
#     title = models.CharField(max_length=255)
#     file = models.FileField(upload_to='media/shifr_va_passport/files/', blank=True, null=True)
#     date = models.DateField(blank=True, null=True)
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
#         verbose_name = 'Shifr va passport'
#         verbose_name_plural = 'Shifr va passport'
#
#
# class Dissertatsiya_va_avtoref(models.Model):
#     title = models.CharField(max_length=255)
#     content = RichTextField(blank=True, null=True)
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
#         verbose_name = 'Dissertatsiya va avtoref'
#         verbose_name_plural = 'Dissertatsiya va avtoref'
#
#
# class Dissertatsiya_fayllar(models.Model):
#     title = models.CharField(max_length=255)
#     content = RichTextField(blank=True, null=True)
#     file = models.FileField(upload_to='media/dissertatsiya_fayllar/files/', blank=True, null=True)
#     base_file = models.FileField(upload_to='media/dissertatsiya_fayllar/base_files/', blank=True, null=True)
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
#         verbose_name = 'Dissertatsiya fayllar'
#         verbose_name_plural = 'Dissertatsiya fayllar'


class Yosh_olimlar(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    file = models.FileField(upload_to='media/yosh_olimlar/files/', blank=True, null=True)
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
        verbose_name = 'Yosh olim'
        verbose_name_plural = 'Yosh olimlar'

#
# class Yosh_olimlar_azolari(models.Model):
#     title = models.CharField(max_length=255)
#     position = models.CharField(max_length=255, blank=True, null=True)
#     degree = models.CharField(max_length=255, blank=True, null=True)
#     contact = models.CharField(max_length=255, blank=True, null=True)
#     email = models.EmailField(max_length=255, blank=True, null=True)
#     file = models.FileField(upload_to='media/yosh_olimlar_azolari/files/', blank=True, null=True)
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
#         verbose_name = 'Yosh olim azoi'
#         verbose_name_plural = 'Yosh olimlar azolari'
#
#
# class Maruzalar(models.Model):
#     title = models.CharField(max_length=255)
#     content = RichTextField(blank=True, null=True)
#     subcontent = RichTextField(blank=True, null=True)
#     file = models.FileField(upload_to='media/maruzalar/files/', blank=True, null=True)
#     data = models.DateField(blank=True, null=True)
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
#         verbose_name = 'Maruza'
#         verbose_name_plural = 'Maruzalar'

from django.db import models


class Azolar(models.Model):
    shifr = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    ish_joy = models.CharField(max_length=255)
    lavozim = models.CharField(max_length=255)
    ilmiy_darajasi = models.CharField(max_length=255)
    ilmiy_unvoni = models.CharField(max_length=255)
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
        return self.name

    class Meta:
        verbose_name = 'Azolar'
        verbose_name_plural = 'Azolar'


class DissertatsiyaIshlar(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='media/dissertatsiya_ishlar/files/')
    isAccepted = models.BooleanField(default=False)
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
        verbose_name = 'DissertatsiyaIshlar'
        verbose_name_plural = 'DissertatsiyaIshlar'


class Content(models.Model):
    azolar = models.ManyToManyField(Azolar, related_name='contents', blank=True,)
    content = RichTextField(blank=True, null=True)
    dissertatsiya_ishlar = models.ManyToManyField(DissertatsiyaIshlar, related_name='contents',)
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
        verbose_name = 'Content'
        verbose_name_plural = 'Content'




