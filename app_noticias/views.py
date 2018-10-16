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
        'noticias': noticias,
        'porcentagem': porcentangem
        })
    except Categoria.DoesNotExist:
        raise Http404('Categoria não encontrada')

def estatisticas_de_publicacao_de_noticias(request):
    autores = Pessoa.objects.all()
    autor_com_mais_publicacoes = None
    quant_noticias_do_autor = 0
    for autor in autores:
        quant_noticias = Noticia.objects.filter(autor=autor).count()
        if quant_noticias > quant_noticias_do_autor:
            quant_noticias_do_autor = quant_noticias
            autor_com_mais_publicacoes = autor
    categorias = Categoria.objects.all()
    porcentagens_por_categoria = []
    for categoria in categorias:
        porcentagens_por_categoria.append([categoria,(Noticia.objects.filter(categoria=categoria).count()/Noticia.objects.count())*100])
    return render(request, 'app_noticias/estatisticas.html', {'autores': autores.count(),
    'autor_com_mais_publicacoes': autor_com_mais_publicacoes,
    'quant_noticias_do_autor': quant_noticias_do_autor,
    'porcentagens_por_categoria': porcentagens_por_categoria,
    })