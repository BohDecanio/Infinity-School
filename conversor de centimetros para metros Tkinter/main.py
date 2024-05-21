from tkinter import*  

root = Tk() #criar objeto do tipo janela - normalmente chamado de raiz/root
root.geometry('600x250') #tamanho da janela

varValor1 = StringVar()   #Variável alimentada pelo usuário
varResultado = StringVar() #Variável que apresentará resultado da conversão

def btnConverteOnClick():
    valor_digitado = varValor1.get() #aqui verifica se a variável recebeu um valor antes de tentar converter.
    if valor_digitado:
        varResultado.set(float(valor_digitado) / 100)
    else:
        varResultado.set("")

lblTitulo = Label(root, text='Conversão de centímetros para metros ', font=('Arial',18))
lblTitulo.pack() #faz o rotulo aparecer em pack , empilhado

lblValor1 = Label(root, text= 'Digite valor em centímetros: ', font=('Arial',11))
lblValor1.pack()  
txtValor1 = Entry(root, textvariable=varValor1)  
txtValor1.pack()  

btnConverte = Button(root, text='converter', command=btnConverteOnClick)
btnConverte.pack()

lblResultado = Label(root, text='O valor em metros é: ', font=('Arial',12))
lblResultado.pack()
txtResultado = Label(root, textvariable=varResultado)
txtResultado.pack()

root.mainloop()