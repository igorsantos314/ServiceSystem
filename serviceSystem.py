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
        command = 'CREATE TABLE {} (data DATE, hora TEXT, servico TEXT, nome_cliente TEXT, valor REAL, valor_manutecao REAL)'.format(m)
        
        self.cur.execute(command)
        self.conection.commit()

    def insertService(self, m, data, hora, servico, nomeCliente, valor, valorManutencao):

        #INSERIR DADOS NA TABELA MES NA POSICAO M
        command = 'INSERT INTO {} (data, hora, servico, nome_cliente, valor, valor_manutecao) VALUES("{}", "{}", "{}", "{}", {}, {})'.format(self.months[m-1], data, hora, servico, nomeCliente, valor, valorManutencao)
        
        self.cur.execute(command)
        self.conection.commit()

    def getService(self, day, month, year):

        #EXIBIR TODOS OS DADOS DE UMA TABELA MES, PELA DATA ESPECIFICA
        show = "SELECT * FROM {} WHERE data = '{}/{}/{}'".format(self.months[month-1], day, month, year)
        #print(show)

        self.cur.execute(show)
        service = self.cur.fetchall()

        return service

    def verifyServiceDate(self, day, month, year):

        #EXIBIR TODOS OS DADOS DE UMA TABELA MES, PELA DATA ESPECIFICA
        show = "SELECT * FROM {} WHERE data = '{}/{}/{}'".format(self.months[month-1], day, month, year)

        self.cur.execute(show)
        service = self.cur.fetchall()

        #CASO EXISTA ALGUM SERVICO
        return len(service) != 0

a = bd()
#for i in a.months:
#    a.createTablesMonths(i)
#a.insertService(10, '15/10/2020', '10:00', 'UNHA', 'Igor Santos', 20, 5)
#a.insertService(10, '15/10/2020', '13:00', 'ALONGAMENTO DA UNHA', 'ELLEN ALTA', 40, 5)
#a.insertService(10, '13/10/2020', '13:00', 'ALONGAMENTO DA UNHA', 'ELLEN ALTA', 40, 5)
#print(a.getService(15, 10, 2020))
#print(a.verifyServiceDate(20, 10, 2020))