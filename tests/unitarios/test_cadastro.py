# -*- coding: utf-8 -*-
import unittest

from pagador_pagseguro_transparente import cadastro


class FormularioPagSeguroTransparente(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(FormularioPagSeguroTransparente, self).__init__(*args, **kwargs)
        self.formulario = cadastro.FormularioPagSeguroTransparente()

    def test_deve_ter_ativo(self):
        self.formulario.ativo.nome.should.be.equal('ativo')
        self.formulario.ativo.ordem.should.be.equal(1)
        self.formulario.ativo.label.should.be.equal('Pagamento ativo?')
        self.formulario.ativo.tipo.should.be.equal(cadastro.cadastro.TipoDeCampo.boleano)

    def test_deve_ter_tarifacao(self):
        self.formulario.tarifacao.nome.should.be.equal('aplicacao')
        self.formulario.tarifacao.ordem.should.be.equal(2)
        self.formulario.tarifacao.label.should.be.equal(u'Tarifação')
        self.formulario.tarifacao.tipo.should.be.equal(cadastro.cadastro.TipoDeCampo.escolha)
        self.formulario.tarifacao.opcoes.should.be.equal((('pagseguro', u'4,79% recebimento em 14 dias.'), ('pagseguro_399', u'3,99% recebimento em 30 dias.')))

    def test_deve_ter_valor_minimo_aceitado(self):
        self.formulario.valor_minimo_aceitado.nome.should.be.equal('valor_minimo_aceitado')
        self.formulario.valor_minimo_aceitado.ordem.should.be.equal(3)
        self.formulario.valor_minimo_aceitado.label.should.be.equal(u'Valor mínimo')
        self.formulario.valor_minimo_aceitado.tipo.should.be.equal(cadastro.cadastro.TipoDeCampo.decimal)

    def test_deve_ter_valor_minimo_parcela(self):
        self.formulario.valor_minimo_parcela.nome.should.be.equal('valor_minimo_parcela')
        self.formulario.valor_minimo_parcela.ordem.should.be.equal(4)
        self.formulario.valor_minimo_parcela.label.should.be.equal(u'Valor mínimo da parcela')
        self.formulario.valor_minimo_parcela.tipo.should.be.equal(cadastro.cadastro.TipoDeCampo.decimal)

    def test_deve_ter_mostrar_parcelamento(self):
        self.formulario.mostrar_parcelamento.nome.should.be.equal('mostrar_parcelamento')
        self.formulario.mostrar_parcelamento.ordem.should.be.equal(5)
        self.formulario.mostrar_parcelamento.label.should.be.equal(u'Marque para mostrar o parcelamento na listagem e na página do produto.')
        self.formulario.mostrar_parcelamento.tipo.should.be.equal(cadastro.cadastro.TipoDeCampo.boleano)

    def test_deve_ter_maximo_parcelas(self):
        self.formulario.maximo_parcelas.nome.should.be.equal('maximo_parcelas')
        self.formulario.maximo_parcelas.ordem.should.be.equal(6)
        self.formulario.maximo_parcelas.label.should.be.equal(u'Máximo de parcelas')
        self.formulario.maximo_parcelas.tipo.should.be.equal(cadastro.cadastro.TipoDeCampo.escolha)
        self.formulario.maximo_parcelas.opcoes.should.be.equal(self.formulario._PARCELAS)

    def test_deve_ter_quantidade_certa_parcelas(self):
        self.formulario._PARCELAS.should.be.equal([(18, 'Todas'), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17)])

    def test_deve_ter_parcelas_sem_juros(self):
        self.formulario.parcelas_sem_juros.nome.should.be.equal('parcelas_sem_juros')
        self.formulario.parcelas_sem_juros.ordem.should.be.equal(7)
        self.formulario.parcelas_sem_juros.label.should.be.equal('Parcelas sem juros')
        self.formulario.parcelas_sem_juros.tipo.should.be.equal(cadastro.cadastro.TipoDeCampo.escolha)