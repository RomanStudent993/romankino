from django.db import models
from django.urls import reverse


class Genre(models.Model):
    """Модель жанра фильма"""
    name = models.CharField(max_length=100, verbose_name="Название жанра", unique=True)
    
    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Director(models.Model):
    """Модель режиссёра"""
    name = models.CharField(max_length=200, verbose_name="Имя режиссёра")
    
    class Meta:
        verbose_name = "Режиссёр"
        verbose_name_plural = "Режиссёры"
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Film(models.Model):
    """Модель фильма"""
    title = models.CharField(max_length=200, verbose_name="Название фильма")
    description = models.TextField(verbose_name="Описание")
    genres = models.ManyToManyField(Genre, related_name="films", verbose_name="Жанры")
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Режиссёр")
    release_date = models.DateField(verbose_name="Дата выхода")
    poster = models.ImageField(upload_to='posters/', verbose_name="Постер", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    
    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
        ordering = ['-release_date', 'title']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('film_detail', kwargs={'pk': self.pk})
