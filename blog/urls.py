# ezt a fájlt Attila hozta létre 2025.02.11-én url-ek részére

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]