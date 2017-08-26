from tkinter import*



root = Tk()
root.geometry("1000x500+0+0")
root.title("dojo python")

text_input = StringVar()
operador =""

Tops= Frame(root, width =1600, height =80 ,bg= "powder blue",relief=SUNKEN)
Tops.pack(side = TOP)

Frame=Frame(root, width =300, height =700 ,bg= "powder blue",relief=SUNKEN)                           
Frame.pack(side = TOP)

info = Label(Tops, font=("SHOWCARD GOTHIC", 50, "bold"), text ="dojo python")
info.grid(row=0, column=0)

def btonClick(numero):
	global operador
	operador=operador + str(numero)
	text_input.set(operador)

def btonEval(numero):
	global operador
	result =str(eval (operador))
	text_input.set(result)
	operador=""

txtDisplay = Entry (Frame,font =("SHOWCARD GOTHIC", 50, "bold"), textvariable=text_input bg="black")
txtDisplay.grid(columnspan=4)


boton_1 =Button (frame, font =("SHOWCARD GOTHIC", 50, "bold"), command=lamdba.btonClick(1).grid)(row=2 column=0)
boton_1 =Button (frame, font =("SHOWCARD GOTHIC", 50, "bold"), command=lamdba.btonClick(2).grid)(row=2 column=1)

boton_suma =Button (frame, font =("SHOWCARD GOTHIC", 50, "bold"), command=lamdba.btonClick("+").grid)(row=2 column=2)
boton_igual =Button (frame, font =("SHOWCARD GOTHIC", 50, "bold"), command=.btonEval(2).grid)(row=2 column=1)


root.mainloop()
