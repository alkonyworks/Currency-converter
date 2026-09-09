from tkinter import *

def pounds_to_euros():
    txt_euros.delete(0,"end")
    pounds = txt_pounds.get()
    euros = float(pounds) * 1.16
    txt_euros.insert(END,f"€{euros:.2f}")
    
def pounds_to_dollars():
    txt_dollars.delete(0,"end")
    pounds = txt_pounds.get()
    dollars = float(pounds) * 1.35
    txt_dollars.insert(END,f"${dollars:.2f}")
    
def pounds_convert():
    pounds_to_euros()
    pounds_to_dollars()
    
window = Tk()
window.geometry("700x500")

LBL_pounds = Label(window, text="Pounds")
LBL_pounds.pack()

txt_pounds = Entry(window, width = 15)
txt_pounds.pack()

btn_convert = Button(window, text="Convert", command = pounds_convert)
btn_convert.pack(pady = 15)

LBL_euros = Label(window, text="Euros")
LBL_euros.pack()

txt_euros = Entry(window,width = 15)
txt_euros.pack()

LBL_dollars = Label(window, text="Dollars")
LBL_dollars.pack(pady = 10)

txt_dollars = Entry(window,width = 15)
txt_dollars.pack()

window.mainloop()
