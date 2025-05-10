from django.db import models
from apps.core.models import BaseModel

class Category(BaseModel):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nome")
    color = models.CharField(max_length=7, default='#000000', verbose_name="Cor") 
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return str(self.name)

class News(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Título")
    abstract = models.CharField(max_length=255, verbose_name="Resumo", null=True, blank=True)
    content = models.TextField(verbose_name="Conteúdo")
    image = models.ImageField(upload_to="news/", null=True, blank=True, verbose_name="Imagem")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='news', verbose_name="Categoria da Notícia")
    is_featured = models.BooleanField(default=False, verbose_name="Destacar")
    is_sponsored = models.BooleanField(default=False, verbose_name="Patrocinada")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Notícia"
        verbose_name_plural = "Notícias"

    def __str__(self):
        return str(self.title)