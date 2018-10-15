from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView, name='home'),
    path('noticias/resumo/', views.noticias_resumo, name='resumo'),
    path('noticias/detalhes/<id>/', views.noticia_detalhes, name='detalhes'),
    path('noticias/autor/<id_autor>/', views.noticias_por_autor, name='autor'),
]