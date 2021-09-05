from django.urls import path

from .views import dashboard, home, contato

app_name = 'core'
urlpatterns = [
    path("", home, name="home"),
    path('dashboard/', dashboard, name="dashboard"),
    path('contato/', contato, name="contato"),
]
