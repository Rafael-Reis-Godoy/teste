from tkinter import *

janela = Tk()
janela.title('rafa')
janela.geometry("500x250")
janela['bg'] ="blue"

def mensagem ():
    print('Mensagem')
popup_label = Label(janela, text="Este é um pop-up!")
popup_label.pack()


btn=Button(janela,text='Executar', command=mensagem)
btn.pack()
janela.mainloop()
print = "rafa"
