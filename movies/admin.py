from django.contrib import admin
from django.utils.html import format_html
from .models import Film, Genre, Director


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['title', 'director', 'release_date', 'display_genres', 'poster_preview']
    list_filter = ['genres', 'release_date', 'director']
    search_fields = ['title', 'description']
    filter_horizontal = ['genres']
    date_hierarchy = 'release_date'
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'description', 'poster')
        }),
        ('Детали', {
            'fields': ('director', 'genres', 'release_date')
        }),
    )
    
    def display_genres(self, obj):
        """Отображение жанров в списке"""
        return ", ".join([genre.name for genre in obj.genres.all()[:3]])
    display_genres.short_description = "Жанры"
    
    def poster_preview(self, obj):
        """Превью постера в админке"""
        if obj.poster:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />', obj.poster.url)
        return "Нет постера"
    poster_preview.short_description = "Постер"
