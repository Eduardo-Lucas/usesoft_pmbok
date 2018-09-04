from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from processos.models import Versao, GrupoProcesso, AreaConhecimento, Processo, Entrada, EntradaProcesso, Ferramenta, \
    FerramentaProcesso, Saida, SaidaProcesso


@admin.register(Versao)
class CategoriaResource(ImportExportModelAdmin):
    pass


@admin.register(GrupoProcesso)
class GrupoProcessoResource(ImportExportModelAdmin):
    pass


@admin.register(AreaConhecimento)
class AreaConhecimentoResource(ImportExportModelAdmin):
    pass


@admin.register(Processo)
class ProcessoResource(ImportExportModelAdmin):
    pass


@admin.register(Entrada)
class EntradaResource(ImportExportModelAdmin):
    pass


@admin.register(EntradaProcesso)
class EntradaProcessoResource(ImportExportModelAdmin):
    pass


@admin.register(Ferramenta)
class FerramentaResource(ImportExportModelAdmin):
    pass


@admin.register(FerramentaProcesso)
class FerramentaProcessoResource(ImportExportModelAdmin):
    pass


@admin.register(Saida)
class SaidaResource(ImportExportModelAdmin):
    pass


@admin.register(SaidaProcesso)
class SaidaProcessoResource(ImportExportModelAdmin):
    pass
