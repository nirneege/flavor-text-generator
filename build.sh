#!/usr/bin/env bash
set -o errexit
pip install -r requirements.txt
cd flavor_text_generator
python manage.py collectstatic --no-input
python manage.py migrate
