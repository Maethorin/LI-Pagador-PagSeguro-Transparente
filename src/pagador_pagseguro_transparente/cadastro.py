# -*- coding: utf-8 -*-

from li_common.padroes import cadastro


class FormularioPagSeguroTransparente(cadastro.Formulario):
    _PARCELAS = [(x, x) for x in range(1, 18)]
    _PARCELAS.insert(0, (18, "Todas"))
    ativo = cadastro.CampoFormulario('ativo', 'Pagamento ativo?', tipo=cadastro.TipoDeCampo.boleano, ordem=1)
    valor_minimo_aceitado = cadastro.CampoFormulario('valor_minimo_aceitado', u'Valor mínimo', requerido=False, decimais=2, ordem=3, tipo=cadastro.TipoDeCampo.decimal, texto_ajuda=u'Informe o valor mínimo para exibir esta forma de pagamento.')
    valor_minimo_parcela = cadastro.CampoFormulario('valor_minimo_parcela', u'Valor mínimo da parcela', requerido=False, decimais=2, ordem=4, tipo=cadastro.TipoDeCampo.decimal)
    mostrar_parcelamento = cadastro.CampoFormulario('mostrar_parcelamento', u'Marque para mostrar o parcelamento na listagem e na página do produto.', tipo=cadastro.TipoDeCampo.boleano, requerido=False, ordem=5)
    maximo_parcelas = cadastro.CampoFormulario('maximo_parcelas', u'Máximo de parcelas', tipo=cadastro.TipoDeCampo.escolha, requerido=False, ordem=6, texto_ajuda=u'Quantidade máxima de parcelas para esta forma de pagamento.', opcoes=_PARCELAS)
    parcelas_sem_juros = cadastro.CampoFormulario('parcelas_sem_juros', 'Parcelas sem juros', tipo=cadastro.TipoDeCampo.escolha, requerido=False, ordem=7, texto_ajuda=u'Número de parcelas sem juros para esta forma de pagamento.', opcoes=_PARCELAS)
