from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Film, Genre


def film_list(request):
    """Список всех фильмов"""
    films = Film.objects.all()
    
    # Поиск по названию
    search_query = request.GET.get('search', '')
    if search_query:
        films = films.filter(title__icontains=search_query)
    
    # Фильтр по жанру
    genre_filter = request.GET.get('genre', '')
    if genre_filter:
        films = films.filter(genres__id=genre_filter)
    
    # Пагинация
    paginator = Paginator(films, 12)  # 12 фильмов на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Все жанры для фильтра
    genres = Genre.objects.all()
    
    context = {
        'page_obj': page_obj,
        'genres': genres,
        'search_query': search_query,
        'selected_genre': genre_filter,
    }
    
    return render(request, 'movies/film_list.html', context)


def film_detail(request, pk):
    """Детальная страница фильма"""
    film = get_object_or_404(Film, pk=pk)
    
    # Похожие фильмы (по жанрам)
    similar_films = Film.objects.filter(genres__in=film.genres.all()).exclude(pk=film.pk).distinct()[:6]
    
    context = {
        'film': film,
        'similar_films': similar_films,
    }
    
    return render(request, 'movies/film_detail.html', context)
