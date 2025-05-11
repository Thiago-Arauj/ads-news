#form para criação de novas noticias

from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            'category_name',
            'title',
            'abstract',
            'content',
            'image',
            'in_carousel',
            'is_featured',
            'is_sponsored',
        ]
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }
