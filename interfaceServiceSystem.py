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
        self.tuplaServices = (  'MANICURE',
                                'PEDICURE',
                                'MANICURE + PEDICURE',
                                'ESMALTAÇÃO',
                                'DESIGN SOBRAN.',
                                'DESIGN SOBRAN. + HENA',
                                'HENA',
                                'PACOTE MENSAL 1',
                                'PACOTE MENSAL 2',
                                'PACOTE MENSAL 3',
                                'PACOTE MENSAL 4',
                            )

        #DIAS DA SEMANA
        self.dias = [
                'Segunda-feira',
                'Terça-feira',
                'Quarta-feira',
                'Quinta-Feira',
                'Sexta-feira',
                'Sábado',
                'Domingo'
                ]

        #LISTA DE LABELS DOS DIAS DA SEMANA
        self.listOfDays = []

        self.windowService()
    
    def setDaysOfWeek(self):

        #VARRE OS 7 PRIMEIROS DIAS
        for i in range(1, 8):
            #ALINHA OS DIAS
            data = date(year=self.currentYear, month=self.currentMonth, day=i)
            d = self.dias[data.weekday()]

            self.listOfDays[i-1]['text'] = d[:3]

    def setDaysOfWeekInCalendar(self):

        posX = 80

        for i in range(8):
            
            #CRIAR LABELS DE DIAS DA SEMANA
            lblDiaSemana = Label(self.windowMain, text='', font=self.fontDefault, bg=self.colorBackground, fg='black')
            lblDiaSemana.place(x=posX, y=130)

            posX += 80

            #ADICIONA EM UMA LISTA PARA SER ATUALIZADA
            self.listOfDays.append(lblDiaSemana)

    def windowService(self):

        self.windowMain = Tk()
        self.windowMain.geometry('680x480+10+10')
        self.windowMain.resizable(False, False)
        self.windowMain.title('SERVICE SYSTEM')
        self.windowMain['bg'] = self.colorBackground

        #SETAR O MES 
        self.setTitleMonth()

        #SETAR RANGE DE DIAS DA SEMANA
        self.setDaysOfWeekInCalendar()

        #SETAR DIAS ATUAIS
        self.setDaysOfWeek()

        #SETAR BOTOES
        self.createRangeButtons()

        #BOTOES PARA ALTERAR OS MESES
        self.changeMonths()

        #TECLAS DE FUNCOES
        self.windowMain.bind("<F1>", self.keyPressed)
        self.windowMain.bind("<F2>", self.keyPressed)
        self.windowMain.bind("<F3>", self.keyPressed)
        self.windowMain.bind("<F4>", self.keyPressed)
        self.windowMain.bind("<F5>", self.keyPressed)
        self.windowMain.bind("<F6>", self.keyPressed)

        self.windowMain.mainloop()

    def keyPressed(self, event):
        l = event.keysym

        #PRESSIONAR F2
        if l == 'F1':
            #TELA DE AJUDA
            self.helpKeys()

        elif l == 'F2':
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
        
        elif l == 'F6':
            self.plotGraphAllMonths()

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

        comboValor['values'] = (9, 10, 15, 20, 24, 25)
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
            id = elements[0]
            cliente = elements[4]
            hora    = elements[2]
            servico = elements[3]

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
            self.showServices(id, day, cliente, posXCliente, posYCliente, hora, posXHora, posYHora, servico, posXServico, posYServico, '', posXEdit, posYEdit)

        self.windowDay.mainloop()

    def showServices(self, id, day, nomeCliente, posXCliente, posYCliente, hora, posXHora, posYHora, servico, posXServico, posYServico, edit, posXEdit, posYEdit):
        
        #CRIAR O SERVIÇO
        #lblNomeCliente = Label(self.windowDay, text=nomeCliente, height=5, width=30, font=self.fontDefault, bg='white')
        #lblNomeCliente.place(x=posXCliente, y=posYCliente)

        #CRIAR O BOTAO DE EDICAO E NOME DO CLINETE
        btEdit = Button(self.windowDay, text=nomeCliente, bg=self.colorNameMonth, height=4, width=28, font=self.fontDefault, command=lambda : self.editService(id, day, nomeCliente, hora, servico, edit))
        btEdit.place(x=posXCliente, y=posYCliente)

        #HORA DO SERVICO
        lblHora = Label(self.windowDay, text=hora, bg=self.colorNameMonth, font=self.fontDefault)
        lblHora.place(x=posXHora, y=posYHora)

        #NOME DO SERVICO
        lblServico = Label(self.windowDay, text=servico, bg=self.colorNameMonth, font=self.fontDefault)
        lblServico.place(x=posXServico, y=posYServico)

    def editService(self, id, day, nomeCliente, hora, servico, edit):
        
        print(id, self.currentMonth, self.currentYear)

        self.windowEditService = Tk()
        self.windowEditService.geometry('290x245+10+10')
        self.windowEditService.resizable(False, False)
        self.windowEditService.title('EDIT SERVICES')
        self.windowEditService['bg'] = self.colorBackground

        #LISTA DE POSICOES
        positionsX = [i for i in range(10, 600, 140)]
        positionsY = [i for i in range(10, 500, 80)]

        #JANELA DE EDICAO
        def editData(tipo):
            windowMainEdit = Tk()
            windowMainEdit.geometry('450x170+10+10')
            windowMainEdit.resizable(False, False)
            windowMainEdit.title('EDIT SERVICES')
            windowMainEdit['bg'] = self.colorBackground

            def destroyWindows():
                #FECHAR JANELA ATUAL
                windowMainEdit.destroy()

                #FECHAR JANELA DE OPÇOES DE EDICAO
                self.windowEditService.destroy()

            #SALVAR ALTERAÇÕES NO BANCO DE DADOS
            def save():
                data = f'{day}/{self.currentMonth}/{self.currentYear}'

                if tipo == 'Data':
                    #NOVA DATA ATUALIZANDO APENAS O DIA
                    newData = f'{comboData.get()}/{self.currentMonth}/{self.currentYear}'
                    newHora = comboHora.get()

                    #EDITA O DIA DA DATA
                    self.bancoDados.editService(id, self.currentMonth, 'data', newData)

                    #EDITA O HORARIO
                    self.bancoDados.editService(id, self.currentMonth, 'hora', newHora)

                elif tipo == 'Serv':
                    #NOVO SERVICO
                    newServ = comboServico.get()

                    #EDITA O SERVICO
                    self.bancoDados.editService(id, self.currentMonth, 'servico', newServ)

                elif tipo == 'Val':
                    #NOVO VALOR
                    newVal = comboValor.get()

                    #EDITA O SERVICO
                    self.bancoDados.editService(id, self.currentMonth, 'valor', newVal)

                #FECHA TODAS AS WINDOWS
                destroyWindows()

            if tipo == 'Data':
                #Data
                lblData = Label(windowMainEdit, text='Data:', bg=self.colorBackground)
                lblData.place(x=10, y=20)

                comboData = ttk.Combobox(windowMainEdit, width = 8) 

                comboData['values'] = tuple(['{}'.format(i) for i in range(1, 32)])
                comboData.current(self.day-1)
                comboData.place(x=10, y=40)

                #Mes
                lblMes = Label(windowMainEdit, text='Mês:', bg=self.colorBackground)
                lblMes.place(x=130, y=20)

                comboMes = ttk.Combobox(windowMainEdit, width = 8) 

                comboMes['values'] = tuple(['{}'.format(i) for i in range(1, 13)])
                comboMes.current(self.month-1)
                comboMes.place(x=130, y=40)

                #Ano
                lblAno = Label(windowMainEdit, text='Ano:', bg=self.colorBackground)
                lblAno.place(x=250, y=20)

                comboAno = ttk.Combobox(windowMainEdit, width = 8) 

                comboAno['values'] = tuple(['{}'.format(i) for i in range(2020, 2051)])
                comboAno.current(0)
                comboAno.place(x=250, y=40)

                #Hora
                lblHora = Label(windowMainEdit, text='Hora:', bg=self.colorBackground)
                lblHora.place(x=10, y=80)

                comboHora = ttk.Combobox(windowMainEdit, width = 8) 

                comboHora['values'] = ('7:00', '8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00')
                comboHora.current(0)
                comboHora.place(x=10, y=100)

            elif tipo == 'Serv':
                #SERVICO
                lblServico = Label(windowMainEdit, text='Servico:', bg=self.colorBackground)
                lblServico.place(x=10, y=20)
                
                comboServico = ttk.Combobox(windowMainEdit, width = 23) 

                comboServico['values'] = self.tuplaServices
                comboServico.current(2)
                comboServico.place(x=10, y=40)

            elif tipo == 'Val':
                #VALOR
                lblValor = Label(windowMainEdit, text='Valor:', bg=self.colorBackground)
                lblValor.place(x=10, y=20)
                
                comboValor = ttk.Combobox(windowMainEdit, width = 8) 

                comboValor['values'] = (9, 10, 15, 20, 24, 25)
                comboValor.current(3)
                comboValor.place(x=10, y=40)

            #BOTAO DE SALVAR ALTERAÇÕES
            btSave = Button(windowMainEdit, text='Salvar', bg='MediumSpringGreen', command=save)
            btSave.place(x=360, y=130)

            windowMainEdit.mainloop()

        def deleteService():
            #PARAMETRO PARA EXCLUSÃO mes, data, nomeCliente, hora, servico
            data = f'{day}/{self.currentMonth}/{self.currentYear}'

            try:
                #DELETAR SERVICO DA BASE DE DADOS
                self.bancoDados.dropService(self.currentMonth, data, nomeCliente, hora, servico)
                messagebox.showinfo('', 'DELETADO COM SUCESSO !!')

            except:
                messagebox.showerror('', 'OCORREU UM ERRO !')

            #FECHAR JANELA DE SERVICOS DO DIA
            self.windowDay.destroy() 

            #FECHAR JANELA DE OPÇOES DE EDICAO
            self.windowEditService.destroy()

        #EDITAR O TEMPO
        btEditData = Button(self.windowEditService, text='Data', bg=self.colorNameMonth, font=self.fontDefault, width=10, height=3, command=lambda : editData('Data'))
        btEditData.place(x=positionsX[0], y=positionsY[0])

        btEditServicoCliente = Button(self.windowEditService, text='Serviço', bg=self.colorNameMonth, font=self.fontDefault, width=10, height=3, command=lambda : editData('Serv'))
        btEditServicoCliente.place(x=positionsX[0], y=positionsY[1])

        btEditValores = Button(self.windowEditService, text='Valores', bg=self.colorNameMonth, font=self.fontDefault, width=10, height=3, command=lambda : editData('Val'))
        btEditValores.place(x=positionsX[0], y=positionsY[2])

        #BOTAO PARA EXCLUIR SERVICO
        btDelete = Button(self.windowEditService, text='DELETE', bg='red', fg='white', font=self.fontDefault, width=10, height=3, command=lambda : deleteService())
        btDelete.place(x=positionsX[1], y=positionsY[1])

        self.windowEditService.mainloop()    

    def refreshCalendar(self):

        #SETAR DIAS ATUAIS
        self.setDaysOfWeek()

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
        self.windowGastos.geometry('360x160+10+10')
        self.windowGastos.resizable(False, False)
        self.windowGastos.title('ADD NEW SPENDING')
        self.windowGastos['bg'] = self.colorBackground

        #Data
        lblData = Label(self.windowGastos, text='Data:', bg=self.colorBackground)
        lblData.place(x=10, y=20)

        comboData = ttk.Combobox(self.windowGastos, width=8) 

        comboData['values'] = tuple(['{}'.format(i) for i in range(1, 32)])
        comboData.current(self.day-1)
        comboData.place(x=10, y=40)

        #Mes
        lblMes = Label(self.windowGastos, text='Mês:', bg=self.colorBackground)
        lblMes.place(x=130, y=20)

        comboMes = ttk.Combobox(self.windowGastos, width=8) 

        comboMes['values'] = tuple(['{}'.format(i) for i in range(1, 13)])
        comboMes.current(self.month-1)
        comboMes.place(x=130, y=40)

        #Ano
        lblAno = Label(self.windowGastos, text='Ano:', bg=self.colorBackground)
        lblAno.place(x=250, y=20)

        comboAno = ttk.Combobox(self.windowGastos, width=8) 

        comboAno['values'] = tuple(['{}'.format(i) for i in range(2020, 2051)])
        comboAno.current(0)
        comboAno.place(x=250, y=40)

        #Itens
        lblItens = Label(self.windowGastos, text='Itens:', bg=self.colorBackground)
        lblItens.place(x=10, y=70)

        etItens = Entry(self.windowGastos, width=10)
        etItens.place(x=10, y=90)

        #Valor
        lblValor = Label(self.windowGastos, text='Valor R$:', bg=self.colorBackground)
        lblValor.place(x=130, y=70)

        etValor = Entry(self.windowGastos, width=10)
        etValor.place(x=130, y=90)

        def insertDataBase():
            
            try:
                data = F'{comboData.get()}/{comboMes.get()}/{comboAno.get()}'
                itens = etItens.get().upper()
                valor = float(etValor.get())

                #ADICIONAR GASTO NA BASE DE DADOS
                self.bancoDados.insertGastos(data, itens, valor)

                messagebox.showinfo('', 'GASTO ADICIONADO COM SUCESSO !')

                #LIMPAR CAMPOS
                etValor.delete(0, END)
                etItens.delete(0, END)

                #FOCAR NO CAMPO DE ITENS
                etItens.focus()

            except:
                messagebox.showerror('', 'OCORREU UM ERRO !')

        #CRIAR NOVO GASTO
        btCreate = Button(self.windowGastos, text='SALVAR', bg='MediumSpringGreen', command=insertDataBase)
        btCreate.place(x=250, y=120)

        self.windowGastos.mainloop()

    def plotGraphVisaoNegocio(self):
        
        dados = self.bancoDados.getDataNegocio()

        #ENVIAR AS INFORMAÇÕES PARA FORUMLAR O GRAFICO
        self.setGrafico.gerarGraficoFinanceiro(dados[0], dados[1], dados[2], dados[3])

    def plotGraphAllMonths(self):

        self.windowYear = Tk()
        self.windowYear.geometry('240x140+10+10')
        self.windowYear.resizable(False, False)
        self.windowYear.title('CREATE GRAPH RECEITA ALL MONTHS')
        self.windowYear['bg'] = self.colorBackground

        #Ano
        lblAno = Label(self.windowYear, text='Selecione o Ano:', bg=self.colorBackground)
        lblAno.place(x=10, y=20)

        comboAno = ttk.Combobox(self.windowYear, width = 8) 

        comboAno['values'] = tuple(['{}'.format(i) for i in range(2020, 2051)])
        comboAno.current(0)
        comboAno.place(x=10, y=40)

        def plotar():
            
            ano = comboAno.get()

            #RETORNA A LISTA DE RECEITAR
            listaReceitas = self.bancoDados.getReceitaAllMonths(ano)
            listaDespesas = self.bancoDados.getDespesasAllMonths(ano)

            #PLOTAR GRAFICO
            self.setGrafico.generateGraphYear(listaReceitas, listaDespesas)

        #BOTAO PARAR GERAR O GRAFICO
        btPlot = Button(self.windowYear, text='PLOTAR GRAFICO', bg='MediumSpringGreen', command=plotar)
        btPlot.place(x=10, y=80)

        self.windowYear.mainloop()

    def helpKeys(self):

        #LISTA DE AJUDA
        ajuda = [
                    'F2 - Cadastrar de Servico',
                    'F3 - Adicionar Novo Gasto',
                    'F4 - Plotar Grafico de Visao de Negócio',
                    'F5 - Atualizar Calendário',
                    'F6 - Plotar Grafico de Receitas dos 12 Meses',
                    'F7 - ',
                    'F8 - ',
                    'F9 - ',
        ]

        self.windowHelp = Tk()
        self.windowHelp.geometry('470x350+10+10')
        self.windowHelp.resizable(False, False)
        self.windowHelp.title('Help')
        self.windowHelp['bg'] = self.colorBackground

        lblAjuda = Label(self.windowHelp, text='HELP', font=self.fontDefault, fg='Tomato', bg=self.colorBackground)
        lblAjuda.pack(pady=10)

        posX = 10
        posY = 50

        #ADICIONAR LISTA DE AJUDA
        for i in ajuda:

            lbl = Label(self.windowHelp, text=i, font=self.fontDefault, bg=self.colorBackground)
            lbl.place(x=posX, y=posY)

            posY += 30

        self.windowHelp.mainloop()

if __name__ == "__main__":
    serviceSystem()    
