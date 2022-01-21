from tkinter import *
from tkinter import ttk

windon = Tk()


class FullScreen:
    def __init__(self):
        print('Windon starting')
        self.windon = windon
        self.features()
        self.logo()
        self.f_buttons()
        self.layout()
        self.menu_buttons()
        self.start()
        windon.mainloop()

    def start(self):
        # functions starting
        print()

    def features(self):
        self.windon.title('Laboratório Carol')
        self.windon.geometry('1360x720')
        self.windon.resizable(True, True)
        self.windon.minsize(width=800, height=500)
        self.windon.configure(background="#363636")

    def logo(self):
        font = ('Verdana', '30')
        img_logo = Frame(self.windon, bg="#363636")
        text_logo = Label(img_logo, text='LABORATÓRIO CAROL', font=font, bg='#363636', fg='#FFD700')
        text_logo.place(relx=0.05, rely=0.05, relwidth=0.90, relheight=0.90)
        img_logo.place(relx=0.325, rely=0.01, relwidth=0.35, relheight=0.08)

    def f_buttons(self):
        self.frame_button = Frame(self.windon, bd=-4, bg="#363636", highlightbackground="#1c1c1c", highlightthickness=2)
        self.frame_button.place(relx=0.00, rely=0.10, relwidth=1.00, relheight=0.08)

    def layout(self):
        self.f_layout = Frame(self.windon, bg='#808080')
        self.f_layout.place(relx=0.0025, rely=0.185, relwidth=0.995, relheight=0.81)

    def menu_buttons(self):
        services = Button(self.frame_button, text='Serviços', bg='#808080', bd='0', activebackgroun='#808080',
                          state='active', command=self.frame_services)
        services["font"] = ('Verdana', '13', 'italic', 'bold')
        services.bind('<Enter>', self.enter)
        services.bind('<Leave>', self.leave)
        services.place(relx='0.025', rely='0.20', relwidth='0.10', relheight='0.60')

        pouch = Button(self.frame_button, text='Malotes', bg='#808080', bd='0', activebackgroun='#808080',
                       state='active', command=self.pouch)
        pouch["font"] = ('Verdana', '13', 'italic', 'bold')
        pouch.bind('<Enter>', self.enter)
        pouch.bind('<Leave>', self.leave)
        pouch.place(relx='0.15', rely='0.20', relwidth='0.10', relheight='0.60')

        lens = Button(self.frame_button, text='Lentes', bg='#808080', bd='0', activebackgroun='#808080',
                       state='active', command=self.lens_button)
        lens["font"] = ('Verdana', '13', 'italic', 'bold')
        lens.bind('<Enter>', self.enter)
        lens.bind('<Leave>', self.leave)
        lens.place(relx='0.30', rely='0.20', relwidth='0.10', relheight='0.60')

        mov_serv = Button(self.frame_button, text='Mov. Serv.', bg='#808080', bd='0', activebackgroun='#808080',
                          state='active', command=self.movServ_button)
        mov_serv["font"] = ('Verdana', '13', 'italic', 'bold')
        mov_serv.bind('<Enter>', self.enter)
        mov_serv.bind('<Leave>', self.leave)
        mov_serv.place(relx='0.45', rely='0.20', relwidth='0.10', relheight='0.60')

        smash = Button(self.frame_button, text='Quebras', bg='#808080', bd='0', activebackgroun='#808080',
                       state='active')
        smash["font"] = ('Verdana', '13', 'italic', 'bold')
        smash.bind('<Enter>', self.enter)
        smash.bind('<Leave>', self.leave)
        smash.place(relx='0.60', rely='0.20', relwidth='0.10', relheight='0.60')

        reports = Button(self.frame_button, text='Relatórios', bg='#808080', bd='0', activebackgroun='#808080',
                       state='active')
        reports["font"] = ('Verdana', '13', 'italic', 'bold')
        reports.bind('<Enter>', self.enter)
        reports.bind('<Leave>', self.leave)
        reports.place(relx='0.60', rely='0.20', relwidth='0.10', relheight='0.60')

        exit = Button(self.frame_button, text='Sair', bg='#808080', bd='0', activebackgroun='#808080',
                       state='active')
        exit["font"] = ('Verdana', '13', 'italic', 'bold')
        exit.bind('<Enter>', self.enter)
        exit.bind('<Leave>', self.leave)
        exit.place(relx='0.75', rely='0.20', relwidth='0.10', relheight='0.60')

    def frame_services(self):
        self.layout()
        list_store = ('2064', '1432', '1518', '1571', '2007', '2226')
        list_lab = ('Haytek', 'Farol', 'Zeiss', 'Hoya', 'Wallau', 'Forla', 'Grow')
        list_situation = ('Aguardando', 'Montagem', 'Lentes Separadas', 'Urgente', 'Montagem Farol', 'Montagem Forla',
                          'Montagem Wallau', 'Montagem Paris', 'Complete Frame')
        font = ('Verdana', '12')
        # list
        lista = Frame(self.f_layout, bd=-10, bg="#C0C0C0", highlightbackground="#1c1c1c", highlightthickness=2)
        lista.place(relx='0.0025', rely='0.0040', relwidth='0.16', relheight='0.99')
        list_tilte = Label(lista, text='BUSCA', bg='#C0C0C0')
        list_tilte["font"] = ('Verdana', '15')
        list_tilte.place(relx='0.25', rely='0.025', relwidth='0.50', relheight='0.04')

        # datas
        datas = Frame(self.f_layout, bd=-10, bg="#C0C0C0", highlightbackground="#1c1c1c", highlightthickness=2)
        datas.place(relx='0.165', rely='0.0040', relwidth='0.50', relheight='0.99')
        data_title = Label(datas, text='DADOS DO SERVIÇO', bg='#C0C0C0')
        data_title["font"] = ('Verdana', '15')
        data_title.place(relx='0.25', rely='0.025', relwidth='0.50', relheight='0.04')

        # historic
        historic = Frame(self.f_layout, bd=-10, bg="#C0C0C0", highlightbackground="#1c1c1c", highlightthickness=2)
        historic.place(relx='0.667', rely='0.0040', relwidth='0.331', relheight='0.99')
        hist_title = Label(historic, text='HISTÓRICO', bg='#C0C0C0')
        hist_title["font"] = ('Verdana', '15')
        hist_title.place(relx='0.25', rely='0.025', relwidth='0.50', relheight='0.04')
        self.data_hist = Text(historic, bg='#FFF', font=font)
        self.data_hist.place(relx='0.025', rely='0.07', relwidth='0.95', relheight='0.91')

        # data_list
        store = Label(lista, text='Loja', font=font, bg='#C0C0C0')
        store.place(relx='0.13', rely='0.07', relwidth='0.20', relheight='0.04')
        seq = Label(lista, text='Sequência', font=font, bg='#C0C0C0')
        seq.place(relx='0.42', rely='0.07', relwidth='0.50', relheight='0.04')

        ent_store = ttk.Combobox(lista, font=font)
        ent_store['values'] = list_store
        ent_store.place(relx='0.08', rely='0.11', relwidth='0.30', relheight='0.04')
        ent_seq = Entry(lista, bg='#FFF', font=font)
        ent_seq.place(relx='0.52', rely='0.11', relwidth='0.30', relheight='0.04')

        button = Button(lista, text='Buscar', bg='#808080', bd='0', activebackgroun='#808080')
        button.bind('<Enter>', self.enter)
        button.bind('<Leave>', self.leave)
        button.place(relx='0.20', rely='0.17', relwidth='0.60', relheight='0.04')

        # data_inf
        seq = Label(datas, text='Sequência:', bg='#C0C0C0', font=font)
        store = Label(datas, text='Loja:', bg='#C0C0C0', font=font)
        lab = Label(datas, text='Laboratório:', bg='#C0C0C0', font=font)
        n_order = Label(datas, text='N. Pedido:', bg='#C0C0C0', font=font)
        prev_lab = Label(datas, text='Prev. Laboratório:', bg='#C0C0C0', font=font)
        prev_svc = Label(datas, text='Prev. Serviço:', bg='#C0C0C0', font=font)
        typing_resp = Label(datas, text='Digitado por:', bg='#C0C0C0', font=font)
        cost = Label(datas, text='Custo:', bg='#C0C0C0', font=font)
        smash_cost = Label(datas, text='Custo em Garantias:', bg='#C0C0C0', font=font)
        tipo = Label(datas, text='Tipo:', bg='#C0C0C0', font=font)
        sit = Label(datas, text='Situação:', bg='#C0C0C0', font=font)
        obs = Label(datas, text='Observação:', bg='#C0C0C0', font=font)
        status = Label(datas, text='Status:', bg='#C0C0C0', font=font)
        box = Label(datas, text='Caixa:', bg='#C0C0C0', font=font)
        cod_bars = Label(datas, text='Cod. Barras:', bg='#C0C0C0', font=font)
        pouch = Label(datas, text='Malote:', bg='#C0C0C0', font=font)

        seq.place(relx='0.05', rely='0.07', relwidth='0.13', relheight='0.04')
        store.place(relx='0.05', rely='0.12', relwidth='0.06', relheight='0.04')
        lab.place(relx='0.05', rely='0.17', relwidth='0.145', relheight='0.04')
        n_order.place(relx='0.05', rely='0.22', relwidth='0.12', relheight='0.04')
        prev_lab.place(relx='0.05', rely='0.27', relwidth='0.21', relheight='0.04')
        prev_svc.place(relx='0.05', rely='0.32', relwidth='0.16', relheight='0.04')
        typing_resp.place(relx='0.05', rely='0.37', relwidth='0.15', relheight='0.04')
        cost.place(relx='0.05', rely='0.42', relwidth='0.07', relheight='0.04')
        smash_cost.place(relx='0.05', rely='0.47', relwidth='0.235', relheight='0.04')
        tipo.place(relx='0.05', rely='0.52', relwidth='0.06', relheight='0.04')
        sit.place(relx='0.05', rely='0.57', relwidth='0.11', relheight='0.04')
        obs.place(relx='0.05', rely='0.62', relwidth='0.15', relheight='0.04')
        status.place(relx='0.05', rely='0.72', relwidth='0.08', relheight='0.04')
        box.place(relx='0.05', rely='0.77', relwidth='0.07', relheight='0.04')
        cod_bars.place(relx='0.05', rely='0.82', relwidth='0.145', relheight='0.04')
        pouch.place(relx='0.05', rely='0.87', relwidth='0.085', relheight='0.04')

        self.seq = Entry(datas, bg='#FFF', font=font)
        self.store = Entry(datas, bg='#FFF', font=font)
        self.lab = ttk.Combobox(datas,  font=font)
        self.lab['values'] = list_lab
        self.n_order = Entry(datas, bg='#FFF', font=font)
        self.prev_lab = Entry(datas, bg='#FFF', font=font)
        self.prev_svc = Entry(datas, bg='#FFF', font=font)
        self.typing_resp = Entry(datas, bg='#FFF', font=font)
        self.cost = Entry(datas, bg='#FFF', font=font)
        self.smash_cost = Entry(datas, bg='#FFF', font=font)
        self.tipo = ttk.Combobox(datas, font=font)
        self.tipo['values'] = ('Visão Simples', 'Multifocal')
        self.sit = ttk.Combobox(datas, font=font)
        self.sit['values'] = list_situation
        self.obs = Text(datas, bg='#FFF', font=font)
        self.status = Entry(datas, bg='#FFF', font=font)
        self.box = Entry(datas, bg='#FFF', font=font)
        self.cod_bars = Entry(datas, bg='#FFF', font=font)
        self.pouch = Entry(datas, bg='#FFF', font=font)

        self.seq.place(relx='0.40', rely='0.07', relwidth='0.35', relheight='0.04')
        self.store.place(relx='0.40', rely='0.12', relwidth='0.35', relheight='0.04')
        self.lab.place(relx='0.40', rely='0.17', relwidth='0.35', relheight='0.04')
        self.n_order.place(relx='0.40', rely='0.22', relwidth='0.35', relheight='0.04')
        self.prev_lab.place(relx='0.40', rely='0.27', relwidth='0.35', relheight='0.04')
        self.prev_svc.place(relx='0.40', rely='0.32', relwidth='0.35', relheight='0.04')
        self.typing_resp.place(relx='0.40', rely='0.37', relwidth='0.35', relheight='0.04')
        self.cost.place(relx='0.40', rely='0.42', relwidth='0.35', relheight='0.04')
        self.smash_cost.place(relx='0.40', rely='0.47', relwidth='0.35', relheight='0.04')
        self.tipo.place(relx='0.40', rely='0.52', relwidth='0.35', relheight='0.04')
        self.sit.place(relx='0.40', rely='0.57', relwidth='0.35', relheight='0.04')
        self.obs.place(relx='0.40', rely='0.62', relwidth='0.35', relheight='0.09')
        self.status.place(relx='0.40', rely='0.72', relwidth='0.35', relheight='0.04')
        self.box.place(relx='0.40', rely='0.77', relwidth='0.35', relheight='0.04')
        self.cod_bars.place(relx='0.40', rely='0.82', relwidth='0.35', relheight='0.04')
        self.pouch.place(relx='0.40', rely='0.87', relwidth='0.35', relheight='0.04')

        alt_button = Button(datas, text='Alterar', bg='#808080', bd='0', activebackgroun='#808080')
        alt_button.bind('<Enter>', self.enter)
        alt_button.bind('<Leave>', self.leave)
        alt_button.place(relx='0.20', rely='0.94', relwidth='0.20', relheight='0.04')

        save_button = Button(datas, text='Cadastrar', bg='#808080', bd='0', activebackgroun='#808080')
        save_button.bind('<Enter>', self.enter)
        save_button.bind('<Leave>', self.leave)
        save_button.place(relx='0.60', rely='0.94', relwidth='0.20', relheight='0.04')

        # search_list
        src_list = ttk.Treeview(lista, height=6, columns=('col1', 'col2'))
        src_list.place(relx='0.01   ', rely='0.23 ', relwidth='0.98', relheight='0.765')
        src_list.heading('#0')
        src_list.heading('col1', text='Loja')
        src_list.heading('col2', text='Sequência')
        src_list.column('#0', width=0)
        src_list.column('col1', width=60)
        src_list.column('col2', width=100)

    def pouch(self):
        self.layout()
        font = ('Verdana', '12', 'bold', 'italic')

        f_buttons = Frame(self.f_layout, bd=-10, bg="#C0C0C0", highlightbackground="#1c1c1c", highlightthickness=2)
        f_buttons.place(relx='0.003', rely='0.005', relwidth='0.14', relheight='0.99')

        src_button = Button(f_buttons, text='Buscar', font=font, bg='#808080', bd='0', activebackgroun='#808080',
                            command=self.src_Pouchlayout)
        src_button.bind('<Enter>', self.enter)
        src_button.bind('<Leave>', self.leave)
        src_button.place(relx='0.05', rely='0.03', relwidth='0.90', relheight='0.06')

        add_button = Button(f_buttons, text='Add. Malote', font=font, bg='#808080', bd='0', activebackgroun='#808080',
                             command=self.add_in_pouch)
        add_button.bind('<Enter>', self.enter)
        add_button.bind('<Leave>', self.leave)
        add_button.place(relx='0.05', rely='0.12', relwidth='0.90', relheight='0.06')

        rec_button = Button(f_buttons, text='Rec. Malote', font=font, bg='#808080', bd='0', activebackgroun='#808080',
                            command=self.rec_pouch)
        rec_button.bind('<Enter>', self.enter)
        rec_button.bind('<Leave>', self.leave)
        rec_button.place(relx='0.05', rely='0.21', relwidth='0.90', relheight='0.06')

        exp_pouch = Button(f_buttons, text='Exp. Malote', font=font, bg='#808080', bd='0', activebackgroun='#808080',
                           command=self.send_pouch)
        exp_pouch.bind('<Enter>', self.enter)
        exp_pouch.bind('<Leave>', self.leave)
        exp_pouch.place(relx='0.05', rely='0.30', relwidth='0.90', relheight='0.06')

    def src_Pouchlayout(self):
        frame_layout = Frame(self.f_layout, bg='#808080')
        frame_layout.place(relx='0.145', rely='0.005', relwidth='0.855', relheight='0.99')
        font = ('Verdana', '15')
        search = Frame(frame_layout, bg='#C0C0C0', highlightbackground="#1c1c1c", highlightthickness=2)
        search.place(relx='0.00', rely='0.00', relwidth='0.70', relheight='1.00')
        title = Label(search, text='BUSCAR MALOTE', font=font, bg='#C0C0C0')
        title.place(relx='0.05', rely='0.010', relwidth='0.90', relheight='0.06')

        self.src_seqPouch = Entry(search, bg='#FFF')
        self.src_seqPouch.place(relx='0.40', rely='0.10', relwidth='0.20', relheight='0.045')

        srcPouch_button = Button(search,  text='Buscar', bg='#808080', bd='0', activebackgroun='#808080')
        srcPouch_button['font'] = ('Verdana', '12')
        srcPouch_button.place(relx='0.425', rely='0.18', relwidth='0.15', relheight='0.04')

        # list
        lista = ttk.Treeview(search, height=6, columns=('col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7'))
        lista.place(relx='0.01', rely='0.25', relwidth='0.98', relheight='0.745')
        lista.heading('#0')
        lista.heading('col1', text='Loja')
        lista.heading('col2', text='Seq')
        lista.heading('col3', text='Previsão')
        lista.heading('col4', text='Data da Venda')
        lista.heading('col5', text='Data de Envio')
        lista.heading('col6', text='Data de Recebimento')
        lista.heading('col7', text='Status')

        lista.column('#0', width=0)
        lista.column('col1', width=20)
        lista.column('col2', width=30)
        lista.column('col3', width=90)
        lista.column('col4', width=90)
        lista.column('col5', width=90)
        lista.column('col6', width=140)
        lista.column('col7', width=50)

        # historic
        historic = Frame(frame_layout, bd=-10, bg="#C0C0C0", highlightbackground="#1c1c1c", highlightthickness=2)
        historic.place(relx='0.703 ', rely='0.00', relwidth='0.294', relheight='1.00')
        hist_title = Label(historic, text='HISTÓRICO', bg='#C0C0C0')
        hist_title["font"] = ('Verdana', '15')
        hist_title.place(relx='0.25', rely='0.025', relwidth='0.50', relheight='0.04')
        self.hist_pouch = Text(historic, bg='#FFF', font=font)
        self.hist_pouch.place(relx='0.025', rely='0.07', relwidth='0.95', relheight='0.91')

    def add_in_pouch(self):
        frame_layout = Frame(self.f_layout, bg='#808080')
        frame_layout.place(relx='0.145', rely='0.005', relwidth='0.855', relheight='0.99')
        list_store = ('2064', '1432', '1518', '1571', '2007', '2226')
        font = ('Verdana', '15')
        layout = Frame(frame_layout, bg='#C0C0C0', highlightbackground="#1c1c1c", highlightthickness=2)
        layout.place(relx='0.17', rely='0.00', relwidth='0.63', relheight='1.00')
        title = Label(layout, text='ADICIONAR NO MALOTE', font=font, bg='#C0C0C0')
        title.place(relx='0.05', rely='0.010', relwidth='0.90', relheight='0.06')

        self.src_seqPouch = Entry(layout, bg='#FFF')
        self.src_seqPouch.place(relx='0.40', rely='0.10', relwidth='0.20', relheight='0.045')

        pouch_button = Button(layout, text='Adiconar', bg='#808080', bd='0', activebackgroun='#808080')
        pouch_button['font'] = ('Verdana', '12')
        pouch_button.place(relx='0.425', rely='0.18', relwidth='0.15', relheight='0.04')
        # list
        lista = ttk.Treeview(layout, height=6, columns=('col1', 'col2', 'col3', 'col4', 'col5', 'col6'))
        lista.place(relx='0.01', rely='0.25', relwidth='0.98', relheight='0.745')
        lista.heading('#0')
        lista.heading('col1', text='Loja')
        lista.heading('col2', text='Seq')
        lista.heading('col3', text='Previsão')
        lista.heading('col4', text='Data da Venda')
        lista.heading('col5', text='Data de Envio')
        lista.heading('col6', text='Status')

        lista.column('#0', width=0)
        lista.column('col1', width=20)
        lista.column('col2', width=30)
        lista.column('col3', width=90)
        lista.column('col4', width=90)
        lista.column('col5', width=90)
        lista.column('col6', width=50)

    def rec_pouch(self):
        frame_layout = Frame(self.f_layout, bg='#808080')
        frame_layout.place(relx='0.145', rely='0.005', relwidth='0.855', relheight='0.99')
        font = ('Verdana', '15')
        layout = Frame(frame_layout, bg='#C0C0C0', highlightbackground="#1c1c1c", highlightthickness=2)
        layout.place(relx='0.27', rely='0.20', relwidth='0.45', relheight='0.50')
        title = Label(layout, text='RECEBER MALOTE', font=font, bg='#C0C0C0')
        title.place(relx='0.05', rely='0.05', relwidth='0.90', relheight='0.06')

        n_pouch = Label(layout, text='N. do Malote', bg='#C0C0C0')
        n_pouch['font'] = ('Verdana', '12')
        n_pouch.place(relx='0.30', rely='0.32', relwidth='0.40', relheight='0.08')
        self.src_seqPouch = Entry(layout, bg='#FFF')
        self.src_seqPouch.place(relx='0.30', rely='0.40', relwidth='0.40', relheight='0.085')

        pouch_button = Button(layout, text='Receber', bg='#808080', bd='0', activebackgroun='#808080')
        pouch_button['font'] = ('Verdana', '12')
        pouch_button.place(relx='0.35', rely='0.80', relwidth='0.30', relheight='0.09')

    def send_pouch(self):
        frame_layout = Frame(self.f_layout, bg='#808080')
        frame_layout.place(relx='0.145', rely='0.005', relwidth='0.855', relheight='0.99')
        font = ('Verdana', '15')
        layout = Frame(frame_layout, bg='#C0C0C0', highlightbackground="#1c1c1c", highlightthickness=2)
        layout.place(relx='0.27', rely='0.20', relwidth='0.45', relheight='0.50')
        title = Label(layout, text='ENVIAR MALOTE', font=font, bg='#C0C0C0')
        title.place(relx='0.05', rely='0.05', relwidth='0.90', relheight='0.06')

        n_pouch = Label(layout, text='N. do Malote', bg='#C0C0C0')
        n_pouch['font'] = ('Verdana', '12')
        n_pouch.place(relx='0.30', rely='0.32', relwidth='0.40', relheight='0.08')
        self.src_seqPouch = Entry(layout, bg='#FFF')
        self.src_seqPouch.place(relx='0.30', rely='0.40', relwidth='0.40', relheight='0.085')
        password = Label(layout, text='Senha', bg='#C0C0C0')
        password['font'] = ('Verdana', '12')
        password.place(relx='0.30', rely='0.50', relwidth='0.40', relheight='0.08')
        pass_entry = Entry(layout, bg='#FFF')
        pass_entry.place(relx='0.35', rely='0.59', relwidth='0.30', relheight='0.085')

        pouch_button = Button(layout, text='Expedir', bg='#808080', bd='0', activebackgroun='#808080')
        pouch_button['font'] = ('Verdana', '12')
        pouch_button.place(relx='0.35', rely='0.80', relwidth='0.30', relheight='0.09')

    def lens_button(self):
        self.layout()
        font = ('Verdana', '12', 'bold', 'italic')

        f_buttons = Frame(self.f_layout, bd=-10, bg="#C0C0C0", highlightbackground="#1c1c1c", highlightthickness=2)
        f_buttons.place(relx='0.003', rely='0.005', relwidth='0.14', relheight='0.99')

        input_lens = Button(f_buttons, text='Cadastrar', font=font, bg='#808080', bd='0', activebackgroun='#808080',
                            command=self.cad_lens)
        input_lens.bind('<Enter>', self.enter)
        input_lens.bind('<Leave>', self.leave)
        input_lens.place(relx='0.05', rely='0.03', relwidth='0.90', relheight='0.06')

        src_lens = Button(f_buttons, text='Vis. Estoque', font=font, bg='#808080', bd='0', activebackgroun='#808080',
                            command=self.vis_stock)
        src_lens.bind('<Enter>', self.enter)
        src_lens.bind('<Leave>', self.leave)
        src_lens.place(relx='0.05', rely='0.12', relwidth='0.90', relheight='0.06')

        exit_lens = Button(f_buttons, text='Retirar', font=font, bg='#808080', bd='0', activebackgroun='#808080',
                            command=self.exit_lens)
        exit_lens.bind('<Enter>', self.enter)
        exit_lens.bind('<Leave>', self.leave)
        exit_lens.place(relx='0.05', rely='0.21', relwidth='0.90', relheight='0.06')

        register = Button(f_buttons, text='Registro', font=font, bg='#808080', bd='0', activebackgroun='#808080',
                           command=self.vis_reg)
        register.bind('<Enter>', self.enter)
        register.bind('<Leave>', self.leave)
        register.place(relx='0.05', rely='0.30', relwidth='0.90', relheight='0.06')

        reserve = Button(f_buttons, text='Reserva', font=font, bg='#808080', bd='0', activebackgroun='#808080',
                          command=self.vis_reserve)
        reserve.bind('<Enter>', self.enter)
        reserve.bind('<Leave>', self.leave)
        reserve.place(relx='0.05', rely='0.39', relwidth='0.90', relheight='0.06')

    def movServ_button(self):
        self.layout()
        font = ('Verdana', '12', 'bold', 'italic')

        f_buttons = Frame(self.f_layout, bd=-10, bg="#C0C0C0", highlightbackground="#1c1c1c", highlightthickness=2)
        f_buttons.place(relx='0.003', rely='0.005', relwidth='0.14', relheight='0.99')

        input_lens = Button(f_buttons, text='Cadastrar', font=font, bg='#808080', bd='0', activebackgroun='#808080',
                            command=self.cad_lens)
        input_lens.bind('<Enter>', self.enter)
        input_lens.bind('<Leave>', self.leave)
        input_lens.place(relx='0.05', rely='0.03', relwidth='0.90', relheight='0.06')

        src_lens = Button(f_buttons, text='Vis. Estoque', font=font, bg='#808080', bd='0', activebackgroun='#808080',
                            command=self.vis_stock)
        src_lens.bind('<Enter>', self.enter)
        src_lens.bind('<Leave>', self.leave)
        src_lens.place(relx='0.05', rely='0.12', relwidth='0.90', relheight='0.06')

        exit_lens = Button(f_buttons, text='Retirar', font=font, bg='#808080', bd='0', activebackgroun='#808080',
                            command=self.exit_lens)
        exit_lens.bind('<Enter>', self.enter)
        exit_lens.bind('<Leave>', self.leave)
        exit_lens.place(relx='0.05', rely='0.21', relwidth='0.90', relheight='0.06')

        register = Button(f_buttons, text='Registro', font=font, bg='#808080', bd='0', activebackgroun='#808080',
                           command=self.vis_reg)
        register.bind('<Enter>', self.enter)
        register.bind('<Leave>', self.leave)
        register.place(relx='0.05', rely='0.30', relwidth='0.90', relheight='0.06')

        reserve = Button(f_buttons, text='Reserva', font=font, bg='#808080', bd='0', activebackgroun='#808080',
                          command=self.vis_reserve)
        reserve.bind('<Enter>', self.enter)
        reserve.bind('<Leave>', self.leave)
        reserve.place(relx='0.05', rely='0.39', relwidth='0.90', relheight='0.06')

    def cad_lens(self):
        frame_layout = Frame(self.f_layout, bg='#808080')
        frame_layout.place(relx='0.145', rely='0.005', relwidth='0.855', relheight='0.99')

        layout = Frame(frame_layout, bd=-10, bg="#C0C0C0", highlightbackground="#1c1c1c", highlightthickness=2)
        layout.place(relx='0.00', rely='0.00', relwidth='0.60', relheight='1.00')

        lista = ttk.Treeview(frame_layout, height=6, columns=('col1', 'col2', 'col3', 'col4', 'col5', 'col6'))

        lista.heading('#0')
        lista.heading('col1', text='Cod. Barras')
        lista.heading('col2', text='Esf.')
        lista.heading('col3', text='Cil.')
        lista.heading('col4', text='Adição')
        lista.heading('col5', text='Material')
        lista.heading('col6', text='Unid.')

        lista.column('#0', width=0)
        lista.column('col1', width=100)
        lista.column('col2', width=50)
        lista.column('col3', width=50)
        lista.column('col4', width=70)
        lista.column('col5', width=100)
        lista.column('col6', width=100)

        lista.place(relx='0.604', rely='0.00', relwidth='0.392', relheight='1.00')

        # DATAS

        fontepadrao = ("Verdana", 10, 'bold')
        #  LABELS
        codBarras = Label(frame_layout, text='Cód. De Barras:', font=fontepadrao, bg='#C0C0C0')
        sphe_degree = Label(frame_layout, text='Esférico:', font=fontepadrao, bg='#C0C0C0')
        cylin_degree = Label(frame_layout, text='Cilindrico:', font=fontepadrao, bg='#C0C0C0')
        lab = Label(frame_layout, text='Laboratório:', font=fontepadrao, bg='#C0C0C0')
        mat = Label(frame_layout, text='Material:', font=fontepadrao, bg='#C0C0C0')
        add = Label(frame_layout, text='Adição:', font=fontepadrao, bg='#C0C0C0')
        eye = Label(frame_layout, text='Olho:', font=fontepadrao, bg='#C0C0C0')
        #  ESTRADA DE DADOS
        self.codBarrasEntry = Entry(frame_layout, font=fontepadrao, bg='white')
        self.codBarrasEntry.bind("<Return>")
        self.sphe_Entry = ttk.Combobox(frame_layout, font=fontepadrao)
        self.sphe_Entry['values'] = ('0.00', '+0.25', '+0.50', '+0.75', '+1.00', '+1.25', '+1.50', '+1.75', '+2.00',
                                     '+2.25', '+2.50', '+2.75', '+3.00', '+3.25', '+3.50', '+3.75', '+4.00',
                                     '-0.25', '-0.50', '-0.75', '-1.00', '-1.25', '-1.50', '-1.75', '-2.00',
                                     '-2.25',
                                     '-2.50', '-2.75', '-3.00', '-3.25', '-3.50', '-3.75', '-4.00')
        self.sphe_Entry.bind("<Return>")
        self.cylin_Entry = ttk.Combobox(frame_layout, font=fontepadrao)
        self.cylin_Entry['values'] = (
        '0.00', '-0.25', '-0.50', '-0.75', '-1.00', '-1.25', '-1.50', '-1.75', '-2.00',
        '-2.25', '-2.50', '-2.75', '-3.00', '-3.25', '-3.50', '-3.75', '-4.00')
        self.cylin_Entry.bind("<Return>")
        self.lab_Entry = ttk.Combobox(frame_layout, font=fontepadrao)
        self.lab_Entry['values'] = ('Farol', 'Haytek', 'Zeiss')
        self.lab_Entry.bind("<Return>")
        self.mat_Entry = ttk.Combobox(frame_layout, font=fontepadrao)
        self.mat_Entry['values'] = ('Lente Vis Simples 1.50 c/A.R.', 'Lente Vis Simples 1.56 c/A.R.',
                                    'Lente V.S. 1.56 Filtro Azul c/A.R.', 'Lente Vis Simp 1.59 Poly c/A.R.',
                                    'Lente Vis Simp 1.59 Poly Filtro Azul c/A.R.',
                                    'Lente Ac. Progressiva 1.56 c/A.R.',
                                    'Zeiss 1.50 Platinum', 'Zeiss 1.50 BlueProtect', 'Zeiss 1.50 Silver',
                                    'Zeiss 1.50 Photo')
        self.mat_Entry.bind("<Return>")
        self.add_Entry = ttk.Combobox(frame_layout, font=fontepadrao)
        self.add_Entry['values'] = ('1.00', '1.25', '1.50', '1.75', '2.00', '2.25', '2.50', '2.75', '3.00', '3.25',
                                    '3.50')
        self.add_Entry.bind("<Return>")
        self.eye_Entry = ttk.Combobox(frame_layout, font=fontepadrao)
        self.eye_Entry['values'] = ('D', 'E')
        self.eye_Entry.bind("<Return>")
        #  LOCALIZAÇÃO DAS LABELS
        codBarras.place(relx=0.095, rely=0.03, relwidth=0.20, relheight=0.05)
        sphe_degree.place(relx=0.087, rely=0.12, relwidth=0.17, relheight=0.05)
        cylin_degree.place(relx=0.107, rely=0.20, relwidth=0.14, relheight=0.05)
        lab.place(relx=0.085, rely=0.28, relwidth=0.20, relheight=0.05)
        mat.place(relx=0.075, rely=0.36, relwidth=0.20, relheight=0.05)
        add.place(relx=0.12, rely=0.44, relwidth=0.10, relheight=0.05)
        eye.place(relx=0.087, rely=0.52, relwidth=0.15, relheight=0.05)
        #  LOCALIZAÇÃO DAS ENTRY
        self.codBarrasEntry.place(relx=0.30, rely=0.03, relwidth=0.15, relheight=0.045)
        self.sphe_Entry.place(relx=0.30, rely=0.12, relwidth=0.15, relheight=0.045)
        self.cylin_Entry.place(relx=0.30, rely=0.20, relwidth=0.15, relheight=0.045)
        self.lab_Entry.place(relx=0.30, rely=0.28, relwidth=0.15, relheight=0.045)
        self.mat_Entry.place(relx=0.30, rely=0.36, relwidth=0.20, relheight=0.045)
        self.add_Entry.place(relx=0.30, rely=0.44, relwidth=0.15, relheight=0.045)
        self.eye_Entry.place(relx=0.30, rely=0.52, relwidth=0.15, relheight=0.045)

        button = Button(frame_layout, text='Cadastrar', font=fontepadrao, bg='#808080', bd='0',
                        activebackgroun='#808080')
        button.place(relx=0.25, rely=0.90, relwidth=0.10, relheight=0.05)

    def vis_stock(self):
        fontepadrao = ("Verdana", 10, 'bold')
        frame_layout = Frame(self.f_layout, bg='#808080')
        frame_layout.place(relx='0.145', rely='0.005', relwidth='0.855', relheight='0.99')

        l_visStock = Frame(frame_layout, bd=-10, bg="#C0C0C0", highlightbackground="#1c1c1c", highlightthickness=2)
        l_visStock.place(relx='0.10', rely='0.00', relwidth='0.80', relheight='1.00')

        title = Label(l_visStock, text='VISUALIZAR ESTOQUE', bg='#C0C0C0')
        title['font'] = ('Verdana', 14)
        title.place(relx='0.10', rely='0.015', relwidth='0.80', relheight='0.05')

        sphe = Label(l_visStock, text='Esférico', font=fontepadrao, bg='#C0C0C0')
        cylin = Label(l_visStock, text='Cilíndrico', font=fontepadrao, bg='#C0C0C0')
        add = Label(l_visStock, text='Adição', font=fontepadrao, bg='#C0C0C0')
        sphe.place(relx='0.20', rely='0.16', relwidth='0.10', relheight='0.04')
        cylin.place(relx='0.45', rely='0.16', relwidth='0.10', relheight='0.04')
        add.place(relx='0.70', rely='0.16', relwidth='0.10', relheight='0.04')

        self.stockVis_sphe = ttk.Combobox(l_visStock, font=fontepadrao)
        self.stockVis_sphe['values'] = ('0.00', '+0.25', '+0.50', '+0.75', '+1.00', '+1.25', '+1.50', '+1.75', '+2.00',
                               '+2.25', '+2.50', '+2.75', '+3.00', '+3.25', '+3.50', '+3.75', '+4.00',
                               '-0.25', '-0.50', '-0.75', '-1.00', '-1.25', '-1.50', '-1.75', '-2.00', '-2.25',
                               '-2.50', '-2.75', '-3.00', '-3.25', '-3.50', '-3.75', '-4.00')
        self.stockVis_cylin = ttk.Combobox(l_visStock, font=fontepadrao)
        self.stockVis_cylin['values'] = ('0.00', '-0.25', '-0.50', '-0.75', '-1.00', '-1.25', '-1.50', '-1.75',
                                '-2.00', '-2.25', '-2.50', '-2.75', '-3.00', '-3.25', '-3.50', '-3.75',
                                '-4.00')
        self.stockVis_add = ttk.Combobox(l_visStock, font=fontepadrao)
        self.stockVis_add['values'] = ('1.00', '1.25', '1.50', '1.75', '2.00', '2.25', '2.50', '2.75', '3.00', '3.25',
                              '3.50')
        self.stockVis_sphe.place(relx='0.20', rely='0.20', relwidth='0.10', relheight='0.04')
        self.stockVis_cylin.place(relx='0.45', rely='0.20', relwidth='0.10', relheight='0.04')
        self.stockVis_add.place(relx='0.70', rely='0.20', relwidth='0.10', relheight='0.04')

        lista = ttk.Treeview(l_visStock, height=6, columns=('col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7'))
        lista.heading('#0')
        lista.heading('col1', text='Esférico')
        lista.heading('col2', text='Cilíndrico')
        lista.heading('col3', text='Adição')
        lista.heading('col4', text='Olho')
        lista.heading('col5', text='Material')
        lista.heading('col6', text='Laboratório')
        lista.heading('col7', text='Unidade(s)')

        lista.column('#0', width=0)
        lista.column('col1', width=80)
        lista.column('col2', width=80)
        lista.column('col3', width=80)
        lista.column('col4', width=50)
        lista.column('col5', width=180)
        lista.column('col6', width=100)
        lista.column('col7', width=90)

        lista.bind('<Double-1>', self.double_ClickReserv)
        lista.place(relx=0.10, rely=0.30, relwidth=0.80, relheight=0.60)

        button = Button(l_visStock, text='Procurar', font=fontepadrao, bg='#808080', bd='0',
                        activebackgroun='#808080')
        button.bind('<Enter>', self.enter)
        button.bind('<Leave>', self.leave)
        button.place(relx=0.44, rely=0.92, relwidth=0.12, relheight=0.05)

    def double_ClickReserv(self, event=''):
        store_list = ('2064', '1432', '1518', '1744', '1571', '2226')
        fontepadrao = ("Verdana", 10, 'bold')
        double_frame = Frame(self.l_visStock, bd=-4, bg="#C0C0C0", highlightbackground="#1c1c1c",
                             highlightthickness=2)
        double_frame.place(relx=0.40, rely=0.50, relwidth=0.20, relheight=0.20)
        label_reserv = Label(double_frame, text='Reservar', font=fontepadrao, bg='#C0C0C0')
        label_reserv.place(relx=0.05, rely=0.045, relwidth=0.90, relheight=0.15)

        label_store = Label(double_frame, text='Loja', font=fontepadrao, bg='#C0C0C0')
        label_store.place(relx=0.05, rely=0.48, relwidth=0.90, relheight=0.15)

        self.unit = ttk.Combobox(double_frame, font=fontepadrao)
        self.unit['values'] = ('1', '2', '3', '4', '5')
        self.unit.bind('<Return>')
        self.unit.place(relx=0.20, rely=0.23, relwidth=0.60, relheight=0.19)

        self.store_Reserv = ttk.Combobox(double_frame, font=fontepadrao)
        self.store_Reserv['values'] = store_list
        self.store_Reserv.bind('<Return>')
        self.store_Reserv.place(relx=0.20, rely=0.68, relwidth=0.60, relheight=0.19)

    def exit_lens(self):
        store_list = ('2064', '1432', '1518', '1744', '1571', '2226')
        fontepadrao = ("Verdana", 10, 'bold')
        frame_layout = Frame(self.f_layout, bg='#808080')
        frame_layout.place(relx='0.145', rely='0.005', relwidth='0.855', relheight='0.99')

        l_visStock = Frame(frame_layout, bd=-10, bg="#C0C0C0", highlightbackground="#1c1c1c", highlightthickness=2)
        l_visStock.place(relx='0.10', rely='0.00', relwidth='0.80', relheight='1.00')

        title = Label(l_visStock, text='RETIRAR LENTES', bg='#C0C0C0')
        title['font'] = ('Verdana', 14)
        title.place(relx='0.10', rely='0.015', relwidth='0.80', relheight='0.05')

        codBarras = Label(l_visStock, text='Cód. De Barras:', font=fontepadrao, bg='#C0C0C0')
        store_Exit = Label(l_visStock, text='Loja:', font=fontepadrao, bg='#C0C0C0')
        seq_Exit = Label(l_visStock, text='Sequência:', font=fontepadrao, bg='#C0C0C0')
        reason_Exit = Label(l_visStock, text='Motivo:', font=fontepadrao, bg='#C0C0C0')
        # ENTRYS
        self.codBarrasEntry_Exit = Entry(l_visStock, font=fontepadrao, bg='white')
        self.codBarrasEntry_Exit.bind("<Return>")

        self.storeEntry_Exit = ttk.Combobox(l_visStock, font=fontepadrao)
        self.storeEntry_Exit['values'] = store_list
        self.storeEntry_Exit.bind("<Return>")

        self.seqEntry_Exit = Entry(l_visStock, font=fontepadrao, bg='white')
        self.seqEntry_Exit.bind("<Return>")

        self.reasonEntry_Exit = ttk.Combobox(l_visStock, font=fontepadrao)
        self.reasonEntry_Exit['values'] = ('Montagem', 'Garantia', 'Quebra')
        self.reasonEntry_Exit.current(0)
        self.reasonEntry_Exit.bind("<Return>")
        # PLACES ENTRYS E LABELS
        store_Exit.place(relx=0.35, rely=0.10, relwidth=0.05, relheight=0.04)
        seq_Exit.place(relx=0.35, rely=0.17, relwidth=0.10, relheight=0.04)
        reason_Exit.place(relx=0.35, rely=0.24, relwidth=0.07, relheight=0.04)
        codBarras.place(relx=0.35, rely=0.31, relwidth=0.13, relheight=0.04)

        self.storeEntry_Exit.place(relx=0.50, rely=0.10, relwidth=0.11, relheight=0.04)
        self.seqEntry_Exit.place(relx=0.50, rely=0.17, relwidth=0.11, relheight=0.04)
        self.reasonEntry_Exit.place(relx=0.50, rely=0.24, relwidth=0.11, relheight=0.04)
        self.codBarrasEntry_Exit.place(relx=0.50, rely=0.31, relwidth=0.20, relheight=0.04)

        lista = ttk.Treeview(l_visStock, height=6, columns=('col1', 'col2', 'col3', 'col4', 'col5', 'col6'))
        lista.heading('#0')
        lista.heading('col1', text='Esférico')
        lista.heading('col2', text='Cilíndrico')
        lista.heading('col3', text='Adição')
        lista.heading('col4', text='Loja')
        lista.heading('col5', text='Sequência')
        lista.heading('col6', text='Motivo')

        lista.column('#0', width=0)
        lista.column('col1', width=80)
        lista.column('col2', width=80)
        lista.column('col3', width=80)
        lista.column('col4', width=50)
        lista.column('col5', width=180)
        lista.column('col6', width=100)

        lista.bind('<Double-1>', self.double_ClickReserv)
        lista.place(relx=0.10, rely=0.42, relwidth=0.80, relheight=0.48)

        button = Button(l_visStock, text='Retirar', font=fontepadrao, bg='#808080', bd='0',
                        activebackgroun='#808080')
        button.bind('<Enter>', self.enter)
        button.bind('<Leave>', self.leave)
        button.place(relx=0.44, rely=0.92, relwidth=0.12, relheight=0.05)

    def vis_reg(self):
        store_list = ('2064', '1432', '1518', '1744', '1571', '2226')
        fontepadrao = ("Verdana", 10, 'bold')
        frame_layout = Frame(self.f_layout, bg='#808080')
        frame_layout.place(relx='0.145', rely='0.005', relwidth='0.855', relheight='0.99')

        l_vis = Frame(frame_layout, bd=-10, bg="#C0C0C0", highlightbackground="#1c1c1c", highlightthickness=2)
        l_vis.place(relx='0.10', rely='0.00', relwidth='0.80', relheight='1.00')

        title = Label(l_vis, text='REGISTRO DE SAÍDA DE LENTES ', bg='#C0C0C0')
        title['font'] = ('Verdana', 14)
        title.place(relx='0.10', rely='0.015', relwidth='0.80', relheight='0.05')

        data_Inicio = Label(l_vis, text='Data Início:', font=fontepadrao, bg='#C0C0C0')
        data_Fim = Label(l_vis, text='Data Fim:', font=fontepadrao, bg='#C0C0C0')
        store_Reg = Label(l_vis, text='Loja:', font=fontepadrao, bg='#C0C0C0')
        # ENTRYS
        self.data_InicioEntry = Entry(l_vis, font=fontepadrao, bg='white')
        self.data_InicioEntry.bind("<Return>")
        self.data_FimEntry = Entry(l_vis, font=fontepadrao, bg='white')
        self.data_FimEntry.bind("<Return>")
        self.store_RegEntry = ttk.Combobox(l_vis, font=fontepadrao)
        self.store_RegEntry['values'] = store_list
        self.store_RegEntry.bind("<Return>")
        # LOCALIZAÇÃO DAS LABELS
        data_Inicio.place(relx=0.10, rely=0.10, relwidth=0.10, relheight=0.045)
        data_Fim.place(relx=0.42, rely=0.10, relwidth=0.09, relheight=0.045)
        store_Reg.place(relx=0.74, rely=0.10, relwidth=0.05, relheight=0.045)
        # LOCALIZAÇÃO DAS ENTRYS
        self.data_InicioEntry.place(relx=0.20, rely=0.10, relwidth=0.17, relheight=0.045)
        self.data_FimEntry.place(relx=0.508, rely=0.10, relwidth=0.17, relheight=0.045)
        self.store_RegEntry.place(relx=0.79, rely=0.10, relwidth=0.11, relheight=0.045)

        listaReg = ttk.Treeview(l_vis, height=6, columns=('col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7',
                                                          'col8', 'col9', 'col10'))
        listaReg.heading('#0')
        listaReg.heading('col1', text='Data')
        listaReg.heading('col2', text='Esférico')
        listaReg.heading('col3', text='Cilindro')
        listaReg.heading('col4', text='Adição')
        listaReg.heading('col5', text='Olho')
        listaReg.heading('col6', text='Material')
        listaReg.heading('col7', text='Laboratório')
        listaReg.heading('col8', text='Loja')
        listaReg.heading('col9', text='Sequência')
        listaReg.heading('col10', text='Motivo')

        listaReg.column('#0', width=0)
        listaReg.column('col1', width=40)
        listaReg.column('col2', width=5)
        listaReg.column('col3', width=5)
        listaReg.column('col4', width=5)
        listaReg.column('col5', width=5)
        listaReg.column('col6', width=60)
        listaReg.column('col7', width=40)
        listaReg.column('col8', width=20)
        listaReg.column('col9', width=20)
        listaReg.column('col10', width=50)

        listaReg.place(relx=0.01, rely=0.25, relwidth=0.98, relheight=0.65)

        button = Button(l_vis, text='Buscar', font=fontepadrao, bg='#808080', bd='0', activebackgroun='#808080')
        button.bind('<Enter>', self.enter)
        button.bind('<Leave>', self.leave)
        button.place(relx=0.44, rely=0.92, relwidth=0.12, relheight=0.05)

    def vis_reserve(self):
        store_list = ('2064', '1432', '1518', '1744', '1571', '2226')
        fontepadrao = ("Verdana", 10, 'bold')
        frame_layout = Frame(self.f_layout, bg='#808080')
        frame_layout.place(relx='0.145', rely='0.005', relwidth='0.855', relheight='0.99')

        l_vis = Frame(frame_layout, bd=-10, bg="#C0C0C0", highlightbackground="#1c1c1c", highlightthickness=2)
        l_vis.place(relx='0.10', rely='0.00', relwidth='0.80', relheight='1.00')

        title = Label(l_vis, text='RESERVAS', bg='#C0C0C0')
        title['font'] = ('Verdana', 14)
        title.place(relx='0.10', rely='0.015', relwidth='0.80', relheight='0.05')

        store = Label(l_vis, text='Loja:', font=fontepadrao, bg='#C0C0C0')
        store.place(relx='0.42', rely='0.10', relwidth='0.06', relheight='0.04')
        self.stReserv_Enter = ttk.Combobox(l_vis, font=fontepadrao)
        self.stReserv_Enter['values'] = store_list
        self.stReserv_Enter.place(relx='0.48', rely='0.10', relwidth='0.10', relheight='0.04')

        listRes = ttk.Treeview(l_vis, height=6, columns=('col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7'))
        listRes.heading('#0')
        listRes.heading('col1', text='Data')
        listRes.heading('col2', text='Esférico')
        listRes.heading('col3', text='Cilindro')
        listRes.heading('col4', text='Adição')
        listRes.heading('col5', text='Olho')
        listRes.heading('col6', text='Material')
        listRes.heading('col7', text='Laboratório')

        listRes.column('#0', width=0)
        listRes.column('col1', width=40)
        listRes.column('col2', width=5)
        listRes.column('col3', width=5)
        listRes.column('col4', width=5)
        listRes.column('col5', width=5)
        listRes.column('col6', width=90)
        listRes.column('col7', width=90)

        listRes.place(relx=0.01, rely=0.25, relwidth=0.98, relheight=0.65)

        button = Button(l_vis, text='Buscar', font=fontepadrao, bg='#808080', bd='0', activebackgroun='#808080')
        button.bind('<Enter>', self.enter)
        button.bind('<Leave>', self.leave)
        button.place(relx=0.44, rely=0.92, relwidth=0.12, relheight=0.05)

    def enter(self, event):
        event.widget.config(relief=GROOVE)

    def leave(self, event):
        event.widget.config(relief=RAISED)


FullScreen()
