from tkinter import *
from tkinter import ttk

root = Tk()
class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.criando_frames_da_tela()
        self.widgets_frame_1()
        root.mainloop() #abrir a janela  principal do programa
    
    def tela(self): #função para configuração da tela
        self.root.title('Cadastro de clientes')
        self.root.configure(background='#19334d') # cor da fundo da tela
        self.root.geometry('700x500')#largura x altura da janela
        self.root.resizable(True, True)#permite redimensionar a janela(Responsivo == True (ativado) or False(desativado))
        self.root.maxsize(width=900, height=700) # definir o maximo de largura e altura que a janela pode ter
        self.root.minsize(width=400, height=300) # definir o minimo de largura e altura que a janela pode ser reduzida
    
    def criando_frames_da_tela(self):
        self.frame_1 = Frame(self.root, border=4, background='#d9e6f2', highlightbackground='#538cc6', highlightthickness=3).place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.45) #relx e rely posição inicial do frame (x= esquerda e y= direita)
        self.frame_2 = Frame(self.root, bd=4, bg='#d9e6f2', highlightbackground='#538cc6', highlightthickness=3).place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.45)
        #Frame()
        
    def widgets_frame_1(self):
        self.btn_limpar = Button(self.frame_1, text='Limpar', 
                                bd=3,bg='#19334d', fg='#fff', font=('verdana', 8, 'bold')).place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.05)
        self.btn_buscar = Button(self.frame_1, text='Buscar',
                                bd=3, bg='#19334d', fg='#fff', font=('verdana', 8, 'bold')).place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.05)
        self.btn_novo = Button(self.frame_1, text='Novo',
                                bd=3,bg='#19334d', fg='#fff', font=('verdana', 8, 'bold')).place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.05)
        self.btn_alterar = Button(self.frame_1, text='Alterar',
                                bd=3,bg='#19334d', fg='#fff', font=('verdana', 8, 'bold')).place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.05)
        self.btn_apagar = Button(self.frame_1, text='Apagar',
                                bd=3,bg='#19334d', fg='#fff', font=('verdana', 8, 'bold')).place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.05)
        
        #criando a Label e entrada do codigo
        self.lb_codigo = Label(self.frame_1, text='Código', 
                                bg='#d9e6f2', fg='#19334d', font=('verdana', 10, 'bold')).place(relx=0.05, rely=0.05)
        self.codigo_entrada = Entry(self.frame_1).place(relx=0.05, rely=0.11, relwidth=0.09)
        
        #criando a Label e entrada do nome
        self.lb_nome = Label(self.frame_1, text='Nome',
                            bg='#d9e6f2', fg='#19334d', font=('verdana', 10, 'bold')).place(relx=0.05, rely=0.2)
        self.codigo_entrada = Entry(self.frame_1).place(relx=0.05, rely=0.25, relwidth=0.5)
        
        #criando a Label e entrada do telefone
        self.lb_nome = Label(self.frame_1, text='Telefone',
                            bg='#d9e6f2', fg='#19334d', font=('verdana', 10, 'bold')).place(relx=0.05, rely=0.32)
        self.codigo_entrada = Entry(self.frame_1).place(relx=0.05, rely=0.37, relwidth=0.3)
        
        #criando a Label e entrada da cidade
        self.lb_nome = Label(self.frame_1, text='Cidade',
                            bg='#d9e6f2', fg='#19334d', font=('verdana', 10, 'bold')).place(relx=0.5, rely=0.32)
        self.codigo_entrada = Entry(self.frame_1).place(relx=0.5, rely=0.37, relwidth=0.3)
Application()