from tkinter import *
from serviceSystem import bd
from datetime import date

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

        self.windowMain.mainloop()

    def setTitleMonth(self):

        self.lblMonth = Label(self.windowMain, text=self.bancoDados.months[self.month], font=self.fontStyleUpper, bg=self.colorNameMonth, fg='white', width=40, height=2)
        self.lblMonth.pack(pady=30)

    def createRangeButtons(self):

        constSpaceX = 80
        constSpaceY = 60

        posX = 60

        matrizData = [  [d for d in range(1,30,7)],
                        [d for d in range(2,31,7)],
                        [d for d in range(3,32,7)],
                        [d for d in range(4,26,7)],
                        [d for d in range(5,28,7)],
                        [d for d in range(6,29,7)],
                        [d for d in range(7,29,7)]]

        #VARRE AS COLUNAS
        for i in matrizData:
            listTemp = []
            posY = 150

            #VARRE AS LINHAS
            for j in i:
                btTemp = self.createButton(j, posX, posY)
                listTemp.append(btTemp)

                posY += constSpaceY

            posX += constSpaceX
            self.buttonsDays.append(listTemp)

    def createButton(self, value, posX, posY):

        #CRIAR OS BOTOES
        bt = Button(self.windowMain, text=value, width=5, height=2, bg=self.colorButtons)
        bt.place(x=posX, y=posY)

        #RETORNA OS BOTOES PARA CRIAR
        return bt

if __name__ == "__main__":
    serviceSystem()    
