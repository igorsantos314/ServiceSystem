from tkinter import *
from serviceSystem import bd
from datetime import date
import calendar
from tkinter import ttk
from tkinter import messagebox
from plotGraphs import plotGraphs

class serviceSystem(Frame):

    def __init__(self):
        #OBJETO DE BANCO DE DADOS
        self.bancoDados = bd()

        #OBEJTO DE CRIAÇÃO DE GRAFICOS
        self.setGrafico = plotGraphs()

        #BOTOES COM OS DATAS DE CADA MES
        self.buttonsDays = []

        #DATA ATUAL
        self.day = date.today().day
        self.month = date.today().month
        self.year = date.today().year

        #DEFAULTS
        self.fontStyleUpper = 'Courier 30 bold'
        self.colorNameMonth = 'Tomato'
        self.colorBackground = 'PaleGoldenrod'
        self.colorButtons = 'PowderBlue'
        self.fontDefault = 'Courier 12 bold'

        #POSITIONS DOS SERVIÇOS DO DIA
        self.dictPositionsServices = {
                                        0:(20, 20, 25, 85, 25, 25, 295, 20),
                                        1:(340, 20, 345, 85, 345, 25, 615, 20),
                                        2:(660, 20, 665, 85, 665, 25, 935, 20),
                                        3:(20, 120, 25, 185, 25, 125, 295, 120),
                                        4:(340, 120, 345, 185, 345, 125, 615, 120),
                                        5:(660, 120, 665, 185, 665, 125, 935, 120),
                                        6:(20, 220, 25, 285, 25, 225, 295, 220),
                                        7:(340, 220, 345, 285, 345, 225, 615, 220),
                                        8:(660, 220, 665, 285, 665, 225, 935, 220),
                                        9:(20, 320, 25, 385, 25, 325, 295, 320),
                                        10:(340, 320, 345, 385, 345, 325, 615, 320),
                                        11:(660, 320, 665, 385, 665, 325, 935, 320) 
                                    }

        #MES CORRENTE PARA PESQUISAS
        self.currentMonth = self.month
        self.currentYear = date.today().year

        #TUPLA DE SERVICOS
        self.tuplaServices = (  'UNHAS MÃO',
                                'UNHAS PÉ',
                                'UNHAS PÉ E MÃO',
                                'UNHAS EM GEL',
                                'UNHAS ALONGAMENTO',
                                'SOBRANCELHA NORMAL',
                                'SOBRANCELHA NA RENA'
                            )

        self.windowService()
    
    def windowService(self):

        self.windowMain = Tk()
        self.windowMain.geometry('680x480+10+10')
        self.windowMain.resizable(False, False)
        self.windowMain.title('SERVICE SYSTEM')
        self.windowMain['bg'] = self.colorBackground

        #SETAR O MES 
        self.setTitleMonth()

        #SETAR BOTOES
        self.createRangeButtons()

        #BOTOES PARA ALTERAR OS MESES
        self.changeMonths()

        #PRESSIONAR F2 PARA CRIAR POST IT
        self.windowMain.bind("<F2>", self.keyPressed)
        self.windowMain.bind("<F3>", self.keyPressed)
        self.windowMain.bind("<F4>", self.keyPressed)
        self.windowMain.bind("<F5>", self.keyPressed)

        self.windowMain.mainloop()

    def keyPressed(self, event):
        l = event.keysym

        #PRESSIONAR F2
        if l == 'F2':
            #CRIAR NOVO SERVICO
            self.AddNewServices()

        elif l == 'F3':
            #ADICIONAR CUSTO EM SERVIÇOS
            self.gastos()

        elif l == 'F4':
            #ADICIONAR CUSTO EM SERVIÇOS
            self.plotGraphVisaoNegocio()

        elif l == 'F5':
            #CASO O USUARIO PRESSIONE F5
            self.refreshCalendar()

    def AddNewServices(self):

        self.windowAddSerivice = Tk()
        self.windowAddSerivice.geometry('480x260+10+10')
        self.windowAddSerivice.resizable(False, False)
        self.windowAddSerivice.title('CREATE NEW SERVICE')
        self.windowAddSerivice['bg'] = self.colorBackground

        #Data
        lblData = Label(self.windowAddSerivice, text='Data:', bg=self.colorBackground)
        lblData.place(x=10, y=20)

        comboData = ttk.Combobox(self.windowAddSerivice, width = 8) 

        comboData['values'] = tuple(['{}'.format(i) for i in range(1, 32)])
        comboData.current(self.day-1)
        comboData.place(x=10, y=40)

        #Mes
        lblMes = Label(self.windowAddSerivice, text='Mês:', bg=self.colorBackground)
        lblMes.place(x=130, y=20)

        comboMes = ttk.Combobox(self.windowAddSerivice, width = 8) 

        comboMes['values'] = tuple(['{}'.format(i) for i in range(1, 13)])
        comboMes.current(self.month-1)
        comboMes.place(x=130, y=40)

        #Ano
        lblAno = Label(self.windowAddSerivice, text='Ano:', bg=self.colorBackground)
        lblAno.place(x=250, y=20)

        comboAno = ttk.Combobox(self.windowAddSerivice, width = 8) 

        comboAno['values'] = tuple(['{}'.format(i) for i in range(2020, 2051)])
        comboAno.current(0)
        comboAno.place(x=250, y=40)
        
        #Hora
        lblHora = Label(self.windowAddSerivice, text='Hora:', bg=self.colorBackground)
        lblHora.place(x=370, y=20)

        comboHora = ttk.Combobox(self.windowAddSerivice, width = 8) 

        comboHora['values'] = ('7:00', '8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00')
        comboHora.current(0)
        comboHora.place(x=370, y=40)

        #SERVICO
        lblServico = Label(self.windowAddSerivice, text='Serviço:', bg=self.colorBackground)
        lblServico.place(x=10, y=80)
        
        comboServico = ttk.Combobox(self.windowAddSerivice, width = 23) 

        comboServico['values'] = self.tuplaServices
        comboServico.current(2)
        comboServico.place(x=10, y=100)

        #NOME DO CLIENTE
        lblNomeCliente = Label(self.windowAddSerivice, text='Nome do Cliente:', bg=self.colorBackground)
        lblNomeCliente.place(x=250, y=80)

        etNomeCliente = Entry(self.windowAddSerivice, width=24)
        etNomeCliente.place(x=250, y=100)

        #VALOR
        lblValor = Label(self.windowAddSerivice, text='Valor:', bg=self.colorBackground)
        lblValor.place(x=10, y=140)
        
        comboValor = ttk.Combobox(self.windowAddSerivice, width = 8) 

        comboValor['values'] = tuple([i for i in range(5, 60, 5)])
        comboValor.current(3)
        comboValor.place(x=10, y=160)

        #PORCENTAGEM PARA MANUTENÇÃO
        lblValorManutencao = Label(self.windowAddSerivice, text='Manutenção:', bg=self.colorBackground)
        lblValorManutencao.place(x=130, y=140)
        
        comboValorManutencao = ttk.Combobox(self.windowAddSerivice, width = 8) 

        comboValorManutencao['values'] = tuple(['{}%'.format(i) for i in range(10, 100, 10)])
        comboValorManutencao.current(2)
        comboValorManutencao.place(x=130, y=160)

        def insertDataBase():
            
            try:
                mes = int(comboMes.get())
                data = '{}/{}/{}'.format(comboData.get(), mes, comboAno.get())
                hora = comboHora.get()
                servico = comboServico.get()
                cliente = etNomeCliente.get().upper()
                valor = float(comboValor.get())

                #CALCULO DE PORCENTAGEM PARA VALOR DE MANUTENCAO
                porcentagem = int(comboValorManutencao.get().replace('%',''))
                manutencao = ( porcentagem / 100) * valor
                
                #INSERIR DADOS NO BANCO DE DADOS
                self.bancoDados.insertService(mes, data, hora, servico, cliente, valor, manutencao)

                #MENSAGEM DE SUCESSO
                messagebox.showinfo('','SERVIÇO ADICIONADO COM SUCESSO !')

                #LIMPAR NOME DO CLIENTE
                etNomeCliente.delete(0, END)
            
            except:
                messagebox.showerror('','OCORREU UM ERRO!')

        #CRIAR NOVO SERVICO
        btCreate = Button(self.windowAddSerivice, text='SALVAR', bg='MediumSpringGreen', command=insertDataBase)
        btCreate.place(x=370, y=200)

        self.windowAddSerivice.mainloop()

    def setTitleMonth(self):
        
        #DATA E ANO ATUAL
        data = '{} - {}'.format(self.bancoDados.months[self.currentMonth-1], self.currentYear)

        self.lblMonth = Label(self.windowMain, text=data, font=self.fontStyleUpper, bg=self.colorNameMonth, fg='white', width=24, height=2)
        self.lblMonth.pack(pady=30)

    def changeMonths(self):

        def nextMonth():
            
            #VERIFICA SE ESTA EM DEZEMBRO E AVANÇA UM ANO
            if self.currentMonth == 12:
                self.currentMonth = 1
                self.currentYear += 1
            
            else:
                self.currentMonth += 1
            
            #ATUALIZAR O CALENDARIO COM O MES CORRENTE
            self.refreshCalendar()

        def prevMonth():

            #VERIFICA SE ESTA EM JANEIRO E VOLTA UM ANO ATRAS
            if self.currentMonth == 1:
                self.currentMonth = 12
                self.currentYear -= 1
            
            else:
                self.currentMonth -= 1

            #ATUALIZAR O CALENDARIO COM O MES CORRENTE
            self.refreshCalendar()

        #ADIANTAR UM MES
        btRight = Button(self.windowMain, text='>', width=2, height=1, bg=self.colorNameMonth, fg='white', font=self.fontDefault, command=lambda: nextMonth())
        btRight.place(x=575, y=430)

        #VOLTAR UM MES
        btLeft = Button(self.windowMain, text='<', width=2, height=1, bg=self.colorNameMonth, fg='white', font=self.fontDefault, command=lambda: prevMonth())
        btLeft.place(x=530, y=430)
    
    def daysMonth(self, d, m, y):
        #CRIA O CALENDARIO
        cal_x = calendar.month(int(y),int(m),w = 2, l = 1)

        #RETORNA SE O MES TEM DETERIMANDO DIA
        return str(d) in cal_x.split()[9:]

    def createRangeButtons(self):

        #MATRIZ DE NUMEROS DO CALENDÁRIO
        matrizData = [  [d for d in range(1,30,7)],
                        [d for d in range(2,31,7)],
                        [d for d in range(3,32,7)],
                        [d for d in range(4,26,7)],
                        [d for d in range(5,28,7)],
                        [d for d in range(6,29,7)],
                        [d for d in range(7,29,7)]]

        constSpaceX = 80
        constSpaceY = 60

        posX = 60

        #VARRE AS COLUNAS
        for i in matrizData:
            listTemp = []
            posY = 150

            #VARRE AS LINHAS
            for j in i:
                
                #VERIFICA SE O DATA EXISTE NO MES
                if self.daysMonth(j, self.currentMonth, self.currentYear):
                    
                    #COR PADRAO DO BOTAO
                    backgroundButton = self.colorButtons

                    #INDICAR A DATA ATUAL
                    if j == int(self.day):
                        backgroundButton = 'Tomato'

                    #CASO EXISTA ALGUMA TAREFA MUDAR A COR DE FUNDO
                    elif self.bancoDados.verifyServiceDate(j, self.currentMonth, self.currentYear):
                        backgroundButton = 'MediumSpringGreen'

                    #CRIA O SERVICO NO QUADRO
                    btTemp = self.createButton(j, posX, posY, backgroundButton)

                    #ADICIONA BOTAO A LISTA
                    listTemp.append(btTemp)

                posY += constSpaceY

            posX += constSpaceX

            #ADICIONA BOTAO A MATRIZ
            self.buttonsDays.append(listTemp)

    def createButton(self, value, posX, posY, backgroundButton):

        #CRIAR OS BOTOES
        bt = Button(self.windowMain, text=value, width=5, height=2, bg=backgroundButton, command=lambda: self.windowServicesDay(value))
        bt.place(x=posX, y=posY)

        #RETORNA OS BOTOES PARA CRIAR
        return bt

    def windowServicesDay(self, day):

        self.windowDay = Tk()
        self.windowDay.geometry('980x440+10+10')
        self.windowDay.resizable(False, False)
        self.windowDay.title('SERVICES OF DAY')
        self.windowDay['bg'] = self.colorBackground

        #LISTA DE SERVICOS MARCADOS
        listServicos = self.bancoDados.getService(day, int(self.currentMonth), self.currentYear)

        for j, elements in enumerate(listServicos):
            
            #PEGA OS DADOS DOS ELEMENTOS EXIBIDOS
            cliente = elements[3]
            hora    = elements[1]
            servico = elements[2]

            #SETA AS POSICOES DE CADA SERVICO NO QUADRO
            posXCliente =   self.dictPositionsServices[j][0]
            posYCliente =   self.dictPositionsServices[j][1]
            posXHora =      self.dictPositionsServices[j][2]
            posYHora =      self.dictPositionsServices[j][3]
            posXServico =   self.dictPositionsServices[j][4]
            posYServico =   self.dictPositionsServices[j][5]
            posXEdit =      self.dictPositionsServices[j][6]
            posYEdit =      self.dictPositionsServices[j][7]

            #CRIA O SERVICO
            self.showServices(cliente, posXCliente, posYCliente, hora, posXHora, posYHora, servico, posXServico, posYServico, '', posXEdit, posYEdit)

        self.windowDay.mainloop()

    def showServices(self, nomeClinete, posXCliente, posYCliente, hora, posXHora, posYHora, servico, posXServico, posYServico, edit, posXEdit, posYEdit):
        
        #CRIAR O SERVIÇO
        lblNomeCliente = Label(self.windowDay, text=nomeClinete, height=5, width=30, font=self.fontDefault, bg='white')
        lblNomeCliente.place(x=posXCliente, y=posYCliente)

        lblHora = Label(self.windowDay, text=hora, bg='white', font=self.fontDefault)
        lblHora.place(x=posXHora, y=posYHora)

        lblServico = Label(self.windowDay, text=servico, bg='white', font=self.fontDefault)
        lblServico.place(x=posXServico, y=posYServico)

        #CRIAR O BOTAO DE EDICAO
        btEdit = Button(self.windowDay, bg=self.colorNameMonth, font=self.fontDefault)
        btEdit.place(x=posXEdit, y=posYEdit)

    def refreshCalendar(self):

        for lista in self.buttonsDays:

            for days in lista:
                #APAGA TODOS OS BOTOES
                days.destroy()

        #RECRIAR BOTOES COM O MES CORRENTE
        self.createRangeButtons()
        
        #ATUALIZA O NOME DO MÊS E O ANO ATUAL
        self.lblMonth['text'] = '{} - {}'.format(self.bancoDados.months[self.currentMonth-1], self.currentYear)

    def gastos(self):

        self.windowGastos = Tk()
        self.windowGastos.geometry('360x140+10+10')
        self.windowGastos.resizable(False, False)
        self.windowGastos.title('ADD NEW SPENDING')
        self.windowGastos['bg'] = self.colorBackground

        #Itens
        lblItens = Label(self.windowGastos, text='Itens:', bg=self.colorBackground)
        lblItens.place(x=10, y=20)

        etItens = Entry(self.windowGastos)
        etItens.place(x=10, y=40)

        #Valor
        lblValor = Label(self.windowGastos, text='Valor R$:', bg=self.colorBackground)
        lblValor.place(x=180, y=20)

        etValor = Entry(self.windowGastos)
        etValor.place(x=180, y=40)

        def insertDataBase():
            
            try:
                itens = etItens.get().upper()
                valor = float(etValor.get())

                #ADICIONAR GASTO NA BASE DE DADOS
                self.bancoDados.insertGastos(itens, valor)

                messagebox.showinfo('', 'GASTO ADICIONADO COM SUCESSO !')

                #LIMPAR CAMPOS
                etValor.delete(0, END)
                etItens.delete(0, END)

                etItens.focus()

            except:
                messagebox.showerror('', 'OCORREU UM ERRO !')

        #CRIAR NOVO GASTO
        btCreate = Button(self.windowGastos, text='SALVAR', bg='MediumSpringGreen', command=insertDataBase)
        btCreate.place(x=10, y=80)

        self.windowGastos.mainloop()

    def plotGraphVisaoNegocio(self):
        
        dados = self.bancoDados.getDataNegocio()

        #ENVIAR AS INFORMAÇÕES PARA FORUMLAR O GRAFICO
        self.setGrafico.gerarGraficoFinanceiro(dados[0], dados[1], dados[2], dados[3])

if __name__ == "__main__":
    serviceSystem()    
