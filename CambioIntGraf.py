from tkinter import *
from tkinter import messagebox

interfaz = Tk()

def cambio():
    precioAux = precio.get()
    pagoAux = pago.get()
    cambioAux = pagoAux-precioAux
    fatlanteAux = precioAux-pagoAux

    if(cambioAux<0):
        messagebox.showinfo(title = "FALTA DINERO EN PAGO", message="Falta dinero en el pago. El monto faltante es: " + str(fatlanteAux))
    elif (cambioAux == 0 ):
        messagebox.showinfo(title = "PAGO EXISTOSO", message="El pago ha sido exacto. No es necesario dar cambio. ")
    elif (cambioAux>0):
        messagebox.showinfo(title = "CAMBIO", message="El cambio a dar es de: " + str(cambioAux))

interfaz.geometry("500x300+100+100")
interfaz.title("Cambio de una compra")
lblTitle = Label(text="*** ¿CUÁNTO CAMBIO DAR EN UNA COMPRA? ***", font=("AR CENA", 14)).pack()

lblIngrese = Label (text="Ingrese el precio del artículo: ", font=("Agency FB", 14)).place(x=10, y=40)
precio = DoubleVar()
txtIngrese = Entry(interfaz, textvariable=precio).place(x=270, y=48)

lblpago = Label(text="¿Cuánto ha pagado el cliente? ", font=("Agency FB", 14)).place(x=10, y=70)
pago=DoubleVar()
textPago = Entry(interfaz, textvariable=pago).place(x=270, y=78)

btnResultado = Button(interfaz, text="Calcular Cambio", command=cambio, font=("Agency FB", 14)).place(x=10, y=110)


interfaz.mainloop()




















