import calendar
from tkinter import *

"""gui = Tk()
gui.title("Calendar")
"""
def cal():
    y = 2020
    m = 11
    cal_x = calendar.month(int(y),int(m),w = 2, l = 1)
    print(cal_x)
    print(cal_x.split())

cal()

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