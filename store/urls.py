"""
URL de l'application store
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.listing),
]
