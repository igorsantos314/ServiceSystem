from pylab import *
from serviceSystem import bd
from numpy import arange
from matplotlib.pyplot import * 

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

    def generateGraphYear(self, revenue, spending):
        
        #DADOS DA AMOSTRAGEM
        #REVENUE E SPENDING
        months = ['JAN', 'FEV', 'MARC', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']

        barWidth = 0.30
        matplotlib.pyplot.figure(figsize=(10,5))

        #POSICAO DAS BARRAS
        r1 = np.arange(len(revenue))
        r2 = [(x + barWidth) for x in r1]

        #CRIANDO BARRAS
        matplotlib.pyplot.bar(r1, revenue, color='Cyan', width=barWidth, label='REVENUE')
        matplotlib.pyplot.bar(r2, spending, color='DarkCyan', width=barWidth, label='SPENGING')

        #ADICIONANDO LEGENDAS AS BARRAS
        matplotlib.pyplot.xlabel('MONTHS')
        matplotlib.pyplot.xticks([r + barWidth for r in range(len(revenue))], months)
        matplotlib.pyplot.ylabel('VALUE R$')
        matplotlib.pyplot.title('GRAPH OF YEAR')

        #CRIANDO E EXIBINDO O GRAFICO
        matplotlib.pyplot.legend()
        matplotlib.pyplot.show()
        
plotGraphs()
#a.gerarGraficosReceitaMeses()
#a.gerirFinanceiro(200, 20, 100, 100)
