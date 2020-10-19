from pylab import *
from serviceSystem import bd

class plotGraphs:
    
    def __init__(self):
        #OBJETO DE BANCO DE DADOS
        self.bancoDados = bd()

    def gerarGraficoFinanceiro(self, receita, manutencao, gastos, lucro):
        pos = arange(4) + .5

        valores = (receita, manutencao, gastos, lucro)
        topicos = ('RECEITA', 'MANUT.', 'GASTOS', 'LUCRO')

        #GERAR GRAFICO
        barh(pos, valores, align='center', color='DarkMagenta')
        yticks(pos, topicos)

        #INFORMAÇÕES
        title('VISÃO DE NEGÓCIO')
        xlabel('Valor em R$')
        ylabel('Metricas')

        #LINHAS CORTANDO O GRÁFICOs
        grid(True)

        #EXIBIR GRAFICO
        show()

    def gerarGraficosReceitaMeses(self, receitas):
        pos = arange(12) + .5

        valores = tuple(receitas)
        topicos = tuple(self.bancoDados.months.__reversed__())

        #GERAR GRAFICO
        barh(pos, valores, align='center', color='DarkMagenta')
        yticks(pos, topicos)

        #INFORMAÇÕES
        title('RECEITA DE TODOS OS MESES')
        xlabel('Valor em R$')
        ylabel('Meses')

        #LINHAS CORTANDO O GRÁFICO
        grid(True)

        #EXIBIR GRAFICO
        show()

a = plotGraphs()
#a.gerarGraficosReceitaMeses()
#a.gerirFinanceiro(200, 20, 100, 100)
