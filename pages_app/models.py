from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Page(models.Model):
    title = models.CharField(max_length=50, verbose_name='Título')
    content = RichTextField(verbose_name='Contenido')
    slug = models.CharField(max_length=150, verbose_name='URL Amigable')
    visible = models.BooleanField(verbose_name='Es visible')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha Actualización')

    class Meta:
        db_table = 'pages'
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'

    
    def __str__(self):
        return f"{self.title} ({'Visible' if self.visible == True else 'No Visible'})"
    