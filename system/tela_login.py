# =========================//======================/TELA DE OBSERVAÇÕES/======================//========================

class Interface_Obs():
    def __init__(self):
        self.obs = Tk()
        self.connect_BD()
        self.fontepadrao = ("Verdana", 10, "italic", 'bold')
        self.tela_obs()
        self.frame()
        self.funcs_Obs()
        self.button()
        self.Funcs.double_Click()

    def connect_BD(self): # acho que aqui não precisa
        try:
            self.conn = mysql.connector.connect(host='localhost', user='root', password='', database="lab_carol")
            self.cursor = self.conn.cursor()
            print('Conectado no BD')
        except mysql.connector.errors.ProgrammingError:  # AJUSTAR EXCESSÃO DE ERRO
            print('\033[31mErro ao conectar no BD!\033[m')


    def frame(self):
        self.frame_fundo = Frame(self.obs, bg='#ffd700')
        self.frame_fundo.place(relx=0.02, rely=0.03, relwidth=0.96, relheight=0.94)
    def tela_obs(self):
        self.obs.title('Observações')
        self.obs.geometry('500x300')
        self.obs.resizable(False, False)
        self.obs.configure(background='Blue')

    def funcs_Obs(self, event=''):
        # LABELS
        self.situation = Label(self.frame_fundo, text='Situação:', bg='#ffd700', fg='black', font=self.fontepadrao)
        self.situation.place(relx=0.32, rely=0.10, relwidth=0.14, relheight=0.08)
        self.observation = Label(self.frame_fundo, text='Observação', bg='#ffd700', fg='black', font=self.fontepadrao)
        self.observation.place(relx=0.42, rely=0.30, relwidth=0.20, relheight=0.08)
        # ENTRYS
        self.situationEntry = ttk.Combobox(self.frame_fundo, font=self.fontepadrao)
        self.situationEntry['values'] = ('Digitação', 'Aguardando', 'Montagem', 'Finalizado', 'Retrabalho')
        self.situationEntry.bind("<Return>", self.option_Button)
        self.situationEntry.place(relx=0.465, rely=0.10, relwidth=0.23, relheight=0.08)

        self.text = Text(self.frame_fundo, font=self.fontepadrao, bg='#f0e68c', highlightbackground="#1c1c1c",
                                   highlightthickness=1)
        self.text.place(relx=0.10, rely=0.40, relwidth=0.80, relheight=0.40)

    def button(self):
        self.button_Enter = Button(self.frame_fundo, font=self.fontepadrao, text='Inserir', bg='#f0e68c',
                                   command=self.option_Button)
        self.button_Enter.bind('<Enter>', self.passou_por_cima)
        self.button_Enter.bind('<Leave>', self.saiu_de_cima)
        self.button_Enter.place(relx=0.425, rely=0.86, relwidth=0.15, relheight=0.08)

    def option_Button(self, event=''):
        self.CaptDados()

    # EFEITOS NOS BOTÕES
    def passou_por_cima(self, event):
        event.widget.config(relief=GROOVE)
    def saiu_de_cima(self, event):
        event.widget.config(relief=RAISED)

    # CAPTURA DE DADOS
    def CaptDados_Obs(self):
        self.situationCapt = self.situationEntry.get()
        self.textCapt = self.text.get('1.0')

    # MANIPULAÇÃO DE DADOS
    def insert_Obs(self):
        print('')

    def alter_Sit(self):
        print('')

    def start_Obs(self, event=''):
        Interface_Obs()
        print('Start')