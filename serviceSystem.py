import sqlite3
import os
from random import randint

class bd:

    def __init__(self):

        #LISTA DE MESES
        self.months = ['JANEIRO', 'FEVEREIRO', 'MARCO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO']

        caminhoAtual = os.getcwd()

        self.conection = sqlite3.connect('{}/ss.db'.format(caminhoAtual))
        self.cur = self.conection.cursor()
        
    def createTablesMonths(self, m):
        #CRIAR TABELAS DE MESES
        command = F'CREATE TABLE {m} (id serial, data DATE, hora TEXT, servico TEXT, nome_cliente TEXT, valor REAL, valor_manutecao REAL)'
        
        self.cur.execute(command)
        self.conection.commit()

    def createTablesGastos(self):
        #CRIAR TABELAS DE GASTOS
        command = 'CREATE TABLE GASTOS (itens TEXT, valor REAL)'
        
        self.cur.execute(command)
        self.conection.commit()

    def insertService(self, m, data, hora, servico, nomeCliente, valor, valorManutencao):
        
        #INSERIR DADOS NA TABELA MES NA POSICAO M
        command = 'INSERT INTO {} (data, hora, servico, nome_cliente, valor, valor_manutecao) VALUES("{}", "{}", "{}", "{}", {}, {})'.format(self.months[m-1], data, hora, servico, nomeCliente, valor, valorManutencao)
        print(command)

        self.cur.execute(command)
        self.conection.commit()

    def insertGastos(self, data, itens, valor):

        #INSERIR DADOS NA TABELA GASTOS
        command = F'INSERT INTO GASTOS (data, itens, valor) VALUES("{data}", "{itens}", {valor})'
        
        self.cur.execute(command)
        self.conection.commit()

    def getService(self, day, month, year):

        #EXIBIR TODOS OS DADOS DE UMA TABELA MES, PELA DATA ESPECIFICA
        show = "SELECT * FROM {} WHERE data = '{}/{}/{}'".format(self.months[month-1], day, month, year)
        print(show)
        
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

    def getDataNegocio(self):

        receita = 0
        manutencao = 0
        gastos = 0

        #VARRER TODOS OS MESES
        for i in self.months:

            #PEGAR O VALOR E O VALOR PARA MANUTENAO DE CADA MES
            show = "SELECT valor, valor_manutecao FROM {}".format(i)

            self.cur.execute(show)
            service = self.cur.fetchall()

            #SOMA A RECEITA
            for s in service:
                receita += s[0]
                manutencao += s[1]

        #VARRER TODOS OS GASTOS
        show = "SELECT valor FROM GASTOS"

        self.cur.execute(show)
        listaGastos = self.cur.fetchall()

        #VARRE A LISTA DE GASTOS E VAI SOMANDO
        for g in listaGastos:
            gastos += g[0]

        #CALCULAR LUCRO
        lucro = receita - gastos

        #RETORNA A TUPLA DE INFORMAÇÕES
        return (receita, manutencao, gastos, lucro)
        
    def getAllServices(self):

        listaGastos = []

        #VARRER TODOS OS MESES
        for m in self.months:
            show = f"SELECT * FROM {m}"

            self.cur.execute(show)

            for service in self.cur.fetchall():
                listaGastos.append(service)

        return listaGastos

    def getReceitaAllMonths(self, ano):
        
        listaReceitaMeses = []

        #VARRER TODOS OS MESES
        for m in self.months:

            #PEGAR O VALOR E O VALOR PARA MANUTENAO DE CADA MES
            show = "SELECT valor from {} WHERE data like '%{}'".format(m, ano)

            self.cur.execute(show)
            service = self.cur.fetchall()

            #SOMA A RECEITA
            receita = 0

            for s in service:
                receita += s[0]

            listaReceitaMeses.append(receita)
        
        return listaReceitaMeses

    def getDespesasAllMonths(self, ano):
        listaDespesaMeses = []

        #VARRER TODOS OS MESES
        for m in range(1, 13):

            #PEGAR O VALOR E O VALOR PARA MANUTENAO DE CADA MES
            show = "SELECT valor from GASTOS WHERE data like '%/{}/{}'".format(m, ano)

            self.cur.execute(show)
            service = self.cur.fetchall()

            #SOMA A DESPESA
            despesa = 0

            for s in service:
                despesa += s[0]

            listaDespesaMeses.append(despesa)

        return listaDespesaMeses


    def editService(self, id, mes, atributoEdit, newValor):
        command = f'UPDATE {self.months[mes-1]} SET {atributoEdit} = "{newValor}" WHERE id = {id}'
        
        self.cur.execute(command)
        self.conection.commit()

    def dropService(self, mes, data, nomeCliente, hora, servico):
        command = f'DELETE FROM {self.months[mes-1]} WHERE data="{data}" AND nome_cliente = "{nomeCliente}" AND servico = "{servico}" AND hora = "{hora}"'
        #print(command)

        self.cur.execute(command)
        self.conection.commit()

    # ----------------------------------------- SETOR DE TESTES DE SOFTWARE -----------------------------------------
    def dropAllTables(self):

        for m in self.months:
            #DELETAR A TABELA
            command = F'DROP TABLE {m}'

            self.cur.execute(command)
            self.conection.commit()

    def testGastos(self):
        
        #INSERIR DESPESAS NVZS NOS 12 MESES
        for m in range(1, 13):

            #ITERAR NVZS
            nRandom = randint(10, 50)

            for i in range(nRandom):
                #ADICIONAR DESPESA TESTE
                data = F'1/{m}/2020'
                self.insertGastos(data, 'TESTE', randint(20,200))
    
    def testeReceita(self):

        #INSERIR DESVICEOS NVZS NOS 12 MESES
        for m in range(1, 13):

            nRandom = randint(10, 50)
            print(nRandom)
            
            #ITERAR NVZS
            for i in range(10):

                #ADICIONAR SERVICO TESTE
                data = F'1/{m}/2020'

                #m, data, hora, servico, nomeCliente, valor, valorManutencao
                self.insertService(m, data, '7:00', 'TESTE', 'TESTE', randint(20,200), 10)

a = bd()
#a.testeReceita()
#a.dropAllTables()
#a.testeReceita()
#a.testGastos()
#print(a.getDespesasAllMonths('2020'))
#a.insertGastos('20/12/2020', 'ESMALTE', 50)
#a.dropService(10, '15/10/2020', 'AMELIA', '7:00', 'UNHAS PÉ E MÃO')
#a.editService()
#print(a.getReceitaAllMonths(2020))
#a.getReceitaAllMonths(2020)
#a.getDataNegocio()
#a.insertGastos('esmaltes', 16.50)
#a.createTablesGastos()
#for i in a.months:
#    a.createTablesMonths(i)
#a.insertService(10, '15/10/2020', '10:00', 'UNHA', 'Igor Santos', 20, 5)
#a.insertService(10, '15/10/2020', '13:00', 'ALONGAMENTO DA UNHA', 'ELLEN ALTA', 40, 5)
#a.insertService(10, '13/10/2020', '13:00', 'ALONGAMENTO DA UNHA', 'ELLEN ALTA', 40, 5)
#print(a.getService(15, 10, 2020))
#print(a.verifyServiceDate(20, 10, 2020))