import sqlite3
import os

class bd:

    def __init__(self):

        #LISTA DE MESES
        self.months = ['JANEIRO', 'FEVEREIRO', 'MARCO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO']

        caminhoAtual = os.getcwd()

        self.conection = sqlite3.connect('{}/ss.db'.format(caminhoAtual))
        self.cur = self.conection.cursor()
        
    def createTablesMonths(self, m):
        #CRIAR TABELAS DE MESES
        command = 'CREATE TABLE {} (data DATE, hora TEXT, servico TEXT, valor REAL, valor_manutecao REAL)'.format(m)
        
        self.cur.execute(command)
        self.conection.commit()

    def insertService(self, m, data, hora, servico, valor, valorManutencao):

        #INSERIR DADOS NA TABELA MES NA POSICAO M
        command = 'INSERT INTO {} (data, hora, servico, valor, valor_manutecao) VALUES("{}", "{}", "{}", {}, {})'.format(self.months[m], data, hora, servico, valor, valorManutencao)
        
        self.cur.execute(command)
        self.conection.commit()

a = bd()
a.createTablesMonths('NOVEMBRO')
#a.insertService(11, '15/10/2020', '10:00', 'UNHA', 20, 5)

