# -*- coding: utf-8 -*-
from pagador import configuracoes, entidades
from pagador_pagseguro_transparente import cadastro

CODIGO_GATEWAY = 16
GATEWAY = 'pstransparente'


class TipoEnvio(object):
    def __init__(self, codigo):
        self.codigo = codigo

    @property
    def valor(self):
        if self.codigo == 'pac':
            return 1
        if 'sedex' in self.codigo:
            return 2
        return 3


class Item(entidades.BaseParaPropriedade):
    _chaves_alternativas_para_serializacao = {
        'item_id': 'ItemId',
        'item_description': 'ItemDescription',
        'item_amount': 'ItemAmount',
        'item_quantity': 'ItemQuantity',
    }


class Malote(entidades.Malote):
    _chaves_alternativas_para_serializacao = {
        'app_id': 'appId',
        'app_key': 'appKey',
        'payment_mode': 'paymentMode',
        'payment_method ': 'paymentMethod',
        'currency': 'currency',
        'credit_card_token': 'creditCardToken',
        'installment_quantity': 'installmentQuantity',
        'installment_value': 'installmentValue',
        'no_interest_installment_quantity': 'noInterestInstallmentQuantity',
        'reference': 'reference',
        'credit_card_holder_name': 'creditCardHolderName',
        'credit_card_holder_cpf': 'creditCardHolderCPF',
        'credit_card_holder_birth_date': 'creditCardHolderBirthDate',
        'credit_card_holder_area_code': 'creditCardHolderAreaCode',
        'credit_card_holder_phone': 'creditCardHolderPhone',
        'sender_name': 'senderName',
        'sender_cpf': 'senderCPF',
        'sender_cnpj': 'senderCNPJ',
        'sender_hash': 'senderHash',
        'sender_area_code': 'senderAreaCode',
        'sender_phone': 'senderPhone',
        'sender_email': 'senderEmail',
        'shipping_type': 'shippingType',
        'shipping_address_street': 'shippingAddressStreet',
        'shipping_address_number': 'shippingAddressNumber',
        'shipping_address_complement': 'shippingAddressComplement',
        'shipping_address_district': 'shippingAddressDistrict',
        'shipping_address_postal_code': 'shippingAddressPostalCode',
        'shipping_address_city': 'shippingAddressCity',
        'shipping_address_state': 'shippingAddressState',
        'shipping_address_country': 'shippingAddressCountry',
        'shipping_cost': 'shippingCost',
        'billing_address_street': 'billingAddressStreet',
        'billing_address_number': 'billingAddressNumber',
        'billing_address_complement': 'billingAddressComplement',
        'billing_address_district': 'billingAddressDistrict',
        'billing_address_postal_code': 'billingAddressPostalCode',
        'billing_address_city': 'billingAddressCity',
        'billing_address_state': 'billingAddressState',
        'billing_address_country': 'billingAddressCountry',
        'extra_amount': 'extraAmount',
        'redirect_url': 'redirectURL',
        'notification_url': 'notificationURL'
    }

    def __init__(self, configuracao):
        super(Malote, self).__init__(configuracao)
        self.app_id = None
        self.app_key = None
        self.payment_mode = 'default'
        self.payment_method = 'creditCard'
        self.installment_quantity = 1
        self.installment_value = None
        self.no_interest_installment_quantity = None
        self.currency = 'BRL'
        self.credit_card_token = None
        self.reference = None
        self.credit_card_holder_name = None
        self.credit_card_holder_cpf = None
        self.credit_card_holder_birth_date = None
        self.credit_card_holder_area_code = None
        self.credit_card_holder_phone = None
        self.sender_name = None
        self.sender_cpf = None
        self.sender_cnpj = None
        self.sender_hash = None
        self.sender_area_code = None
        self.sender_phone = None
        self.sender_email = None
        self.shipping_type = None
        self.shipping_address_street = None
        self.shipping_address_number = None
        self.shipping_address_complement = None
        self.shipping_address_district = None
        self.shipping_address_postal_code = None
        self.shipping_address_city = None
        self.shipping_address_state = None
        self.shipping_address_country = 'BRA'
        self.shipping_cost = None
        self.billing_address_street = None
        self.billing_address_number = None
        self.billing_address_complement = None
        self.billing_address_district = None
        self.billing_address_postal_code = None
        self.billing_address_city = None
        self.billing_address_state = None
        self.billing_address_country = 'BRA'
        self.extra_amount = None
        self.redirect_url = None
        self.notification_url = None

    def _cria_item(self, indice, item_pedido):
        indice += 1
        item_id = 'item_id{}'.format(indice)
        sku = self.formatador.trata_unicode_com_limite(item_pedido.sku, 100, ascii=True)
        setattr(self, item_id.format(indice), sku)
        self._chaves_alternativas_para_serializacao[item_id] = 'itemId{}'.format(indice)
        item_description = 'item_description{}'.format(indice)
        descricao = self.formatador.trata_unicode_com_limite(item_pedido.nome, 100, ascii=True)
        if not descricao:
            descricao = sku
        setattr(self, item_description, descricao)
        self._chaves_alternativas_para_serializacao[item_description] = 'itemDescription{}'.format(indice)
        item_amount = 'item_amount{}'.format(indice)
        setattr(self, item_amount, self.formatador.formata_decimal(item_pedido.preco_venda))
        self._chaves_alternativas_para_serializacao[item_amount] = 'itemAmount{}'.format(indice)
        item_quantity = 'item_quantity{}'.format(indice)
        setattr(self, item_quantity, self.formatador.formata_decimal(item_pedido.quantidade, como_int=True))
        self._chaves_alternativas_para_serializacao[item_quantity] = 'itemQuantity{}'.format(indice)

    def monta_conteudo(self, pedido, parametros_contrato=None, dados=None):
        notification_url = configuracoes.NOTIFICACAO_URL.format(GATEWAY, self.configuracao.loja_id)
        numero_telefone = pedido.cliente_telefone
        self.app_key = parametros_contrato['app_secret']
        self.app_id = parametros_contrato['app_id']
        self.reference = pedido.numero
        self.notification_url = '{}/notificacao'.format(notification_url)
        self.redirect_url = u'{}/resultado?next_url={}&referencia={}'.format(notification_url, dados['next_url'], pedido.numero)
        self.sender_name = pedido.cliente_nome_ascii
        self.sender_area_code = numero_telefone[0]
        self.sender_phone = numero_telefone[1]
        self.sender_email = self.formatador.trata_email_com_mais(pedido.cliente['email'])
        self.shipping_type = TipoEnvio(pedido.forma_envio).valor
        self.shipping_cost = self.formatador.formata_decimal(pedido.valor_envio)
        self.extra_amount = self.formatador.formata_decimal((pedido.valor_desconto * -1))
        self.shipping_address_street = self.formatador.trata_unicode_com_limite(pedido.endereco_entrega['endereco'], 80, ascii=True)
        self.shipping_address_number = pedido.endereco_entrega['numero']
        self.shipping_address_complement = self.formatador.trata_unicode_com_limite(pedido.endereco_entrega['complemento'], 40, ascii=True)
        self.shipping_address_district = self.formatador.trata_unicode_com_limite(pedido.endereco_entrega['bairro'], 60, ascii=True)
        self.shipping_address_postal_code = pedido.endereco_entrega['cep']
        self.shipping_address_city = self.formatador.trata_unicode_com_limite(pedido.endereco_entrega['cidade'], 60, ascii=True)
        self.shipping_address_state = pedido.endereco_entrega['estado']
        self.shipping_address_country = 'BRA'

        for indice, item in enumerate(pedido.itens):
            self._cria_item(indice, item)


class ConfiguracaoMeioPagamento(entidades.ConfiguracaoMeioPagamento):
    modos_pagamento_aceitos = {
        'cartoes': ['visa', 'mastercard', 'hipercard', 'amex']
    }

    def __init__(self, loja_id, codigo_pagamento=None, eh_listagem=False):
        self.campos = ['ativo', 'aplicacao', 'codigo_autorizacao', 'valor_minimo_aceitado', 'valor_minimo_parcela', 'mostrar_parcelamento', 'maximo_parcelas', 'parcelas_sem_juros']
        self.codigo_gateway = CODIGO_GATEWAY
        self.eh_gateway = True
        self.src_js_sdk = 'https://stc.{}pagseguro.uol.com.br/pagseguro/api/v2/checkout/pagseguro.directpayment.js'.format(
            'sandbox.' if (configuracoes.ENVIRONMENT == 'local' or configuracoes.ENVIRONMENT == 'development') else ''
        )
        super(ConfiguracaoMeioPagamento, self).__init__(loja_id, codigo_pagamento, eh_listagem=eh_listagem)
        if not self.eh_listagem:
            self.formulario = cadastro.FormularioPagSeguroTransparente()
            self.eh_aplicacao = True
