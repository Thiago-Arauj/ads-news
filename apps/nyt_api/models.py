from django.db import models
from apps.core.models import BaseModel


# Create your models here.
class News(BaseModel):
    section = models.CharField(
        max_length=255,
        verbose_name="Seção",
        db_index=True
    )
    title = models.CharField(max_length=255, verbose_name="Titulo")
    abstract = models.TextField(verbose_name="Resumo")
    news_url = models.URLField(verbose_name="Link da matéria", unique=True)
    image_url = models.URLField(verbose_name="Url da imagem")
    published_date = models.DateTimeField(
        verbose_name="Data de publicação",
        db_index=True
    )
