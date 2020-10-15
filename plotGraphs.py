from pylab import *

class plotGraphs:
    
    def __init__(self):
        pass

    def gerarGraficoFinanceiro(self, receita, manutencao, gastos, lucro):
        pos = arange(4) + .5

        valores = (receita, manutencao, gastos, lucro)
        topicos = ('RECEITA', 'MANUT.', 'GASTOS', 'LUCRO')

        #GERAR GRAFICO
        barh(pos, valores, align='center', color='PaleGoldenrod')
        yticks(pos, topicos)

        #INFORMAÇÕES
        title('VISÃO DE NEGÓCIO')
        title('Service System')
        xlabel('Valor em R$')
        ylabel('Metricas')

        #LINHAS CORTANDO O GRÁFICO
        grid(True)

        #EXIBIR GRAFICO
        show()

a = plotGraphs()
#a.gerirFinanceiro(200, 20, 100, 100)
