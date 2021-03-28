from tkinter import *
import mysql.connector
print('\033[31mRODANDO O PROGRAMA!\033[m')

root = Tk()


### BACKEND ###
class Funcs():
    def connect_BD(self):
        try:
            self.conn = mysql.connector.connect(host='localhost', user='root', password='', database="lab_carol")
            self.cursor = self.conn.cursor()
            print('Conectado no BD')
        except:
            print('\033[31mErro ao conectar no BD!\033[m')

    def clear(self):
        self.codigo_Capt = self.codBarrasEntry.delete(0, END)
        self.sphe_Capt = self.sphe_Entry.delete(0, END)
        self.cylin_Capt = self.cylin_Entry.delete(0, END)
        self.add_Capt = self.add_Entry.delete(0, END)
        self.eye_Capt = self.eye_Entry.delete(0, END)
        self.lab = self.lab_Entry.delete(0, END)
        self.mat_Capt = self.mat_Entry.delete(0, END)

    def captura_dados(self):
        self.codigo_Capt = self.codBarrasEntry.get()
        self.sphe_Capt = self.sphe_Entry.get()
        self.cylin_Capt = self.cylin_Entry.get()
        self.add_Capt = self.add_Entry.get()
        self.eye_Capt = self.eye_Entry.get()
        self.lab_Capt = self.lab_Entry.get()
        self.mat_Capt = self.mat_Entry.get()

    def verification_Int(self):  #>>> VERIFICAR ESTA FUNÇÃO
        self.captura_dados()
        try:
            validate = str(self.codigo_Capt)
            if validate.isalpha() or validate.isspace():
                self.text_warning = 'DADOS INVÁLIDOS'
                self.sound()
                self.clear()
                print('\033[31mEntrada Inválida do if\033[m')
                return False
            else:
                return True
                self.text_warning = ''
                print('Dados aceitos!')
        except (ValueError, TypeError):
            print('\033[31mEntrada Inválida do try\033[m')

    def verification_Code(self):
        self.captura_dados()
        self.connect_BD()
        self.cursor.execute(f"SELECT amount FROM stock WHERE cod_barras = {self.codigo_Capt}")
        result = self.cursor.fetchone()
        if result is None:
            result = 0
        else:
            if result[0] > int(0):
                print('\033[31mChamando a função "Register_Cod"!\033[m')
                self.register_cod()
            else:
                self.text_warning = 'CADASTRAR LENTE'

    def insert_Dados(self, event):
        self.connect_BD()
        self.cursor.execute(f"SELECT material, spherical, cylindrical, adicao, eye, laboratory FROM stock")
        result = self.cursor.fetchall()
        for i in result:
            mat = (i[0])
            sphe = (i[1])
            cyl = (i[2])
            add = (i[3])
            eye = (i[4])
            lab = (i[5])

        self.mat_Entry.insert(END, mat)
        self.sphe_Entry.insert(END, sphe)
        self.cylin_Entry.insert(END, cyl)
        self.add_Entry.insert(END, add)
        self.eye_Entry.insert(END, eye)
        self.lab_Entry.insert(END, lab)

    # ESTA FUNÇÃO CASO JA TENHA O CÓDIGO DE BARRAS CADASTRADO
    def register_cod(self):
        if self.verification_Int():
            self.captura_dados()
            codigos = []

            self.cursor = self.conn.cursor()
            self.cursor.execute(f"SELECT cod_barras FROM stock ")
            result = self.cursor.fetchall()
            for d in result:
                e = d
                for c in e:
                    codigos.append(c)
            if int(self.codigo_Capt) in codigos:
                self.insert_Dados(event='')
                self.cursor.execute(f"UPDATE stock SET amount = amount+{1} WHERE cod_barras = {self.codigo_Capt}")
                self.conn.commit()
                self.conn.close()
                self.text_warning = 'LENTE ADICIONADA'
                self.warning()
                print(f'\033[34mLente adicionada com sucesso!\033[m'.title())
            else:
                print('Não existe esta lente na base de dados!'.title()) #>>> CRIAR FUNÇÃO PARA CADASTRAR A LENTE
                self.text_warning = 'CADASTRAR LENTE'
                self.sound()
                self.clear()
                self.connect_BD()
                self.captura_dados()
                self.cursor.execute(f"INSERT INTO stock VALUES "
                                    f"('{self.codigo_Capt}', '{self.mat_Capt}', '{self.sphe_Capt}', "
                                    f"'{self.cylin_Capt}', '{self.add_Capt}', '{self.eye_Capt}', "
                                    f"'{self.lab_Capt}', '1' )")
                print('\033[31mCadastrada lente ixesistete!\033[m'.title())

    def warning(self):
        self.font_warning = ('Verdana', 20, 'italic', 'bold')
        self.text_warning_Label = Label(self.frame_options, text=self.text_warning, font=self.font_warning,
                                        bg='#f0e68c', fg='red')

        self.text_warning_Label.place(relx=0.05, rely=0.60, relwidth=0.90, relheight=0.16)

    def sound(self):
        #  REPRODUZ TRÊS BIPS EM SEGUIDA
        import winsound
        for c in range(3):
            b = winsound.Beep(332, 200)
            self.warning()

    def label_and_entry(self):
        self.options()
        self.button_Ir()
        self.fontepadrao = ("Verdana", 10, "italic", 'bold')
        #  LABELS
        self.codBarras = Label(self.frame_options, text='Cód. De Barras:', font=self.fontepadrao, bg='#f0e68c')
        self.sphe_degree = Label(self.frame_options, text='Esférico:', font=self.fontepadrao, bg='#f0e68c')
        self.cylin_degree = Label(self.frame_options, text='Cilindrico:', font=self.fontepadrao, bg='#f0e68c')
        self.add = Label(self.frame_options, text='Adição:', font=self.fontepadrao, bg='#f0e68c')
        self.eye = Label(self.frame_options, text='Olho:', font=self.fontepadrao, bg='#f0e68c')
        self.lab = Label(self.frame_options, text='Laboratório:', font=self.fontepadrao, bg='#f0e68c')
        self.mat = Label(self.frame_options, text='Material:', font=self.fontepadrao, bg='#f0e68c')
        #  ESTRADA DE DADOS
        self.codBarrasEntry = Entry(self.frame_options, font=self.fontepadrao, bg='#eee8aa')
        self.sphe_Entry = Entry(self.frame_options, font=self.fontepadrao, bg='#eee8aa')
        self.cylin_Entry = Entry(self.frame_options, font=self.fontepadrao, bg='#eee8aa')
        self.add_Entry = Entry(self.frame_options, font=self.fontepadrao, bg='#eee8aa')
        self.eye_Entry = Entry(self.frame_options, font=self.fontepadrao, bg='#eee8aa')
        self.lab_Entry = Entry(self.frame_options, font=self.fontepadrao, bg='#eee8aa')
        self.mat_Entry = Entry(self.frame_options, font=self.fontepadrao, bg='#eee8aa')
        #  LOCALIZAÇÃO DAS LABELS
        self.codBarras.place(relx=0.010, rely=0.08, relwidth=0.20, relheight=0.15)
        self.sphe_degree.place(relx=0.44, rely=0.08, relwidth=0.17, relheight=0.15)
        self.cylin_degree.place(relx=0.72, rely=0.08, relwidth=0.14, relheight=0.15)
        self.add.place(relx=0.19, rely=0.48, relwidth=0.10, relheight=0.15)
        self.eye.place(relx=0.625, rely=0.48, relwidth=0.15, relheight=0.15)
        self.lab.place(relx=0.01, rely=0.275, relwidth=0.20, relheight=0.15)
        self.mat.place(relx=0.50, rely=0.275, relwidth=0.20, relheight=0.15)
        #  LOCALIZAÇÃO DAS ENTRY
        self.codBarrasEntry.place(relx=0.22, rely=0.10, relwidth=0.23, relheight=0.11)
        self.sphe_Entry.place(relx=0.59, rely=0.10, relwidth=0.12, relheight=0.11)
        self.cylin_Entry.place(relx=0.86, rely=0.10, relwidth=0.12, relheight=0.11)
        self.add_Entry.place(relx=0.30, rely=0.50, relwidth=0.08, relheight=0.11)
        self.eye_Entry.place(relx=0.75, rely=0.50, relwidth=0.08, relheight=0.11)
        self.lab_Entry.place(relx=0.20, rely=0.295, relwidth=0.30, relheight=0.11)
        self.mat_Entry.place(relx=0.665, rely=0.295, relwidth=0.30, relheight=0.11)


    ### ENTRADA DE DADOS ###
