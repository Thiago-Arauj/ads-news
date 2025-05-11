from django.db import models
from apps.core.models import BaseModel


class Category(BaseModel):
    class CategoryChoices(models.TextChoices):
        SCIENCE = 'SCI', 'Ciencias'
        BUSINESS = 'BIS', 'Negócios'
        WORLD = 'WRL', 'Mundo'
        HEALTH = 'HEL', 'Saúde'
        THIRD_PARTY = 'TPN', 'Noticias de terceiros'

    category_name = models.CharField(
        max_length=3,
        choices=CategoryChoices.choices,
        unique=True,
        default=CategoryChoices.WORLD,
        verbose_name="Categoria"
    )
    category_color = models.CharField(
        max_length=7,
        default='#000000',
        verbose_name="Cor"
    )

    COLOR_MAPPING = {
        CategoryChoices.SCIENCE: '#4CAF50',
        CategoryChoices.BUSINESS: '#2196F3',
        CategoryChoices.WORLD: '#9C27B0',
        CategoryChoices.HEALTH: '#F44336',
        CategoryChoices.THIRD_PARTY: '#607D8B',
    }

    def save(self, *args, **kwargs):
        if self.category_name in self.COLOR_MAPPING:
            self.category_color = self.COLOR_MAPPING[self.category_name]
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
        ordering = ['-created_at']
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return str(self.name)


class News(Category):
    title = models.CharField(max_length=255, verbose_name="Título")
    abstract = models.CharField(
        max_length=255,
        verbose_name="Resumo",
        null=True,
        blank=True
    )
    content = models.TextField(verbose_name="Conteúdo")
    image = models.ImageField(
        upload_to="news/",
        null=True,
        blank=True,
        verbose_name="Imagem"
    )
    is_featured = models.BooleanField(default=False, verbose_name="Destacar")
    is_sponsored = models.BooleanField(
        default=False,
        verbose_name="Patrocinada"
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Notícia"
        verbose_name_plural = "Notícias"

    def __str__(self):
        return str(self.title)


class ThirdPartyNews(Category):
    section = models.CharField(
        max_length=255,
        verbose_name="Seção",
        db_index=True
    )
    title = models.CharField(max_length=255, verbose_name="Titulo")
    abstract = models.TextField(verbose_name="Resumo")
    news_url = models.URLField(verbose_name="Link da matéria", unique=True)
    image_url = models.URLField(verbose_name="Url da imagem")
    published_date = models.DateTimeField(verbose_name="Data de publicação")

    class Meta:
        ordering = ['-published_date']
        verbose_name = 'Notícias de terceiros'
