
from import_export import resources

from processos.models import Versao, GrupoProcesso, AreaConhecimento, Processo, Entrada, EntradaProcesso, Ferramenta, \
    FerramentaProcesso, Saida, SaidaProcesso


class VersaoResource(resources.ModelResource):
    class Meta:
        model = Versao
        import_id_fields = ('numero',)
        fields = ('numero',)


class GrupoProcessoResource(resources.ModelResource):
    class Meta:
        model = GrupoProcesso
        fields = ('numero', 'sequencia', 'descricao',)


class AreaConhecimentoResource(resources.ModelResource):
    class Meta:
        model = AreaConhecimento
        fields = '__all__'


class ProcessoResource(resources.ModelResource):
    class Meta:
        model = Processo
        fields = '__all__'


class EntradaResource(resources.ModelResource):
    class Meta:
        model = Entrada
        fields = '__all__'


class EntradaProcessoResource(resources.ModelResource):
    class Meta:
        model = EntradaProcesso
        fields = '__all__'
        
        
class FerramentaResource(resources.ModelResource):
    class Meta:
        model = Ferramenta
        fields = '__all__'


class FerramentaProcessoResource(resources.ModelResource):
    class Meta:
        model = FerramentaProcesso
        fields = '__all__'


class SaídaResource(resources.ModelResource):
    class Meta:
        model = Saida
        fields = '__all__'


class SaidaProcessoResource(resources.ModelResource):
    class Meta:
        model = SaidaProcesso
        fields = '__all__'
