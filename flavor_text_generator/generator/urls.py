# generator/urls.py
from django.urls import path

from .views import GenerateFlavorTextView

urlpatterns = [
    path("generate/", GenerateFlavorTextView.as_view(), name="generate_flavor_text"),
]
