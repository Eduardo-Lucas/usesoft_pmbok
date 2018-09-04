from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from processos.models import AreaConhecimento, GrupoProcesso, Processo


"""
    Áreas de Conhecimento
"""


class AreaConhecimentoList(ListView):
    model = AreaConhecimento
    context_object_name = 'area_conhecimento'
    template_name = 'processos/area_conhecimento/list.html'

    def get_queryset(self):
        valor = self.request.GET.get('q')
        if valor:
            object_list = self.model.objects.filter(
                Q(descricao__icontains=valor)
            )
        else:
            object_list = self.model.objects.all()

        paginator = Paginator(object_list, 10)  # Show 2 produtos per page

        page = self.request.GET.get('page')
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            queryset = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            queryset = paginator.page(paginator.num_pages)

        # return object_list
        return queryset
    

class AreaConhecimentoDetalhe(DetailView):
    model = AreaConhecimento
    context_object_name = 'area_conhecimento'
    template_name = 'processos/area_conhecimento/detail.html'
    

"""
    Fim Áreas de Conhecimento
"""

"""
    Grupos de Processos
"""


class GrupoProcessoList(ListView):
    model = GrupoProcesso
    context_object_name = 'grupo_processo'
    template_name = 'processos/grupo_processo/list.html'

    def get_queryset(self):
        valor = self.request.GET.get('q')
        if valor:
            object_list = self.model.objects.filter(
                Q(descricao__icontains=valor)
            )
        else:
            object_list = self.model.objects.all()

        paginator = Paginator(object_list, 10)  # Show 10 records per page

        page = self.request.GET.get('page')
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            queryset = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            queryset = paginator.page(paginator.num_pages)

        # return object_list
        return queryset
    

class GrupoProcessoDetalhe(DetailView):
    model = GrupoProcesso
    context_object_name = 'grupo_processo'
    template_name = 'processos/grupo_processo/detail.html'


"""
    Fim Grupos de Processos
"""


"""
    Processos
"""


class ProcessoList(ListView):
    model = Processo
    context_object_name = 'processo'
    template_name = 'processos/processo/list.html'

    def get_queryset(self):
        valor = self.request.GET.get('q')
        if valor:
            object_list = self.model.objects.filter(
                Q(descricao__icontains=valor) |
                Q(codigo__icontains=valor) |
                Q(name__icontains=valor)
            )
        else:
            object_list = self.model.objects.all()

        paginator = Paginator(object_list, 6)  # Show 6 produtos per page

        page = self.request.GET.get('page')
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            queryset = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            queryset = paginator.page(paginator.num_pages)

        # return object_list
        return queryset
    

class ProcessoDetalhe(DetailView):
    model = Processo
    context_object_name = 'processo'
    template_name = 'processos/processo/detail.html'


"""
    Fim Processos
"""


def under_construction(request):
    return render(request, 'under_construction.html')
