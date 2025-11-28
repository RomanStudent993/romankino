#!/usr/bin/env bash
# exit on error
set -o errexit

# Установка зависимостей
pip install -r requirements.txt

# Сборка статических файлов
python manage.py collectstatic --no-input

# Применение миграций
python manage.py migrate

