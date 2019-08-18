from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fonte = ("Comic Sans MS", "10", "bold")

        self.primeiroContainer = Frame(master)
        self.primeiroContainer["padx"] = 10
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
  
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
  
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer["pady"] = 10
        self.terceiroContainer.pack()       
     
  
        self.titulo = Label(self.primeiroContainer, text="Calculadora de Soma")
        self.titulo["font"] = ("Arial", "14", "bold")
        self.titulo.pack()     

        self.n1 = Entry(self.segundoContainer)
        self.n1["width"] = 5
        self.n1["font"] = self.fonte
        self.n1.pack(side=LEFT)
        
        self.sinalLabel = Label(self.segundoContainer, text="+", font=self.fonte)
        self.sinalLabel.pack(side=LEFT)

        self.n2 = Entry(self.segundoContainer)
        self.n2["width"] = 5
        self.n2["font"] = self.fonte
        self.n2.pack(side=LEFT)
         

        self.msgResultado = Label(self.terceiroContainer, text="Resultado:", font=self.fonte)
        self.msgResultado.pack()

        self.resultado = Button(self.terceiroContainer)
        self.resultado["text"] = "Calcular"
        self.resultado["font"] = ("Arial", "11")
        self.resultado["width"] = 12
        self.resultado["command"] = self.exibirResultado
        self.resultado.pack()
  

    def exibirResultado(self):
    	try:
	    	resultado = float(self.n1.get())+float(self.n2.get())
	    	self.msgResultado["text"] = "Resultado: "+str(resultado)
    	except:
	    	self.msgResultado["text"] = "Entrada inválida!"
  
root = Tk()
root.title("Calculadora de Soma")
# root.attributes('-topmost', True)
# root.update()
# root.attributes('-topmost', False)
Application(root)
root.mainloop()