from ckeditor.fields import RichTextField
from django.db import models


class Seminar_turlari(models.Model):
    title = models.CharField(max_length=255)
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
        verbose_name = 'Seminar turi'
        verbose_name_plural = 'Seminar turlari'


class Seminar(models.Model):
    title = models.CharField(max_length=255)
    subcontent = RichTextField(blank=True, null=True)
    seminar_id = models.ForeignKey(Seminar_turlari, on_delete=models.CASCADE, blank=True, null=True)
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
        verbose_name = 'Seminar'
        verbose_name_plural = 'Seminarlar'


class Seminar_majlislari(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    subcontent = RichTextField(blank=True, null=True)
    file = models.FileField(upload_to='media/Seminar_majlislari/files/', blank=True, null=True)
    data = models.DateField()
    seminar_id = models.ForeignKey(Seminar_turlari, on_delete=models.CASCADE, blank=True, null=True)
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
        verbose_name = 'Seminar majlisi'
        verbose_name_plural = 'Seminar majlislari'
