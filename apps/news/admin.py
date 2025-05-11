from django.contrib import admin
from apps.news import models
from django.utils.html import format_html


# admin.site.register(models.News)
@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'abstract',
        'content',
        'image',
        'category_name',
        'display_category_color',
        'is_featured',
        'is_sponsored',
    )  # Columns in list view
    search_fields = ('title', 'content', 'category_name')
    list_filter = (
        'is_featured',
        'is_sponsored',
        'category_name',
    )  # Filters in sidebar
    ordering = ('-created_at',)  # Default ordering
    date_hierarchy = 'created_at'  # Adds date drilldown navigation
    readonly_fields = ('category_color', 'created_at', 'updated_at')

    def display_category_color(self, obj):
        return format_html(
            '<span style="display:inline-block; width: 20px; height: 20px; '
            'background-color: {}; border-radius: 50%; border: 1px solid #ccc;"></span>',
            obj.category_color
        )
    display_category_color.short_description = 'Cor'
