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


@admin.register(models.ThirdPartyNews)
class ThirdPartyNewsAdmin(admin.ModelAdmin):
    # Display fields in list view
    list_display = (
        'title',
        'section',
        'category_name',
        'display_category_color',
        'published_date',
        'news_url_short'
    )
    list_filter = ('section', 'published_date')
    search_fields = ('title', 'abstract')
    ordering = ('-published_date',)
    readonly_fields = (
        'section',
        'title',
        'category_name',
        'display_category_color',
        'abstract',
        'news_url',
        'image_url',
        'published_date'
    )

    # Fields to display in detail view
    fieldsets = (
        (None, {
            'fields': (
                'title',
                'section',
                'category_name',
                'display_category_color',
                'published_date'
            )
        }),
        ('Conteúdo', {
            'fields': ('abstract', 'news_url', 'image_url'),
            'classes': ('collapse',)
        }),
    )

    def display_category_color(self, obj):
        return format_html(
            '<span style="display:inline-block; width: 20px; height: 20px; '
            'background-color: {}; border-radius: 50%; border: 1px solid #ccc;"></span>',
            obj.category_color
        )
    display_category_color.short_description = 'Cor'

    # Custom method to display shortened URL
    def news_url_short(self, obj):
        return obj.news_url[:50] + '...' if len(obj.news_url) > 50 else obj.news_url
    news_url_short.short_description = 'URL'

    # Disable add/delete permissions
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    # Make all fields read-only when editing
    def get_readonly_fields(self, request, obj=None):
        return [f.name for f in self.model._meta.fields]
