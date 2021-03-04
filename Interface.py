from tkinter import *

root = Tk()

class Interface():
    def __init__(self):
        self.root = root
        self.tela()
        self.buttons()
        self.titulo()
        self.informations()
        self.services()
        self.options()
        self.button_Cadastrar()
        self.button_VisEstoque()
        self.button_LensZero()
        self.button_Retirar()
        self.button_RegSaida()
        self.button_Sair()
        self.entry_Login()
        self.entry_Senha()
        root.mainloop()

    # FRAMES
    def tela(self):  # caracteristicas da tela
        self.root.title("Gerenciamento Laboratório Carol")
        self.root.geometry("1000x700")
        self.root.resizable(True, True)
        self.root.minsize(width= 800, height= 500)
        self.root.configure(background="#0000cd")

    def titulo(self):  # frame do título e algumas informções não excenciais
        self.frame_titulo = Frame(self.root, bd=-4, bg="#ffd700", highlightbackground= "#1c1c1c",
        highlightthickness= 2)
        self.frame_titulo.place(relx=0.13, rely=0.02, relwidth=0.45, relheight=0.15)

    def buttons(self):  # frame dos botões
        self.frame_buttons = Frame(self.root, bd=-4, bg="#ffd700", highlightbackground= "#1c1c1c",
        highlightthickness= 2)
        self.frame_buttons.place(relx=0.01, rely=0.02, relwidth=0.11, relheight=0.96)

    def informations(self):  # frame das informações
        self.frame_informations = Frame(self.root, bd=-4, bg="#ffd700", highlightbackground= "#1c1c1c",
        highlightthickness= 2)
        self.frame_informations.place(relx=0.13, rely=0.19, relwidth=0.45, relheight=0.79)

    def services(self):
        self.frame_services = Frame(self.root, bd=-4, bg="#ffd700", highlightbackground= "#1c1c1c",
        highlightthickness= 2)
        self.frame_services.place(relx=0.59, rely=0.02, relwidth= 0.40, relheight= 0.96)

    def options(self):
        self.frame_options = Frame(self.root, bd=-4, bg="#f0e68c", highlightbackground= "#1c1c1c",
        highlightthickness= 2)
        self.frame_options.place(relx=0.14, rely=0.21, relwidth=0.43, relheight=0.30)

    # OPÇOES DE CADASTRO DE LENTES
    def option_RegisterLens(self):
        from tkinter import messagebox
        self.fontepadrao = ("Verdana", 10, "italic", 'bold')
        self.radiobutton_1 = Radiobutton(self.frame_options, text="Código de barras", font=self.fontepadrao, bg="#f0e68c")
        self.radiobutton_2 = Radiobutton(self.frame_options, text="Dioptria", font=self.fontepadrao, bg="#f0e68c")
        self.radiobutton_1.place(relx=0.04, rely=0.05, relwidth=0.44, relheight=0.15)
        self.radiobutton_2.place(relx=0.035, rely=0.30, relwidth=0.34, relheight=0.15)
        
    # BOTÕES
    def button_Cadastrar(self):
        self.CadastrarLente = Button(self.frame_buttons, text="Cadastrar", command=self.option_RegisterLens,
         bd=2, bg="#c0c0c0", fg="black")
        self.CadastrarLente["font"] = ("Verdana", 10, "italic", "bold")
        self.CadastrarLente.place(relx=0.05 , rely=0.02, relwidth=0.90, relheight=0.05)

        # colocar algumas opções de cadastro de lentes
    # OPÇÕES DE VISUALIZAÇÃO DO ESTOQUE
    def exibirOpcoes(self):
        self.label1 = Frame(self.frame_options, bd=-4, bg="#f0e68c", highlightbackground= "#1c1c1c",
        highlightthickness= 2)
        self.label2 = Label(self.frame_options, text="TESTANDO", bg="#f0e68c", font=self.fontepadrao)
        self.label1.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.label2.place(relx=0.04, rely=0.05, relwidth=0.44, relheight=0.15)

    def button_VisEstoque(self):
        self.VisEstoque = Button(self.frame_buttons, text="Vis. Estoque", bd=2, bg="#c0c0c0", fg="black",
        command= self.exibirOpcoes)
        self.VisEstoque["font"] = ("Verdana", 10, "italic", "bold")
        self.VisEstoque.place(relx=0.05 , rely=0.08, relwidth=0.90, relheight=0.05)

    def button_LensZero(self):
        self.LensZero = Button(self.frame_buttons, text="Lentes\nem\nFalta", bd=2, bg="#c0c0c0", fg="black")
        self.LensZero["font"] = ("Verdana", 10, "italic", "bold")
        self.LensZero.place(relx=0.05, rely=0.14, relwidth=0.90, relheight=0.10)

    def button_Retirar(self):
        self.Retirar = Button(self.frame_buttons, text="Retirar", bd=2, bg="#c0c0c0", fg="black")
        self.Retirar["font"] = ("Verdana", 10, "italic", "bold")
        self.Retirar.place(relx=0.05, rely=0.25, relwidth=0.90, relheight=0.05)

    def button_RegSaida(self):
        self.RegSaida = Button(self.frame_buttons, text="Registro\nde\nSaída", bg="#c0c0c0", fg="black")
        self.RegSaida["font"] = ("Verdana", 10, "italic", "bold")
        self.RegSaida.place(relx=0.05, rely=0.31, relwidth=0.90, relheight=0.10)
        
    def button_Sair(self):
        self.Sair = Button(self.frame_buttons, text="Sair", bg="#c0c0c0", fg="black")
        self.Sair["font"] = ("Verdana", 10, "italic", "bold")
        self.Sair["command"] = quit
        self.Sair.place(relx=0.05, rely=0.93, relwidth=0.90, relheight=0.05)

    # ENTRADA DE DADOS NA LABEL DO TITULO E INFORMAÇÕES

    def entry_Login(self):
        self.labelLogin = Label(self.frame_titulo, text="Usuário", bg="#ffd700")
        self.labelLogin["font"] = ("Verdana", 10, "italic", "bold")
        self.labelLogin.place(relx=0.02, rely=0.20, relwidth=0.15, relheight=0.20)

        self.Login = Entry(self.frame_titulo)
        self.Login["font"] = ("Verdana", 10, "italic")
        self.Login.place(relx=0.18, rely=0.20, relwidth=0.35, relheight=0.20)

    def entry_Senha(self):
        self.labelSenha = Label(self.frame_titulo, text="Senha", bg="#ffd700")
        self.labelSenha["font"] = ("Verdana", 10, "italic", "bold")
        self.labelSenha.place(relx=0.02, rely=0.60, relwidth=0.15, relheight=0.20)

        self.Senha = Entry(self.frame_titulo)
        self.Senha["font"] = ("Verdana", 10, "italic")
        self.Senha["show"] = "*"
        self.Senha.place(relx=0.18, rely=0.60, relwidth=0.35, relheight=0.20)


Interface()  # chamando a classe para iniciar

# sistema desencolvido por Matheus Brodt no ano de 2021 para fins de estudo e de uso próprio...