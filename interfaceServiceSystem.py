from tkinter import *
from serviceSystem import bd
from datetime import date
import calendar

class serviceSystem:

    def __init__(self):
        #OBJETO DE BANCO DE DADOS
        self.bancoDados = bd()

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

        self.windowMain.mainloop()

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
        btRight.place(x=620, y=430)

        #VOLTAR UM MES
        btLeft = Button(self.windowMain, text='<', width=2, height=1, bg=self.colorNameMonth, fg='white', font=self.fontDefault, command=lambda: prevMonth())
        btLeft.place(x=575, y=430)
    
    def daysMonth(self, d, m, y):
        
        print(m)

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

if __name__ == "__main__":
    serviceSystem()    