### FRONT END ###
class Interface(Funcs):
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
        self.logo()
        root.mainloop()

    # FRAMES
    def tela(self):  # caracteristicas da tela
        self.root.title("Gerenciamento Laboratório Carol")
        self.root.geometry("1300x720")
        self.root.resizable(True, True)
        self.root.minsize(width=800, height=500)
        self.root.configure(background="#0000cd")

    def titulo(self):  # frame do título e algumas informções não excenciais
        self.frame_titulo = Frame(self.root, bd=-4, bg="#ffd700", highlightbackground="#1c1c1c",
                                  highlightthickness=2)
        self.frame_titulo.place(relx=0.13, rely=0.02, relwidth=0.45, relheight=0.15)

    def buttons(self):  # frame dos botões
        self.frame_buttons = Frame(self.root, bd=-4, bg="#ffd700", highlightbackground="#1c1c1c",
                                   highlightthickness=2)
        self.frame_buttons.place(relx=0.01, rely=0.02, relwidth=0.11, relheight=0.96)

    def informations(self):  # frame das informações
        self.frame_informations = Frame(self.root, bd=-4, bg="#ffd700", highlightbackground="#1c1c1c",
                                        highlightthickness=2)
        self.frame_informations.place(relx=0.13, rely=0.19, relwidth=0.45, relheight=0.79)

    def services(self):
        self.frame_services = Frame(self.root, bd=-4, bg="#ffd700", highlightbackground="#1c1c1c",
                                    highlightthickness=2)
        self.frame_services.place(relx=0.59, rely=0.02, relwidth=0.40, relheight=0.96)

    def options(self):
        self.frame_options = Frame(self.root, bd=-4, bg="#f0e68c", highlightbackground="#1c1c1c",
                                   highlightthickness=2)
        self.frame_options.place(relx=0.14, rely=0.21, relwidth=0.43, relheight=0.30)


    ### BOTÕES ###

    #>>>>>
    # OPÇÕES DO BOTÃO ENTER   ###>>>> ARRUMAR AQUI <<<<### O COMANDO DO MYSQL
    def option_Ir(self):
        print("Botão 'ir' clicado!".title())
        self.verification_Code()
        self.captura_dados()
        self.clear()
        print('Opção do botão IR concluída!')

    #  BOTÃO ENTER DE CADASTRO DE LENTES
    def button_Ir(self):
        self.fontepadrao = ("Verdana", 10, "italic", 'bold')
        self.Ir = Button(self.frame_options, text='Ir', font=self.fontepadrao, bg='#f0e68c', command=self.option_Ir)

        self.Ir.place(relx=0.425, rely=0.80, relwidth=0.15, relheight=0.15)
    #<<<<<

    #>>>>>
    #  OPÇOES DE CADASTRO DE LENTES
    def option_RegisterLens(self):
        print("Botão de cadastro clicado!".title())
        self.label_and_entry()
    #  BOTÃO CADASTRAR
    def button_Cadastrar(self):
        self.CadastrarLente = Button(self.frame_buttons, text="Cadastrar", command=self.option_RegisterLens,
                                     bd=2, bg="#c0c0c0", fg="black")
        self.CadastrarLente["font"] = ("Verdana", 10, "italic", "bold")
        self.CadastrarLente.place(relx=0.05, rely=0.02, relwidth=0.90, relheight=0.05)
    #<<<<<

    #>>>>>
    #  OPÇÕES DE VISUALIZAÇÃO DO ESTOQUE
    def exibirOpcoes(self):
        print("Botão visualizar estoque clicado!".title())
        self.label_and_entry()

    #  BOTÃO VISUALIZAR
    def button_VisEstoque(self):
        self.VisEstoque = Button(self.frame_buttons, text="Vis. Estoque", bd=2, bg="#c0c0c0", fg="black",
                                 command=self.exibirOpcoes)
        self.VisEstoque["font"] = ("Verdana", 10, "italic", "bold")
        self.VisEstoque.place(relx=0.05, rely=0.08, relwidth=0.90, relheight=0.05)
    #<<<<<

    #>>>>>
    #  OPÇÕES DE LENTES ZERADAS NO ESTOQUE
    def zero_lens(self):
        print("Botão lentes em falta clicado!".title())
        self.options()

    # BOTÃO LENTES ZERADAS
    def button_LensZero(self):
        self.LensZero = Button(self.frame_buttons, text="Lentes\nem\nFalta", bd=2, bg="#c0c0c0", fg="black",
                               command=self.zero_lens)
        self.LensZero["font"] = ("Verdana", 10, "italic", "bold")
        self.LensZero.place(relx=0.05, rely=0.14, relwidth=0.90, relheight=0.10)
    #<<<<<

    #>>>>>
    #  OPÇÕES DE RETIRAR LENTES
    def lens_output(self):
        print("Botão retirar lente clicado!".title())
        self.options()
        self.fontepadrao = ("Verdana", 10, "italic", 'bold')
        self.codBarras = Label(self.frame_options, text='Cód. De Barras:', font=self.fontepadrao, bg='#f0e68c')
        self.codBarrasEntry = Entry(self.frame_options, font=self.fontepadrao, bg='#eee8aa')
        self.codBarrasEntry.place(relx=0.43, rely=0.08, relwidth=0.40, relheight=0.13)
        self.codBarras.place(relx=0.11, rely=0.08, relwidth=0.30, relheight=0.15)

    #  BOTÃO RETIRAR
    def button_Retirar(self):
        self.Retirar = Button(self.frame_buttons, text="Retirar", bd=2, bg="#c0c0c0", fg="black",
                              command=self.lens_output)
        self.Retirar["font"] = ("Verdana", 10, "italic", "bold")
        self.Retirar.place(relx=0.05, rely=0.25, relwidth=0.90, relheight=0.05)
    #<<<<<

    #>>>>>
    #  OPÇÕES DE REGISTRAR SAÍDAS DE LENTES
    def reg_output(self):
        print("Botão registro de saída clicado!".title())
        self.options()

    #  BOTÃO
    def button_RegSaida(self):
        self.RegSaida = Button(self.frame_buttons, text="Registro\nde\nSaída", bg="#c0c0c0", fg="black",
                               command=self.reg_output)
        self.RegSaida["font"] = ("Verdana", 10, "italic", "bold")
        self.RegSaida.place(relx=0.05, rely=0.31, relwidth=0.90, relheight=0.10)
    #<<<<<

    #  BOTÃO DE SAIR
    def button_Sair(self):
        self.Sair = Button(self.frame_buttons, text="Sair", bg="#c0c0c0", fg="black")
        self.Sair["font"] = ("Verdana", 10, "italic", "bold")
        self.Sair["command"] = quit
        self.Sair.place(relx=0.05, rely=0.93, relwidth=0.90, relheight=0.05)



    #>>>>>
    # ENTRADA DE DADOS NA LABEL DO TITULO E INFORMAÇÕES
    def logo(self):
        self.fontepadraoLogo = ('Miso', '40')
        self.logoText_1 = Label(self.frame_titulo, text='ÓTICAS', bg='#ffd700', font=self.fontepadraoLogo, fg='white')
        self.logoText_2 = Label(self.frame_titulo, text='|', bg='#ffd700', font=self.fontepadraoLogo, fg='white')
        self.logoText_3 = Label(self.frame_titulo, text='CAROL', bg='#ffd700', font=self.fontepadraoLogo, fg='#0000cd')

        self.logoText_1.place(relx=0.15, rely=0.03, relwidth=0.335, relheight=0.55)
        self.logoText_2.place(relx=0.485, rely=0.014, relwidth=0.03, relheight=0.53)
        self.logoText_3.place(relx=0.515, rely=0.03, relwidth=0.305, relheight=0.55)

    def entry_Login(self):
        self.labelLogin = Label(self.frame_titulo, text="Usuário:", bg="#ffd700")
        self.labelLogin["font"] = ("Verdana", 10, "italic", "bold")
        self.labelLogin.place(relx=0.02, rely=0.60, relwidth=0.11, relheight=0.20)

        self.Login = Entry(self.frame_titulo, bg='#eee8aa')
        self.Login["font"] = ("Verdana", 10, "italic")
        self.Login.place(relx=0.14, rely=0.60, relwidth=0.35, relheight=0.20)

    def entry_Senha(self):
        self.labelSenha = Label(self.frame_titulo, text="Senha:", bg="#ffd700")
        self.labelSenha["font"] = ("Verdana", 10, "italic", "bold")
        self.labelSenha.place(relx=0.55, rely=0.60, relwidth=0.09, relheight=0.20)

        self.Senha = Entry(self.frame_titulo, bg='#eee8aa')
        self.Senha["font"] = ("Verdana", 10, "italic")
        self.Senha["show"] = "*"
        self.Senha.place(relx=0.65, rely=0.60, relwidth=0.32, relheight=0.20)
    #<<<<<


Interface()  # chamando a classe para iniciar

# sistema desencolvido por Matheus Brodt no ano de 2021 para fins de estudo e de uso próprio...
