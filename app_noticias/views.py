from django.shortcuts import render
from django.views.generic import ListView
from .models import *
from django.http import Http404

def HomePageView(request):
    noticias = Noticia.objects.all()
    return render(request, 'app_noticias/home.html', {'noticias': noticias})

def noticias_resumo(request):
    total= Noticia.objects.count()
    noticias = Noticia.objects.all()
    return render(request, 'app_noticias/resumo.html', {'total': total,
    'noticias': noticias,
    })

def noticia_detalhes(request,id):
    try:
        noticia = Noticia.objects.get(pk=id)
        return render(request, 'app_noticias/detalhes.html', {'noticia': noticia})
    except Noticia.DoesNotExist:
        raise Http404('Notícia não encontrada')

def noticias_por_autor(request, id_autor):
    try:
        autor = Pessoa.objects.get(pk=id_autor)
        noticias = Noticia.objects.filter(autor=autor)
        return render(request, 'app_noticias/autor.html', {'autor': autor, 
        'noticias': noticias,
        })
    except Pessoa.DoesNotExist:
        raise Http404('Autor não encontrado')

def noticias_por_categoria(request, nomeCategoria):
    try:
        categoria = Categoria.objects.get(nome=nomeCategoria)
        noticias = Noticia.objects.filter(categoria=categoria)
        porcentangem = (noticias.count()/Noticia.objects.count())*100
        return render(request, 'app_noticias/categoria.html', {'categoria': categoria,
        'noticias',
        'porcentagme': porcentangem
        })
    except Categoria.DoesNotExist:
        raise Http404('Categoria não encontrada')