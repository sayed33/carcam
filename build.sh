#!/usr/bin/env bash

# تثبيت المتطلبات
pip install -r requirements.txt

# جمع ملفات static
python manage.py collectstatic --noinput

# تنفيذ الترحيلات (migrations)
python manage.py migrate
