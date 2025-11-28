#!/usr/bin/env bash
# exit on error
set -o errexit

# Убеждаемся, что мы в корневой директории проекта
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Устанавливаем PYTHONPATH для поиска модулей (текущая директория должна быть в пути)
export PYTHONPATH="$SCRIPT_DIR:${PYTHONPATH}"

# Проверяем наличие необходимых файлов
if [ ! -f "manage.py" ]; then
    echo "Ошибка: manage.py не найден в текущей директории: $(pwd)"
    exit 1
fi

if [ ! -d "kinopoisk_project" ]; then
    echo "Ошибка: директория kinopoisk_project не найдена в: $(pwd)"
    exit 1
fi

# Установка зависимостей
pip install -r requirements.txt

# Сборка статических файлов
python manage.py collectstatic --no-input

# Применение миграций
python manage.py migrate

