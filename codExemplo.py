import calendar
from tkinter import *

"""gui = Tk()
gui.title("Calendar")
"""
def daysMonth(d, m, y):

    #CRIA O CALENDARIO
    cal_x = calendar.month(int(y),int(m),w = 2, l = 1)
    print(cal_x)

    #TRANSFORMA EM LISTA E DESCARTA OS 9 PRIMEIROS
    l = cal_x.split()[9:]
    
    #RETORNA SE O MES TEM DETERIMANDO DIA
    return str(d) in l

print(daysMonth(31, 10, 2020))

    #cal_out = Label(gui, text=cal_x, font=("courier", 20, "bold"), bg="lightblue")
    #cal_out.pack(padx=3, pady=10)

"""label1 = Label(gui, text="Year:")
label1.pack()

e1 = Entry(gui)
e1.pack()

label2 = Label(gui, text="Month:")
label2.pack()

e2 = Entry(gui)
e2.pack()

button = Button(gui, text="Show",command=cal)
button.pack()

gui.mainloop()"""