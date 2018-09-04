from django.conf.urls import url
from django.urls import path

from processos.views import AreaConhecimentoList, GrupoProcessoList, ProcessoList, AreaConhecimentoDetalhe, \
    GrupoProcessoDetalhe, under_construction, ProcessoDetalhe

app_name = 'processos'

urlpatterns = [
    # Home
    path('', AreaConhecimentoList.as_view(), name='home'),
    url(r'^area_detalhe/(?P<pk>[0-9]+)/$', AreaConhecimentoDetalhe.as_view(), name="area_detalhe"),
    
    # Grupo de Processos
    path('grupo_processo', GrupoProcessoList.as_view(), name='grupo_processo'),
    url(r'^grupo_detalhe/(?P<pk>[0-9]+)/$', GrupoProcessoDetalhe.as_view(), name="grupo_detalhe"),
    
    # Processos
    path('processo', ProcessoList.as_view(), name='processo'),
    url(r'^processo_detalhe/(?P<pk>[0-9]+)/$', ProcessoDetalhe.as_view(), name="processo_detalhe"),
    
    # Under Construction
    url(r'^under_construction/$', under_construction, name="under_construction"),

]
