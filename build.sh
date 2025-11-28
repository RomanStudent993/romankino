#!/usr/bin/env bash
# exit on error
set -o errexit

# Убеждаемся, что мы в корневой директории проекта
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Отладочная информация
echo "Текущая директория: $(pwd)"
echo "Содержимое директории:"
ls -la

# Устанавливаем PYTHONPATH для поиска модулей (текущая директория должна быть в пути)
export PYTHONPATH="$SCRIPT_DIR:${PYTHONPATH}"

# Проверяем наличие необходимых файлов
if [ ! -f "manage.py" ]; then
    echo "Ошибка: manage.py не найден в текущей директории: $(pwd)"
    echo "Ищем manage.py в родительских директориях..."
    # Попробуем найти manage.py в родительской директории (на случай, если проект в поддиректории)
    if [ -f "../manage.py" ]; then
        echo "Найден manage.py в родительской директории, переходим туда"
        cd ..
        SCRIPT_DIR="$(pwd)"
        export PYTHONPATH="$SCRIPT_DIR:${PYTHONPATH}"
    else
        exit 1
    fi
fi

if [ ! -d "kinopoisk_project" ]; then
    echo "Ошибка: директория kinopoisk_project не найдена в: $(pwd)"
    echo "Ищем kinopoisk_project в родительских директориях..."
    if [ -d "../kinopoisk_project" ]; then
        echo "Найден kinopoisk_project в родительской директории"
        cd ..
        SCRIPT_DIR="$(pwd)"
        export PYTHONPATH="$SCRIPT_DIR:${PYTHONPATH}"
    else
        echo "Проверьте, что все файлы проекта закоммичены в Git:"
        echo "  git add kinopoisk_project/"
        echo "  git commit -m 'Add kinopoisk_project directory'"
        echo "  git push"
        exit 1
    fi
fi

echo "Проверка пройдена. Рабочая директория: $(pwd)"

# Установка зависимостей
pip install -r requirements.txt

# Сборка статических файлов
python manage.py collectstatic --no-input

# Применение миграций
python manage.py migrate
