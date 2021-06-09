import datetime
from tkinter import *
from tkinter import ttk
import mysql.connector

print('\033[31mRODANDO O PROGRAMA!\033[m')

root = Tk()

# ===========================//=======================/BACK END/======================//================================
class Funcs():
    def date_Today(self):
        from datetime import date
        self.date = date.today()

    def date_hour(self):
        from datetime import datetime
        date_time = datetime.now()
        self.current_date = date_time.strftime('%Y-%m-%d %H:%M')

    def connect_BD(self):
        try:
            self.conn = mysql.connector.connect(host='mysqlserver.cz1ji5phheqm.us-east-2.rds.amazonaws.com',
                                                user='Lab_carolSL', password='mb028001', database="lab_carol")
            self.cursor = self.conn.cursor()
            print('Conectado no BD')
        except mysql.connector.errors.ProgrammingError:  # AJUSTAR EXCESSÃO DE ERRO
            print('\033[31mErro ao conectar no BD!\033[m')

# ==========================//====================/LIMPEZA DE ENTRYS/====================//=============================

    def clear(self): # LIMPA AS ENTRYS DO REGISTRO DE LENTES
        self.codigo_Capt = self.codBarrasEntry.delete(0, END)
        self.sphe_Capt = self.sphe_Entry.delete(0, END)
        self.cylin_Capt = self.cylin_Entry.delete(0, END)
        self.add_Capt = self.add_Entry.delete(0, END)
        self.eye_Capt = self.eye_Entry.delete(0, END)
        self.lab = self.lab_Entry.delete(0, END)
        self.mat_Capt = self.mat_Entry.delete(0, END)

    def clear_Exit(self):  # LIMPA AS ENTRYS DA REMOÇÃO DE LENTES
        self.codRemove_Capt = self.codBarrasEntry_Exit.delete(0, END)
        #self.store_Capt = self.storeEntry_Exit.delete(0, END)
        #self.seq_Capt = self.seqEntry_Exit.delete(0, END)

    def clear_dadosVis(self):  # LIMPA OS DADOS DA VISUALIZAÇÃO DE LENTES
        self.spheClear_CaptVis = self.sphe_VisEntry.delete(0,END)
        self.cylinClear_CaptVis = self.cylin_VisEntry.delete(0,END)
        self.addClear_CaptVis = self.add_VisEntry.delete(0, END)

    def clear_dadosRegServiço(self):  # LIMPA OS DADOS DO REGISTRO DE SERVIÇOS
        if self.verif:
            self.seq_RegServiceEntryRem = self.seq_RegServiceEntry.delete(0,END)
            self.tipo_RegServiceEntryRem = self.tipo_RegServiceEntry.delete(0, END)
            self.prevDay_RegServiceEntryRem = self.prevDay_RegServiceEntry.delete(0,END)

    def clear_listService(self):  # LIMPA OS DADOS DA LISTA DE SERVIÇOS
        self.seq_serviceEntryRem = self.seq_serviceEntry.delete(0, END)
        self.type_serviceEntryRem = self.type_serviceEntry.delete(0, END)

# ==========================//====================/CAPTURA DE DADOS/====================//=============================

    def captura_dados(self):  # CAPTURA DADOS DAS ENTRYS DE CADASTRO DE LENTES
        self.codigo_Capt = self.codBarrasEntry.get()
        self.sphe_Capt = self.sphe_Entry.get()
        self.cylin_Capt = self.cylin_Entry.get()
        self.add_Capt = self.add_Entry.get()
        self.eye_Capt = self.eye_Entry.get()
        self.lab_Capt = self.lab_Entry.get()
        self.mat_Capt = self.mat_Entry.get()

    def captura_dadosRemove(self):  # CAPTURA DE DADOS DAS ENTRYS DE REMOVER LENTES
        self.codRemove_Capt = self.codBarrasEntry_Exit.get()
        self.store_Capt = self.storeEntry_Exit.get()
        self.seq_Capt = self.seqEntry_Exit.get()
        self.reason_Capt = self.reasonEntry_Exit.get()

    def captura_dadosVis(self):  # CAPTURA DE DADOS DAS ENTRYS DE VISUALIZAR LENTES
        self.sphe_CaptVis = self.sphe_VisEntry.get()
        self.cylin_CaptVis = self.cylin_VisEntry.get()
        self.add_CaptVis = self.add_VisEntry.get()

    def captura_dadosLensZero(self):  # CAPTURA DADOS DAS ENTRYS DE VISUALIZAR LENTES ZERADAS
        self.spheMax_LensZeroCapt = self.spheMax_LensZero.get()
        self.spheMin_LensZeroCapt = self.spheMin_LensZero.get()
        self.cylinEntry_LensZeroCapt = self.cylinEntry_LensZero.get()
        self.matEntry_LensZeroCapt =  self.matEntry_LensZero.get()
        self.labEntry_LensZeroCapt = self.labEntry_LensZero.get()

    def captura_dadosRegSaida(self):  # CAPTURA DE DADOS DAS ENTRYS DE REGISTRAR SAÍDA DE LENTES
        self.data_InicioEntryCapt = self.data_InicioEntry.get()
        self.data_FimEntryCapt = self.data_FimEntry.get()
        self.store_RegEntryCapt = self.store_RegEntry.get()
        if self.data_InicioEntryCapt == '' or self.data_FimEntryCapt == '' or self.store_RegEntryCapt == '':
            self.text_warning = 'PREENCHA TODOS OS CAMPOS'
            self.warning()
        else:
            self.text_warning = ''
            self.warning()

    def captura_dadosRegServico(self):  # CAPTURA OS DADOS DAS ENTRYS DO REGISTRO DE SERVIÇOS
        verif = []
        self.store_RegServiceEntryCapt = str(self.store_RegServiceEntry.get()).strip()
        self.seq_RegServiceEntryCapt = str(self.seq_RegServiceEntry.get()).strip()
        self.tipo_RegServiceEntryCapt = str(self.tipo_RegServiceEntry.get()).strip()
        self.sit_RegServiceEntryCapt = str(self.sit_RegServiceEntry.get()).strip()
        self.prevDay_RegServiceEntryCapt = str(self.prevDay_RegServiceEntry.get()).strip()
        self.prevMonth_RegServiceEntryCapt = str(self.prevMonth_RegServiceEntry.get()).strip()
        self.prevYear_RegServiceEntryCapt = str(self.prevYear_RegServiceEntry.get()).strip()
        verif.append(self.store_RegServiceEntryCapt)
        verif.append(self.seq_RegServiceEntryCapt)
        verif.append(self.sit_RegServiceEntryCapt)
        verif.append(self.prevDay_RegServiceEntryCapt)
        verif.append(self.prevMonth_RegServiceEntryCapt)
        verif.append(self.prevYear_RegServiceEntryCapt)
        if '' in verif:
            self.text_warning = 'PREENCHA TODOS OS CAMPOS'
            self.warning()
            self.verif = False
        else:
            self.text_warning = 'SERVIÇO ADICIONADO'
            self.warning()
            self.verif = True

    def captura_ListService(self):  # CAPTURA AS ENTRYS DA LISTA DE SERVIÇO
        verif = []
        self.store_serviceEntryCapt = str(self.store_serviceEntry.get()).strip()
        self.seq_serviceEntryCapt = str(self.seq_serviceEntry.get()).strip()
        self.type_serviceEntryCapt = str(self.type_serviceEntry.get()).strip()
        verif.append(self.store_serviceEntryCapt)
        verif.append(self.seq_serviceEntryCapt)
        verif.append(self.type_serviceEntryCapt)
        if '' in verif:
            self.text_warning = 'PREENCHA TODOS OS CAMPOS'
            self.warning()
        else:
            self.type_lens = str(self.type_serviceEntryCapt).upper()
            if self.type_lens == 'VS':
                self.type_lens = 'Visão Simples'
            elif self.type_lens == 'M':
                self.type_lens = 'Multifocal'
            elif self.type_lens == 'B':
                self.type_lens = 'Bifocal'
            else:
                self.text_warning = 'DIGITE O TIPO CORRETO'
                self.warning()
            self.addServiceList()

    def pesq_Capt(self):
        verif = []
        self.store_PesqCapt = self.store_PesqEntry.get()
        self.seq_PesqCapt = self.seq_PesqEntry.get()
        verif.append(self.store_PesqCapt)
        verif.append(self.seq_PesqCapt)
        if '' in verif:
            self.text_warning = 'PREENCHA TODOS OS CAMPOS'
            self.warning()
        else:
            self.pesq_Service()

    def CaptDados_Obs(self):
        self.situationCapt = self.situationEntry.get()
        self.textCapt = self.text.get('1.0', '200.0')

    def CaptDados_Rel(self):
        from datetime import datetime
        verif = []
        self.per_iniEntrycapt = self.per_iniEntry.get()
        self.per_fimEntryCapt = self.per_fimEntry.get()
        verif.append(self.per_iniEntrycapt)
        verif.append(self.per_fimEntryCapt)
        if '' in verif:
            self.text_warning = 'PREENCHA TODOS OS CAMPOS'
            self.warning()
        else:
            self.relatorio()
# ==========================//=====================/MANIPULAÇÃO DE DADOS/==================//===========================

    def verification_Int(self):
        self.captura_dados()
        try:
            validate = str(self.codigo_Capt)
            if validate.isalpha() or validate.isspace():
                self.text_warning = 'DADOS INVÁLIDOS'
                self.warning()
                self.clear()
                print('\033[31mENTRADA DE DADOS INVALIDA NA FUNÇÃO "VERIFICATON_INT"\033[m')
                return False
            else:
                return True
                self.text_warning = ''
                print('Dados aceitos!')
        except (ValueError, TypeError):
            print('\033[31mEntrada Inválida do try\033[m')

    def verification_IntExit(self):
        self.captura_dadosRemove()
        try:
            validate = str(self.codRemove_Capt)
            if validate.isalpha() or validate.isspace():
                self.text_warning = 'DADOS INVÁLIDOS'
                self.warning()
                print('\033[31mENTRADA DE DADOS INVALIDA NA FUNÇÃO "VERIFICATON_INT"\033[m')
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
        self.codigos = []
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"SELECT cod_barras FROM stock ")
        result = self.cursor.fetchall()
        if len(self.codigo_Capt) < 10:
            self.text_warning = 'C. BARRAS MÍNIMO 10 DÍGITOS'
            self.warning()
            print('CÓD. BARRAS MÍNIMO 10 DÍGITOS')
        else:
            for d in result:
                e = d
                for c in e:
                    self.codigos.append(c)

            if int(self.codigo_Capt) in self.codigos:
                self.cursor.execute(f"SELECT amount FROM stock WHERE cod_barras = {self.codigo_Capt}")
                result = self.cursor.fetchone()
                if result is None:
                    result = 0
                else:
                    if result[0] >= int(0):
                        print('\033[31mChamando a função "Register_Cod"!\033[m')
                        self.register_cod()
            else:
                print('Não existe esta lente na base de dados! VERIFICATION CODE'.title())
                self.text_warning = 'CADASTRAR LENTE'
                self.warning()
                self.register_cod()

    def insert_Dados(self, event):  # PARA PREENCHER OS CAMPOS DA FUNÇÃO DE CDASTRO AUTOMATICAMENTE
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

    def register_cod(self):
        try:
            if int(self.codigo_Capt) in self.codigos:  # SE JA EXISTIR O CÓDIGO CADASTRADO
                self.insert_Dados(event='')
                self.cursor.execute(f"UPDATE stock SET amount = amount+{1} WHERE cod_barras = {self.codigo_Capt}")
                self.conn.commit()
                #  ADICIONANDO NA LISTA DE EXIBIÇÃO
                self.cursor.execute(f'SELECT spherical, cylindrical, adicao, eye, material, laboratory, amount '
                                    f'FROM stock WHERE cod_barras = {self.codigo_Capt}')
                lista = self.cursor.fetchall()
                for dado in lista:
                    self.listaCli.insert('', END, values=(dado))
                self.conn.close()
                self.text_warning = 'LENTE ADICIONADA'
                self.warning()
                self.clear()
                print(f'\033[34mLente adicionada com sucesso!\033[m'.title())
            else:
                print('Não existe esta lente na base de dados! REGISTER COD'.title())
                self.text_warning = 'DIGITE LAB. E MATERIAL'
                self.warning()
                self.captura_dados()
                if self.mat_Capt != '':  # SE NÃO EXISTIR O CÓDIGO CADASTRADO
                    print('\033[31mEntrando no cadastro de lentes após o campo material ter sido preenchido!\033[m')
                    self.label_and_entry()
                    self.connect_BD()
                    self.cursor.execute(f"INSERT INTO stock VALUES "
                                        f"('{self.codigo_Capt}', '{self.mat_Capt}', '{self.sphe_Capt}', "
                                        f"'{self.cylin_Capt}', '{self.add_Capt}', '{self.eye_Capt}', "
                                        f"'{self.lab_Capt}', '1' )")
                    self.conn.commit()
                    #  ADICIONANDO NA LISTA DE EXIBIÇÃO
                    self.cursor.execute(f'SELECT spherical, cylindrical, adicao, eye, material, laboratory, amount '
                                        f'FROM stock WHERE cod_barras = {self.codigo_Capt}')
                    lista = self.cursor.fetchall()
                    for dado in lista:
                        self.listaCli.insert('', END, values=(dado))
                    self.conn.close()
                    self.text_warning = 'LENTE CADASTRADA'
                    self.warning()
                    self.clear()
                    print('\033[31mCadastrada Lente Inesistete!\033[m')
        except:
            self.text_warning = 'ERRO AO INSERIR DADOS'
            self.warning()
            print('ERRO AO INICIAR REGISTER COD')

    def option_VisLens(self):
        print("Botão de visualização clicado!".title())
        self.connect_BD()
        self.cursor.execute(f"SELECT spherical, cylindrical, adicao, eye, material, laboratory, "
                            f"amount FROM stock WHERE spherical = '{self.sphe_CaptVis}' AND "
                            f"cylindrical = '{self.cylin_CaptVis}' AND adicao = '{self.add_CaptVis}'")
        lista = self.cursor.fetchall()
        cont = 0
        for dado in lista:
            if dado[-1] != 0:
                cont += 1
                self.listaCli.insert('', END, values=(dado))
        self.conn.close()
        if cont == 0:
            self.text_warning = 'NÃO TEM NO ESTOQUE'
            self.warning()

    def print_RegSaida(self):
        self.connect_BD()
        self.cursor.execute(f"SELECT lens.data, stock.spherical, stock.cylindrical, stock.adicao, stock.eye, "
                            f"stock.material, stock.laboratory, lens.store, lens.sequencia, lens.reason "
                            f"FROM stock JOIN lens ON lens.cod_barras = stock. cod_barras "
                            f"WHERE lens.data BETWEEN '{self.data_InicioEntryCapt}' AND '{self.data_FimEntryCapt}' "
                            f"AND lens.store = '{self.store_RegEntryCapt}' ORDER BY lens.data")
        lista = self.cursor.fetchall()
        if lista == []:
            self.text_warning = 'VERIFIQUE O PERÍODO'
            self.warning()
        else:
            self.listaReg.delete(*self.listaReg.get_children())
            for dado in lista:
                self.listaReg.insert('', END, values=(dado))
        self.conn.close()

    def lensZero(self):
        self.connect_BD()
        self.cursor.execute(f"SELECT spherical, cylindrical, material, laboratory, amount FROM stock "
                            f"WHERE spherical BETWEEN {self.spheMax_LensZeroCapt} AND {self.spheMin_LensZeroCapt} "
                            f"AND cylindrical BETWEEN {self.cylinEntry_LensZeroCapt} AND 0 AND "
                            f"material = '{self.matEntry_LensZeroCapt}' AND laboratory = '{self.labEntry_LensZeroCapt}' "
                            f"AND amount < 2 ORDER BY spherical DESC")
        lista = self.cursor.fetchall()
        self.listaZero.delete(*self.listaZero.get_children())
        for dado in lista:
            self.listaZero.insert('', END, values=(dado))
        self.cursor.close()

    def remove_LensAdd(self):  # FUNÇÃO PARA REMOVER LENTES
        self.verification_IntExit()
        if self.verification_IntExit():
            self.captura_dadosRemove()
            self.connect_BD()
            self.cursor.execute(f"SELECT amount FROM stock WHERE cod_barras = {self.codRemove_Capt}")
            result = self.cursor.fetchone()
            if result is not None and result[0] > 0:
                self.cursor.execute(f"SELECT COUNT(*) FROM reserve WHERE store = '{self.store_Capt}' AND "
                                    f"cod_barras = '{self.codRemove_Capt}'")
                uni = self.cursor.fetchone()
                if uni[0] > 0:  # SE A LENTE ESTIVER RESERVADA
                    self.cursor.execute(f"DELETE FROM reserve WHERE store = '{self.store_Capt}' "
                                        f"AND cod_barras = '{self.codRemove_Capt}' LIMIT 1")
                else:  # SE A LENTE NÃO ESTIVER RESERVADA
                    self.cursor.execute(f"UPDATE stock SET amount = amount-1 WHERE cod_barras = {self.codRemove_Capt}")

                # INSERE NA TABELA DE RETIRADA DE LENTES
                self.cursor.execute(f"INSERT INTO lens VALUES "
                                    f"('0', '{self.date}', '{self.codRemove_Capt}', '{self.store_Capt}', "
                                    f"'{self.seq_Capt}', '{self.reason_Capt}')")
                self.conn.commit()
                dados = (self.codRemove_Capt, self.store_Capt, self.seq_Capt, self.reason_Capt)
                self.lista_Exit.insert('', END, values=(dados))
                self.conn.close()
                self.text_warning = 'LENTE RETIRADA'
                self.warning()
                self.clear_Exit()
                print('\033[31mINSERIDA NA TABELA DE SAÍDA DE LENTES!\033[m')
            else:
                self.text_warning = 'LENTE NÃO EXISTE'
                self.warning()
                print('\033[31mNÃO EXISTE A LENTE NO ESTOQUE\033[m')

    def recording_RegService(self):
        from datetime import datetime
        if self.verif:
            var = [self.prevDay_RegServiceEntryCapt, self.prevMonth_RegServiceEntryCapt,
                   self.prevYear_RegServiceEntryCapt]
            month = {'Janeiro':'01', 'Fevereiro':'02', 'Março':'03', 'Abril':'04', 'Maio':'05', 'Junho':'06',
                     'Julho':'07', 'Agosto' :'08', 'Setembro':'09', 'Outubro':'10', 'Novembro':'11', 'Dezembro':'12'}
            previsao = f"{var[2]}-{month[var[1]]}-{var[0]}"
            data_prev = datetime.strptime(previsao, '%Y-%m-%d').date()
            data_today = self.date
            self.connect_BD()
            if data_prev >= data_today:
                self.cursor.execute(f"SELECT sequencia FROM services WHERE store = '{self.store_RegServiceEntryCapt}' "
                                    f"AND sequencia = '{self.seq_RegServiceEntryCapt}'")
                garantia = f'{self.seq_RegServiceEntryCapt}'
                if '-G' in garantia or '-g' in garantia:
                    self.connect_BD()
                    self.date_hour()
                    self.cursor.execute(f"INSERT INTO services VALUES "
                                        f"('{self.date}', DEFAULT, '{self.current_date}', "
                                        f"'{self.store_RegServiceEntryCapt}', '{self.seq_RegServiceEntryCapt}', "
                                        f"'{self.tipo_RegServiceEntryCapt}', '{self.sit_RegServiceEntryCapt}', "
                                        f"'{previsao}', '', 'Sim', '')")
                    self.conn.commit()
                    self.text_warning = 'GARANTIA ADICIONADA'
                    self.warning()
                    self.clear_dadosRegServiço()
                    self.cursor.execute(f"SELECT data, store, sequencia, tipo, situation, previsao FROM services "
                                        f"WHERE store = {self.store_RegServiceEntryCapt} AND "
                                        f"sequencia = '{self.seq_RegServiceEntryCapt}'")
                    lista = self.cursor.fetchall()
                    for dados in lista:
                        self.listaRegService.insert('', END, values=(dados))
                    self.conn.close()
                else:
                    exist = self.cursor.fetchone()
                    if exist is None:
                        self.date_hour()
                        self.cursor.execute(f"INSERT INTO services VALUES "
                                            f"('{self.date}', DEFAULT, '{self.current_date}', "
                                            f"'{self.store_RegServiceEntryCapt}', '{self.seq_RegServiceEntryCapt}', "
                                            f"'{self.tipo_RegServiceEntryCapt}', '{self.sit_RegServiceEntryCapt}', "
                                            f"'{previsao}', '', DEFAULT, '')")
                        self.conn.commit()
                        self.text_warning = 'SERVIÇO ADICIONADO'
                        self.warning()
                        self.clear_dadosRegServiço()
                        self.cursor.execute(f"SELECT data, store, sequencia, tipo, situation, previsao FROM services "
                                            f"WHERE store = {self.store_RegServiceEntryCapt} AND "
                                            f"sequencia = '{self.seq_RegServiceEntryCapt}'")
                        lista = self.cursor.fetchall()
                        for dados in lista:
                            self.listaRegService.insert('', END, values=(dados))
                    else:
                        self.text_warning = 'SERVIÇO JÁ EXISTE'
                        self.warning()
            else:
                self.text_warning = 'PREVISÃO INVÁLIDA'
                self.warning()
            self.conn.close()

    def addServiceList(self):
        self.connect_BD()
        self.cursor.execute(f"SELECT * FROM services WHERE store = '{self.store_serviceEntryCapt}' AND sequencia = "
                            f"'{self.seq_serviceEntryCapt}' AND tipo = '{self.type_lens}' AND situation = 'Finalizado'")
        verif = self.cursor.fetchall()
        if verif != []:
            self.text_warning= 'SERVIÇO JÁ FINALIZADO'
            self.warning()
        else:
            self.connect_BD()
            self.cursor.execute(f"SELECT * FROM services WHERE store = '{self.store_serviceEntryCapt}' AND "
                                f"sequencia = '{self.seq_serviceEntryCapt}' AND tipo = '{self.type_lens}'")
            verif = self.cursor.fetchall()
            if verif == []:
                self.text_warning = 'SERVIÇO NÃO CADASTRADO'
                self.warning()
            else:
                self.date_hour()
                self.cursor.execute(f"UPDATE services SET data_id = '{self.date}', data = '{self.current_date}', "
                                    f"situation = 'Finalizado', status = 'Em Rota' "
                                    f"WHERE store = '{self.store_serviceEntryCapt}' "
                                    f"AND sequencia = '{self.seq_serviceEntryCapt}' AND tipo = '{self.type_lens}'")
                self.conn.commit()
                self.cursor.execute(f"SELECT store, sequencia, tipo, warrant FROM services WHERE "
                                    f"data_id = '{self.date}' AND "
                                    f"situation = 'Finalizado'")
                lista = self.cursor.fetchall()
                self.listSearchServ.delete(*self.listSearchServ.get_children())
                for val in lista:
                    self.listSearchServ.insert('', END, values=(val))
                self.text_warning = ''
                self.warning()
                self.conn.close()
                self.clear_listService()

    def pesq_Service(self):
        self.connect_BD()
        self.cursor.execute(f"SELECT store, sequencia, data, tipo, situation, previsao, obs, status FROM services WHERE "
                            f"store = '{self.store_PesqCapt}' AND LOCATE('{self.seq_PesqCapt}', sequencia)")
        lista = self.cursor.fetchall()
        if lista == []:
            self.text_warning = 'SERVIÇO NÃO ENCONTRADO'
            self.warning()
        else:
            for val in lista:
                self.listaPesq.insert('',  END, values=(val))
            self.text_warning = ''
            self.warning()
        self.conn.close()

    def cont(self):  # RESOLVENDO O BUG DA CONTAGEM DE SERVIÇOS
        self.connect_BD()
        self.cursor.execute(f"SELECT COUNT(data_id) FROM services WHERE data_id = '{self.date}' "
                            f"AND situation = 'Finalizado'")
        total_day = self.cursor.fetchone()
        self.tot_D = f'{total_day[0]}'
        per_inic = f'{self.date.year}-{self.date.month}-01'
        per_end = f'{self.date.year}-{self.date.month}-{self.date.day}'
        self.cursor.execute(f"SELECT COUNT(data_id) FROM services WHERE data_id BETWEEN '{per_inic}' AND '{per_end}' "
                            f"AND situation = 'Finalizado'")
        total_month = self.cursor.fetchone()
        self.tot_M = f'{total_month[0]}'
        self.conn.close()

    def warning(self):
        self.font_warning = ('Verdana', 20, 'italic', 'bold')
        self.text_warning_Label = Label(self.frame_options, text=self.text_warning, font=self.font_warning,
                                        bg='#f0e68c', fg='red')
        self.text_warning_Label.place(relx=0.05, rely=0.84, relwidth=0.90, relheight=0.08)

    def insert_Obs(self):
        self.listaPesq.selection()
        for dado in self.listaPesq.selection(): # INSERIR DADOS NAS ENTRYS DA OBS
            col1, col2, col3, col4, col5, col6, col7, col8 = self.listaPesq.item(dado, 'values')
            self.col1 = col1
            self.col2 = col2
            self.col4 = col4
            self.situationEntry.insert(END, col5)
            self.text.insert(END, col7)

    def alter_Obs(self, event=''):
        self.CaptDados_Obs()
        self.date_hour()
        self.connect_BD()
        self.cursor.execute(f"UPDATE services SET situation = '{self.situationCapt}', obs = '{self.textCapt}', "
                            f"data = '{self.current_date}' WHERE store = '{self.col1}' AND sequencia = '{self.col2}' "
                            f"AND tipo = '{self.col4}'")
        self.conn.commit()
        self.conn.close()
        self.lista_Pesq()
        self.option_buttonPesqEnter()

    def reserve(self, event=''):
        data = self.date
        self.unitCapt = self.unit.get()
        self.store_ReservCapt = self.store_Reserv.get()
        if self.unitCapt == '':
            self.text_warning = '** DIGITE QUANTAS LENTES **'
            self.warning()
        else:
            uniCapt = True
        if self.store_ReservCapt == '':
            self.text_warning = '** DIGITE A LOJA **'
            self.warning()
        else:
            store = True

        if uniCapt is True and store is True:
            self.listaCli.selection()
            for dado in self.listaCli.selection():
                col1, col2, col3, col4, col5, col6, col7 = self.listaCli.item(dado, 'values')
                sphe = col1  # esférico
                cylin = col2  # cilindro
                add = col3  # adição
                eye = col4  # olho
                mat = col5  # material
                lab = col6  # laboratório
                uni = col7  # unidades
            if int(self.unitCapt) > int(uni):
                self.text_warning = f'* NÃO É POSSÍVEL RESERVAR {self.unitCapt} LENTES! *'
                self.warning()
            else:
                self.text_warning = ''
                self.warning()
                self.connect_BD()
                # BUSCA O CÓDIGO DE BARRAS
                self.cursor.execute(f"SELECT cod_barras FROM stock WHERE spherical = '{sphe}' AND cylindrical = '{cylin}' "
                                    f"AND adicao = '{add}' AND eye = '{eye}' AND material = '{mat}' AND "
                                    f"laboratory = '{lab}'")
                cod_barras = self.cursor.fetchone()
                # RETIRA A LENTE DO ESTOQUE
                self.cursor.execute(f"UPDATE stock SET amount = amount-{self.unitCapt} WHERE spherical = '{sphe}' AND "
                                    f"cylindrical = '{cylin}' AND adicao = '{add}' AND eye = '{eye}' AND "
                                    f"material = '{mat}' AND laboratory = '{lab}'")
                # INSERE NA RESERVA
                for reserve in range(int(self.unitCapt)):
                    self.cursor.execute(f"INSERT INTO reserve VALUES "
                                        f"('{data}', '{self.store_ReservCapt}', '{cod_barras[0]}')")
                self.conn.commit()
                self.conn.close()
                self.Double_frame.destroy()
                self.text_warning = '** RESERVADO **'
                self.warning()

# ==========================//============================/PDF/============================//===========================

    def relatorio(self):
        from reportlab.pdfgen import canvas
        day = datetime.date.today().day
        month = datetime.date.today().month
        year = datetime.date.today().year
        zero_day = '0'
        zero_month = '0'
        if month > 9:
            zero_month = ''
        if day > 9:
            zero_day = ''
        data = f'{zero_day}{day}/{zero_month}{month}/{year}'
        print(data)

        pdf = canvas.Canvas('C:/Users/Public/Documents/Relatorio de Montagem Laboratório.pdf')
        pdf.setFont('Times-Bold', 25)
        # CABEÇALHO
        pdf.setFont('Times-Bold', 25)
        pdf.drawString(200, 810, 'Laboratório Carol')

        meses = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
                 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}
        resp = {2064:'Jéssica', 1432:'Priscila', 2007:'Gisele', 1518:'Carmen', 1571:'Mônica', 1744:'Bruna', 1574:'Aline',
                1648:'Milene', 2226:'Vivi'}

        pdf.setFont('Times-Bold', 20)
        pdf.drawString(90, 760, f"Relatório de montagem referente à {meses[month]} de {year}")

        # >>>>>> ARRUMAR PARA PEGAR A REFERENCIA DA TELA
        # LEVANTANDO DADOS DE MONTAGEM
        lojas = ['2064', '1432', '2007', '1518', '1571', '1744', '1574', '1648', '2226']
        periodo = str(f"'{self.per_iniEntrycapt}' AND '{self.per_fimEntryCapt}'")
        self.connect_BD()
        space = 780
        for loja in lojas:
            space = space - 70
            # TOTAL
            self.cursor.execute(f"SELECT COUNT(*) FROM services WHERE store = '{loja}' AND situation = 'Finalizado' AND "
                                f"data_id BETWEEN {periodo} AND warrant = 'Não'")
            total = self.cursor.fetchone()

            # VS
            self.cursor.execute(f"SELECT COUNT(*) FROM services WHERE store = '{loja}' AND situation = 'Finalizado' AND "
                                f" tipo = 'Visão Simples' AND data_id BETWEEN {periodo} AND warrant = 'Não'")
            vs = self.cursor.fetchone()
            # MULTI
            self.cursor.execute(f"SELECT COUNT(*) FROM services WHERE store = '{loja}' AND situation = 'Finalizado' AND "
                                f" tipo = 'Multifocal' AND data_id BETWEEN {periodo} AND warrant = 'Não'")
            multi = self.cursor.fetchone()
            # GARANTIA
            self.cursor.execute(f"SELECT COUNT(*) FROM services WHERE store = '{loja}' AND situation = 'Finalizado' AND "
                                f" warrant = 'Sim' AND data_id BETWEEN {periodo}")
            warrant = self.cursor.fetchone()

            pdf.setFont('Times-Bold', 16)
            pdf.drawString(50, space, f"Loja: {loja} - Responsável. {resp[int(loja)]}")
            pdf.setFont('Times-Bold', 14)
            pdf.drawString(50, space-20, f"Total: {total[0]} óculos montados.")
            pdf.setFont('Times-Bold', 14)
            pdf.drawString(50, space-35, f"{vs[0]} Visão Simples.  {multi[0]} Multifocais.  {warrant[0]} Garantia(s).")

        # TOTAL DE MONTAGENS
        self.cursor.execute(f"SELECT COUNT(*) FROM services WHERE situation = 'Finalizado' AND warrant = 'Não' AND "
                            f"data_id BETWEEN {periodo}")
        tot_mes = self.cursor.fetchone()
        # GARANTIAS
        self.cursor.execute(f"SELECT COUNT(*) FROM services WHERE situation = 'Finalizado' AND warrant = 'Sim' AND "
                            f"data_id BETWEEN {periodo}")
        tot_gar = self.cursor.fetchone()
        pdf.setFont('Times-Bold', 20)
        pdf.drawString(100, 50, f"Total de montagens no mês de {meses[month]}:")
        pdf.setFont('Times-Bold', 16)
        pdf.drawString(100, 30, f"{tot_mes[0]} Montagens e {tot_gar[0]} Garantias")

        # RODAPE
        pdf.setFont('Times-Bold', 9)
        pdf.drawString(30, 5, f"Relatório gerado automaticamente pelo Sistema de Gestão de Laboratório de Montagem.")
        pdf.drawString(525, 5, data)

        self.cursor.close()
        pdf.save()
        self.text_warning = 'RELATÓRIO GERADO'
        self.warning()
        print('Relatorio Gerado com Sucesso!')

# ==========================//============================/LABELS/=========================//===========================

    def label_and_entry(self):
        self.options()
        self.listaFrame()
        self.fontepadrao = ("Verdana", 10, "italic", 'bold')
        #  LABELS
        self.codBarras = Label(self.frame_options, text='Cód. De Barras:', font=self.fontepadrao, bg='#f0e68c')
        self.sphe_degree = Label(self.frame_options, text='Esférico:', font=self.fontepadrao, bg='#f0e68c')
        self.cylin_degree = Label(self.frame_options, text='Cilindrico:', font=self.fontepadrao, bg='#f0e68c')
        self.lab = Label(self.frame_options, text='Laboratório:', font=self.fontepadrao, bg='#f0e68c')
        self.mat = Label(self.frame_options, text='Material:', font=self.fontepadrao, bg='#f0e68c')
        self.add = Label(self.frame_options, text='Adição:', font=self.fontepadrao, bg='#f0e68c')
        self.eye = Label(self.frame_options, text='Olho:', font=self.fontepadrao, bg='#f0e68c')
        #  ESTRADA DE DADOS
        self.codBarrasEntry = Entry(self.frame_options, font=self.fontepadrao, bg='white')
        self.codBarrasEntry.bind("<Return>", self.option_Ir)
        self.sphe_Entry = ttk.Combobox(self.frame_options, font=self.fontepadrao)
        self.sphe_Entry['values'] = ('0.00', '+0.25', '+0.50', '+0.75', '+1.00', '+1.25', '+1.50', '+1.75', '+2.00',
                                        '+2.25', '+2.50', '+2.75', '+3.00', '+3.25', '+3.50', '+3.75', '+4.00',
                                        '-0.25', '-0.50', '-0.75', '-1.00', '-1.25', '-1.50', '-1.75', '-2.00', '-2.25',
                                        '-2.50', '-2.75', '-3.00', '-3.25', '-3.50', '-3.75', '-4.00')
        self.sphe_Entry.bind("<Return>", self.option_Ir)
        self.cylin_Entry = ttk.Combobox(self.frame_options, font=self.fontepadrao)
        self.cylin_Entry['values'] = ('0.00', '-0.25', '-0.50', '-0.75', '-1.00', '-1.25', '-1.50', '-1.75', '-2.00',
                                      '-2.25', '-2.50', '-2.75', '-3.00', '-3.25', '-3.50', '-3.75', '-4.00')
        self.cylin_Entry.bind("<Return>", self.option_Ir)
        self.lab_Entry = ttk.Combobox(self.frame_options, font=self.fontepadrao)
        self.lab_Entry['values'] = ('Farol', 'Haytek', 'Zeiss')
        self.lab_Entry.bind("<Return>", self.option_Ir)
        self.mat_Entry = ttk.Combobox(self.frame_options, font=self.fontepadrao)
        self.mat_Entry['values'] = ('Lente Vis Simples 1.50 c/A.R.', 'Lente Vis Simples 1.56 c/A.R.',
                                    'Lente V.S. 1.56 Filtro Azul c/A.R.', 'Lente Vis Simp 1.59 Poly c/A.R.',
                                    'Lente Vis Simp 1.59 Poly Filtro Azul c/A.R.', 'Lente Ac. Progressiva 1.56 c/A.R.',
                                    'Zeiss 1.50 Platinum', 'Zeiss 1.50 BlueProtect', 'Zeiss 1.50 Silver',
                                    'Zeiss 1.50 Photo')
        self.mat_Entry.bind("<Return>", self.option_Ir)
        self.add_Entry = ttk.Combobox(self.frame_options, font=self.fontepadrao)
        self.add_Entry['values'] = ('1.00', '1.25', '1.50', '1.75', '2.00', '2.25', '2.50', '2.75', '3.00', '3.25',
                                    '3.50')
        self.add_Entry.bind("<Return>", self.option_Ir)
        self.eye_Entry = ttk.Combobox(self.frame_options, font=self.fontepadrao)
        self.eye_Entry['values'] = ('D', 'E')
        self.eye_Entry.bind("<Return>", self.option_Ir)
        #  LOCALIZAÇÃO DAS LABELS
        self.codBarras.place(relx=0.010, rely=0.03, relwidth=0.20, relheight=0.045)
        self.sphe_degree.place(relx=0.44, rely=0.03, relwidth=0.17, relheight=0.045)
        self.cylin_degree.place(relx=0.72, rely=0.03, relwidth=0.14, relheight=0.045)
        self.lab.place(relx=0.01, rely=0.11, relwidth=0.20, relheight=0.045)
        self.mat.place(relx=0.50, rely=0.11, relwidth=0.20, relheight=0.045)
        self.add.place(relx=0.19, rely=0.19, relwidth=0.10, relheight=0.045)
        self.eye.place(relx=0.625, rely=0.19, relwidth=0.15, relheight=0.045)
        #  LOCALIZAÇÃO DAS ENTRY
        self.codBarrasEntry.place(relx=0.22, rely=0.03, relwidth=0.23, relheight=0.045)
        self.sphe_Entry.place(relx=0.59, rely=0.03, relwidth=0.12, relheight=0.045)
        self.cylin_Entry.place(relx=0.86, rely=0.03, relwidth=0.12, relheight=0.045)
        self.lab_Entry.place(relx=0.20, rely=0.11, relwidth=0.30, relheight=0.045)
        self.mat_Entry.place(relx=0.665, rely=0.11, relwidth=0.30, relheight=0.045)
        self.add_Entry.place(relx=0.30, rely=0.19, relwidth=0.08, relheight=0.045)
        self.eye_Entry.place(relx=0.75, rely=0.19, relwidth=0.08, relheight=0.045)

    def label_VisEst(self):  # LABELS E ENTRYS DA FUNÇÃO DE VISUALIZAÇÃO DE LENTES
        # LABELS
        self.fontepadrao = ("Verdana", 10, "italic", 'bold')
        self.sphe_Vis = Label(self.frame_options, text='Esférico:', font=self.fontepadrao, bg='#f0e68c')
        self.cylin_Vis = Label(self.frame_options, text='Cilindro:', font=self.fontepadrao, bg='#f0e68c')
        self.add_Vis = Label(self.frame_options, text='Adição:', font=self.fontepadrao, bg='#f0e68c')
        # ENTRYS
        self.sphe_VisEntry = ttk.Combobox(self.frame_options, font=self.fontepadrao)
        self.sphe_VisEntry['values'] = ('0.00', '+0.25', '+0.50', '+0.75', '+1.00', '+1.25', '+1.50', '+1.75', '+2.00',
                                        '+2.25', '+2.50', '+2.75', '+3.00', '+3.25', '+3.50', '+3.75', '+4.00',
                                        '-0.25', '-0.50', '-0.75', '-1.00', '-1.25', '-1.50', '-1.75', '-2.00', '-2.25',
                                        '-2.50', '-2.75', '-3.00', '-3.25', '-3.50', '-3.75', '-4.00')
        self.sphe_VisEntry.bind("<Return>", self.option_ButtonVis)
        self.cylin_VisEntry = ttk.Combobox(self.frame_options, font=self.fontepadrao)
        self.cylin_VisEntry['values'] = ('0.00', '-0.25', '-0.50', '-0.75', '-1.00', '-1.25', '-1.50', '-1.75', '-2.00',
                                         '-2.25', '-2.50', '-2.75', '-3.00', '-3.25', '-3.50', '-3.75', '-4.00')
        self.cylin_VisEntry.bind("<Return>", self.option_ButtonVis)
        self.add_VisEntry = ttk.Combobox(self.frame_options, font=self.fontepadrao)
        self.add_VisEntry['values'] = ('1.00', '1.25', '1.50', '1.75', '2.00', '2.25', '2.50', '2.75', '3.00', '3.25',
                                       '3.50')
        self.add_VisEntry.bind("<Return>", self.option_ButtonVis)
        # LOCALIZAÇÃO DAS LABELS
        self.sphe_Vis.place(relx=0.08, rely=0.10, relwidth=0.14, relheight=0.045)
        self.cylin_Vis.place(relx=0.358, rely=0.10, relwidth=0.20, relheight=0.045)
        self.add_Vis.place(relx=0.70, rely=0.10, relwidth=0.10, relheight=0.045)
        # LOCALIZAÇÃO DAS ENTRYS
        self.sphe_VisEntry.place(relx=0.21, rely=0.10, relwidth=0.12, relheight=0.045)
        self.cylin_VisEntry.place(relx=0.515, rely=0.10, relwidth=0.12, relheight=0.045)
        self.add_VisEntry.place(relx=0.80, rely=0.10, relwidth=0.10, relheight=0.045)

    def label_LensZero(self):
        # LABELS
        self.fontepadrao = ("Verdana", 10, "italic", 'bold')
        self.sphe_LensZero = Label(self.frame_options, text='Esférico:', font=self.fontepadrao, bg='#f0e68c')
        self.bar_LensZero = Label(self.frame_options, text='/', font=self.fontepadrao, bg='#f0e68c')
        self.cylin_LensZero = Label(self.frame_options, text='Cilíndro:', font=self.fontepadrao, bg='#f0e68c')
        self.mat_LensZero = Label(self.frame_options, text='Material:', font=self.fontepadrao, bg='#f0e68c')
        self.lab_LensZero = Label(self.frame_options, text='Laborátorio:', font=self.fontepadrao, bg='#f0e68c')
        # ENTRYS
        self.spheMax_LensZero = ttk.Combobox(self.frame_options, font=self.fontepadrao)
        self.spheMax_LensZero['values'] = ('-0.25', '-0.50', '-0.75','-1.00', '-1.25', '-1.50', '-1.75', '-2.00',
                                           '-2.25', '-2.50', '-2.75', '-3.00', '-3.25', '-3.50', '-3.75', '-4.00')
        self.spheMax_LensZero.bind("<Return>", self.option_ButtonBuscar)
        self.spheMin_LensZero = ttk.Combobox(self.frame_options, font=self.fontepadrao)
        self.spheMin_LensZero['values'] = ('0.00', '+0.25', '+0.50', '+0.75','+1.00', '+1.25', '+1.50', '+1.75', '+2.00',
                                           '+2.25', '+2.50', '+2.75', '+3.00', '+3.25', '+3.50', '+3.75', '+4.00')
        self.spheMin_LensZero.bind("<Return>", self.option_ButtonBuscar)
        self.cylinEntry_LensZero = ttk.Combobox(self.frame_options, font=self.fontepadrao)
        self.cylinEntry_LensZero['values'] = ('0.00', '-0.25', '-0.50', '-0.75', '-1.00', '-1.25', '-1.50', '-1.75',
                                              '-2.00', '-2.25', '-2.50', '-2.75', '-3.00', '-3.25', '-3.50', '-3.75',
                                              '-4.00')
        self.cylinEntry_LensZero.bind("<Return>", self.option_ButtonBuscar)
        self.matEntry_LensZero = ttk.Combobox(self.frame_options, font=self.fontepadrao)
        self.matEntry_LensZero['values'] = ('Lente Vis Simples 1.50 c/A.R.', 'Lente Vis Simples 1.56 c/A.R.',
                                    'Lente V.S. 1.56 Filtro Azul c/A.R.', 'Lente Vis Simp 1.59 Poly c/A.R.',
                                    'Lente Vis Simp 1.59 Poly Filtro Azul c/A.R.', 'Lente Ac. Progressiva 1.56 c/A.R.',
                                    'Zeiss 1.50 Platinum', 'Zeiss 1.50 BlueProtect', 'Zeiss 1.50 Silver',
                                    'Zeiss 1.50 Photo')
        self.matEntry_LensZero.bind("<Return>", self.option_ButtonBuscar)
        self.labEntry_LensZero = ttk.Combobox(self.frame_options, font=self.fontepadrao)
        self.labEntry_LensZero['values'] = ('Farol', 'Haytek', 'Zeiss')
        self.labEntry_LensZero.bind("<Return>", self.option_ButtonBuscar)
        # LOCALIZAÇÃO DAS LABELS
        self.sphe_LensZero.place(relx=0.17, rely=0.03, relwidth=0.14, relheight=0.045)
        self.bar_LensZero.place(relx=0.43, rely=0.03, relwidth=0.04, relheight=0.045)
        self.cylin_LensZero.place(relx=0.61, rely=0.03, relwidth=0.11, relheight=0.045)
        self.mat_LensZero.place(relx=0.03, rely=0.13, relwidth=0.12, relheight=0.045)
        self.lab_LensZero.place(relx=0.50, rely=0.13, relwidth=0.16, relheight=0.045)
        # LOCALIZAÇÃO DAS ENTRYS
        self.spheMax_LensZero.place(relx=0.305, rely=0.03, relwidth=0.12, relheight=0.045)
        self.spheMin_LensZero.place(relx=0.475, rely=0.03, relwidth=0.12, relheight=0.045)
        self.cylinEntry_LensZero.place(relx=0.73, rely=0.03, relwidth=0.12, relheight=0.045)
        self.matEntry_LensZero.place(relx=0.16, rely=0.13, relwidth=0.30, relheight=0.045)
        self.labEntry_LensZero.place(relx=0.67, rely=0.13, relwidth=0.30, relheight=0.045)

    def label_lensOutput(self):
        self.fontepadrao = ("Verdana", 10, "italic", 'bold')
        # LABELS  >>>>  CÓDIGO, SEQ, MOTIVO, LOJA
        self.codBarras = Label(self.frame_options, text='Cód. De Barras:', font=self.fontepadrao, bg='#f0e68c')
        self.store_Exit = Label(self.frame_options, text='Loja:', font=self.fontepadrao, bg='#f0e68c')
        self.seq_Exit = Label(self.frame_options, text='Sequência:', font=self.fontepadrao, bg='#f0e68c')
        self.reason_Exit = Label(self.frame_options, text='Motivo:', font=self.fontepadrao, bg='#f0e68c')
        # ENTRYS
        self.codBarrasEntry_Exit = Entry(self.frame_options, font=self.fontepadrao, bg='white')
        self.codBarrasEntry_Exit.bind("<Return>", self.option_ButtonExit)
        self.storeEntry_Exit = ttk.Combobox(self.frame_options, font=self.fontepadrao)
        self.storeEntry_Exit['values'] = ('2064', '1432', '2007', '1518', '1571', '1744', '1574', '1648', '2226', 'LAB')
        self.storeEntry_Exit.bind("<Return>", self.option_ButtonExit)
        self.seqEntry_Exit = Entry(self.frame_options, font=self.fontepadrao, bg='white')
        self.seqEntry_Exit.bind("<Return>", self.option_ButtonExit)
        self.reasonEntry_Exit = ttk.Combobox(self.frame_options, font=self.fontepadrao)
        self.reasonEntry_Exit['values'] = ('Montagem', 'Garantia', 'Quebra')
        self.reasonEntry_Exit.current(0)
        self.reasonEntry_Exit.bind("<Return>", self.option_ButtonExit)
        # PLACES ENTRYS E LABELS
        self.codBarrasEntry_Exit.place(relx=0.245, rely=0.03, relwidth=0.23, relheight=0.045)
        self.storeEntry_Exit.place(relx=0.575, rely=0.03, relwidth=0.11, relheight=0.045)
        self.seqEntry_Exit.place(relx=0.86, rely=0.03, relwidth=0.11, relheight=0.045)
        self.reasonEntry_Exit.place(relx=0.45, rely=0.11, relwidth=0.20, relheight=0.045)

        self.codBarras.place(relx=0.02, rely=0.03, relwidth=0.22, relheight=0.045)
        self.store_Exit.place(relx=0.49, rely=0.03, relwidth=0.08, relheight=0.045)
        self.seq_Exit.place(relx=0.70, rely=0.03, relwidth=0.14, relheight=0.045)
        self.reason_Exit.place(relx=0.34, rely=0.11, relwidth=0.10, relheight=0.045)

    def label_RegisSaida(self):
        # LABELS
        self.fontepadrao = ("Verdana", 10, "italic", 'bold')
        self.data_Inicio = Label(self.frame_options, text='Data Início:', font=self.fontepadrao, bg='#f0e68c')
        self.data_Fim = Label(self.frame_options, text='Data Fim:', font=self.fontepadrao, bg='#f0e68c')
        self.store_Reg = Label(self.frame_options, text='Loja:', font=self.fontepadrao, bg='#f0e68c')
        # ENTRYS
        self.data_InicioEntry = Entry(self.frame_options, font=self.fontepadrao, bg='white')
        self.data_InicioEntry.bind("<Return>", self.option_ButtonReg)
        self.data_FimEntry = Entry(self.frame_options, font=self.fontepadrao, bg='white')
        self.data_FimEntry.bind("<Return>", self.option_ButtonReg)
        self.store_RegEntry = ttk.Combobox(self.frame_options, font=self.fontepadrao)
        self.store_RegEntry['values'] = ('2064', '1432', '2007', '1518', '1571', '1744', '1574', '1648', '2226', 'LAB')
        self.store_RegEntry.bind("<Return>", self.option_ButtonReg)
        # LOCALIZAÇÃO DAS LABELS
        self.data_Inicio.place(relx=0.02, rely=0.03, relwidth=0.17, relheight=0.045)
        self.data_Fim.place(relx=0.41, rely=0.03, relwidth=0.16, relheight=0.045)
        self.store_Reg.place(relx=0.77, rely=0.03, relwidth=0.10, relheight=0.045)
        # LOCALIZAÇÃO DAS ENTRYS
        self.data_InicioEntry.place(relx=0.19, rely=0.03, relwidth=0.17, relheight=0.045)
        self.data_FimEntry.place(relx=0.56, rely=0.03, relwidth=0.17, relheight=0.045)
        self.store_RegEntry.place(relx=0.86, rely=0.03, relwidth=0.11, relheight=0.045)

    def label_RegService(self):
        self.fontepadrao = ("Verdana", 10, "italic", 'bold')
        # LABELS
        self.store_RegService = Label(self.frame_options, text='Loja:', font=self.fontepadrao, bg='#f0e68c')
        self.seq_RegService = Label(self.frame_options, text='Sequência:', font=self.fontepadrao, bg='#f0e68c')
        self.tipo_RegService = Label(self.frame_options, text='Tipo:', font=self.fontepadrao, bg='#f0e68c')
        self.sit_RegService = Label(self.frame_options, text='Situação:', font=self.fontepadrao, bg='#f0e68c')
        self.prev_RegService = Label(self.frame_options, text='Previsão:', font=self.fontepadrao, bg='#f0e68c')
        self.prevDay_RegService = Label(self.frame_options, text='Dia', font=self.fontepadrao, bg='#f0e68c')
        self.prevMonth_RegService = Label(self.frame_options, text='Mês', font=self.fontepadrao, bg='#f0e68c')
        self.prevYear_RegService = Label(self.frame_options, text='Ano', font=self.fontepadrao, bg='#f0e68c')
        # ENTRYS
        self.store_RegServiceEntry = ttk.Combobox(self.frame_options, font=self.fontepadrao)
        self.store_RegServiceEntry['values'] = ('2064', '1432', '2007', '1518', '1571', '1744', '1574', '1648', '2226')
        self.store_RegServiceEntry.bind("<Return>", self.option_RegServiceEnter)
        self.seq_RegServiceEntry = Entry(self.frame_options, font=self.fontepadrao, bg='white')
        self.seq_RegServiceEntry.bind("<Return>", self.option_RegServiceEnter)
        self.tipo_RegServiceEntry = ttk.Combobox(self.frame_options, font=self.fontepadrao)
        self.tipo_RegServiceEntry['values'] = ('Visão Simples', 'Multifocal', 'Bifocal')
        self.tipo_RegServiceEntry.bind("<Return>", self.option_RegServiceEnter)
        self.sit_RegServiceEntry = ttk.Combobox(self.frame_options, font=self.fontepadrao)
        self.sit_RegServiceEntry['values'] = ('Digitação', 'Aguardando', 'Montagem', 'Finalizado', 'Retrabalho')
        self.sit_RegServiceEntry.current(1)
        self.sit_RegServiceEntry.bind("<Return>", self.option_RegServiceEnter)
        self.prevDay_RegServiceEntry = ttk.Combobox(self.frame_options, font=self.fontepadrao)
        self.prevDay_RegServiceEntry['values'] = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11',
                                                  '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22',
                                                  '23', '24', '25', '26', '27', '28', '29', '30', '31')
        self.prevDay_RegServiceEntry.bind("<Return>", self.option_RegServiceEnter)
        self.barra_of_date1 = Label(self.frame_options, text='Cód. De Barras:', font=self.fontepadrao, bg='#f0e68c')
        self.prevMonth_RegServiceEntry = ttk.Combobox(self.frame_options, font=self.fontepadrao)
        self.prevMonth_RegServiceEntry['values'] = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
                                                    'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
        self.prevMonth_RegServiceEntry.bind("<Return>", self.option_RegServiceEnter)
        self.barra_of_date2 = Label(self.frame_options, text='Cód. De Barras:', font=self.fontepadrao, bg='#f0e68c')
        self.prevYear_RegServiceEntry = ttk.Combobox(self.frame_options, font=self.fontepadrao)
        self.prevYear_RegServiceEntry['values'] = ('2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027',
                                                   '2028', '2029', '2030')
        self.prevYear_RegServiceEntry.current(1)
        self.prevYear_RegServiceEntry.bind("<Return>", self.option_RegServiceEnter)
        #  LOCALIZAÇÃO DAS LABELS
        self.store_RegService.place(relx=0.06, rely=0.03, relwidth=0.07, relheight=0.045)
        self.seq_RegService.place(relx=0.33, rely=0.03, relwidth=0.15, relheight=0.045)
        self.tipo_RegService.place(relx=0.63, rely=0.03, relwidth=0.12, relheight=0.045)
        self.sit_RegService.place(relx=0.06, rely=0.13, relwidth=0.12, relheight=0.045)
        self.prev_RegService.place(relx=0.45, rely=0.13, relwidth=0.12, relheight=0.045)
        self.prevDay_RegService.place(relx=0.57, rely=0.09, relwidth=0.10, relheight=0.045)
        self.prevMonth_RegService.place(relx=0.705, rely=0.09, relwidth=0.10, relheight=0.045)
        self.prevYear_RegService.place(relx=0.84, rely=0.09, relwidth=0.10, relheight=0.045)
        #  LOCALIZAÇÃO DAS ENTRYS
        self.store_RegServiceEntry.place(relx=0.135, rely=0.03, relwidth=0.12, relheight=0.045)
        self.seq_RegServiceEntry.place(relx=0.48, rely=0.03, relwidth=0.11, relheight=0.045)
        self.tipo_RegServiceEntry.place(relx=0.73, rely=0.03, relwidth=0.21, relheight=0.045)
        self.sit_RegServiceEntry.place(relx=0.185, rely=0.13, relwidth=0.20, relheight=0.045)
        self.prevDay_RegServiceEntry.place(relx=0.58, rely=0.13, relwidth=0.08, relheight=0.045)
        self.prevMonth_RegServiceEntry.place(relx=0.663, rely=0.13, relwidth=0.175, relheight=0.045)
        self.prevYear_RegServiceEntry.place(relx=0.84, rely=0.13, relwidth=0.10, relheight=0.045)

    def label_services(self):
        # LABELS
        self.fontepadrao = ("Verdana", 10, "italic", 'bold')
        self.store_service = Label(self.frame_services, text='Loja:', font=self.fontepadrao, bg='#ffd700')
        self.seq_service = Label(self.frame_services, text='Sequência:', font=self.fontepadrao, bg='#ffd700')
        self.type_service = Label(self.frame_services, text='Tipo:', font=self.fontepadrao, bg='#ffd700')
        # ENTRYS
        self.store_serviceEntry = ttk.Combobox(self.frame_services, font=self.fontepadrao)
        self.store_serviceEntry['values'] = ('2064', '1432', '2007', '1518', '1571', '1744', '1574', '1648', '2226')
        self.store_serviceEntry.bind("<Return>", self.option_AddService)
        self.seq_serviceEntry = Entry(self.frame_services, font=self.fontepadrao, bg='white')
        self.seq_serviceEntry.bind("<Return>", self.option_AddService)
        self.type_serviceEntry = Entry(self.frame_services, font=self.fontepadrao, bg='white')
        self.type_serviceEntry.bind("<Return>", self.option_AddService)
        # LOCALIZAÇÃO DAS LABELS
        self.store_service.place(relx=0.03, rely=0.02, relwidth=0.08, relheight=0.035)
        self.seq_service.place(relx=0.30, rely=0.02, relwidth=0.16, relheight=0.035)
        self.type_service.place(relx=0.80, rely=0.02, relwidth=0.08, relheight=0.035)
        # LOCALIZAÇÃO DAS ENTRYS
        self.store_serviceEntry.place(relx=0.11, rely=0.02, relwidth=0.12, relheight=0.035)
        self.seq_serviceEntry.place(relx=0.46, rely=0.02, relwidth=0.28, relheight=0.035)
        self.type_serviceEntry.place(relx=0.88, rely=0.02, relwidth=0.08, relheight=0.035)

    def label_Pesq(self):
        self.fontepadrao = ("Verdana", 10, "italic", 'bold')
        # LABELS
        self.store_Pesq = Label(self.frame_options, text='Loja:', font=self.fontepadrao, bg='#f0e68c')
        self.seq_Pesq = Label(self.frame_options, text='Sequência:', font=self.fontepadrao, bg='#f0e68c')
        # ENTRYS
        self.store_PesqEntry = ttk.Combobox(self.frame_options, font=self.fontepadrao)
        self.store_PesqEntry['values'] = ('2064', '1432', '2007', '1518', '1571', '1744', '1574', '1648', '2226')
        self.store_PesqEntry.bind("<Return>", self.option_buttonPesqEnter)
        self.seq_PesqEntry = Entry(self.frame_options, font=self.fontepadrao, bg='white')
        self.seq_PesqEntry.bind("<Return>", self.option_buttonPesqEnter)
        # LOCALIZAÇÃO DAS LABELS
        self.store_Pesq.place(relx=0.115, rely=0.07, relwidth=0.07, relheight=0.045)
        self.seq_Pesq.place(relx=0.50, rely=0.07, relwidth=0.15, relheight=0.045)
        # LOCALIZAÇÃO DAS ENTRYS
        self.store_PesqEntry.place(relx=0.188, rely=0.07, relwidth=0.12, relheight=0.045)
        self.seq_PesqEntry.place(relx=0.65, rely=0.07, relwidth=0.22, relheight=0.045)

    def label_Cont(self):
        self.fontepadrao = ("Verdana", 10, "italic", 'bold')
        self.cont_Day = Label(self.frame_services, text='Dia:', font=self.fontepadrao, bg='#ffd700')
        self.total_Day = Label(self.frame_services, text=self.tot_D, font=self.fontepadrao, bg='#ffd700', fg='#0000cd')
        self.cont_Month = Label(self.frame_services, text='Mês:', font=self.fontepadrao, bg='#ffd700')
        self.total_Month = Label(self.frame_services, text=self.tot_M, font=self.fontepadrao, bg='#ffd700', fg='#0000cd')
        self.cont_Day.place(relx=0.022, rely=0.945, relwidth=0.06, relheight=0.045)
        self.cont_Month.place(relx=0.80, rely=0.945, relwidth=0.07, relheight=0.045)
        self.total_Day.place(relx=0.08, rely=0.945, relwidth=0.06, relheight=0.045)
        self.total_Month.place(relx=0.875, rely=0.945, relwidth=0.10, relheight=0.045)

    def labelAlter_Status(self):
        self.fontepadrao = ("Verdana", 10, "italic", 'bold')
        # LABELS
        self.situation = Label(self.frame_Obs, text='Situação:', bg='#f0e68c', fg='black', font=self.fontepadrao)
        self.situation.place(relx=0.10, rely=0.09, relwidth=0.14, relheight=0.14)
        self.observation = Label(self.frame_Obs, text='Observação', bg='#ffd700', fg='black', font=self.fontepadrao)
        self.observation.place(relx=0.42, rely=0.30, relwidth=0.20, relheight=0.14)
        # ENTRYS
        self.situationEntry = ttk.Combobox(self.frame_Obs, font=self.fontepadrao)
        self.situationEntry['values'] = ('Digitação', 'Aguardando', 'Montagem', 'Finalizado', 'Retrabalho')
        self.situationEntry.place(relx=0.24, rely=0.09, relwidth=0.23, relheight=0.14)
        self.situationEntry.bind("<Return>", self.alter_Obs)

        self.text = Text(self.frame_Obs, font=self.fontepadrao, bg='white', highlightbackground="#1c1c1c",
                                   highlightthickness=1)
        self.text.place(relx=0.02, rely=0.30, relwidth=0.96, relheight=0.62)

    def label_Rel(self):
        self.options()
        self.fontepadrao = ("Verdana", 10, "italic", 'bold')
        # LABELS
        self.per_ini = Label(self.frame_options, text='Data Início:', bg='#f0e68c', fg='black', font=self.fontepadrao)
        self.per_fim = Label(self.frame_options, text='Data Fim:', bg='#f0e68c', fg='black', font=self.fontepadrao)
        # ENTRYS
        self.per_iniEntry = Entry(self.frame_options, font=self.fontepadrao)
        self.per_iniEntry.bind('<Return>', self.option_EnterRel)
        self.per_fimEntry = Entry(self.frame_options, font=self.fontepadrao)
        self.per_fimEntry.bind('<Return>', self.option_EnterRel)
        # LACOALIZAÇÃO
        self.per_ini.place(relx=0.103, rely=0.03, relwidth=0.17, relheight=0.045)
        self.per_fim.place(relx=0.549, rely=0.03, relwidth=0.17, relheight=0.045)
        self.per_iniEntry.place(relx=0.265, rely=0.03, relwidth=0.17, relheight=0.045)
        self.per_fimEntry.place(relx=0.70, rely=0.03, relwidth=0.17, relheight=0.045)

    def double_ClickReserv(self, event=''):
        fonte_DoubleClick = ("Verdana", 12, "italic", 'bold')
        self.Double_frame = Frame(self.frame_options, bd=-4, bg="#ffd700", highlightbackground="#1c1c1c",
                                  highlightthickness=2)
        self.Double_frame.place(relx=0.40, rely=0.50, relwidth=0.20, relheight=0.20)
        label_reserv = Label(self.Double_frame, text='Reservar', font=fonte_DoubleClick, bg='#ffd700', fg='#0000cd')
        label_reserv.place(relx=0.05, rely=0.045, relwidth=0.90, relheight=0.15)

        label_store = Label(self.Double_frame, text='Loja', font=fonte_DoubleClick, bg='#ffd700', fg='#0000cd')
        label_store.place(relx=0.05, rely=0.48, relwidth=0.90, relheight=0.15)

        fonte_Entry = ("Verdana", 10, "italic", 'bold')
        self.unit = ttk.Combobox(self.Double_frame, font=fonte_Entry)
        self.unit['values'] = ('1', '2', '3', '4', '5')
        self.unit.bind('<Return>', self.reserve)
        self.unit.place(relx=0.20, rely=0.23, relwidth=0.60, relheight=0.19)

        self.store_Reserv = ttk.Combobox(self.Double_frame, font=fonte_Entry)
        self.store_Reserv['values'] = ('2064', '1432', '2007', '1518', '1571', '1744', '1574', '1648', '2226', 'LAB')
        self.store_Reserv.bind('<Return>', self.reserve)
        self.store_Reserv.place(relx=0.20, rely=0.68, relwidth=0.60, relheight=0.19)
# ==========================//===========================/LISTAS/========================//=============================

    def listaFrame_Reg(self):
        self.listaReg = ttk.Treeview(self.frame_options, height=6, columns=('col1', 'col2', 'col3', 'col4', 'col5',
                                                                            'col6', 'col7', 'col8', 'col9', 'col10'))
        self.listaReg.heading('#0')
        self.listaReg.heading('col1', text='Data')
        self.listaReg.heading('col2', text='Esférico')
        self.listaReg.heading('col3', text='Cilindro')
        self.listaReg.heading('col4', text='Adição')
        self.listaReg.heading('col5', text='Olho')
        self.listaReg.heading('col6', text='Material')
        self.listaReg.heading('col7', text='Laboratório')
        self.listaReg.heading('col8', text='Loja')
        self.listaReg.heading('col9', text='Sequência')
        self.listaReg.heading('col10', text='Motivo')

        self.listaReg.column('#0', width=0)
        self.listaReg.column('col1', width=40)
        self.listaReg.column('col2', width=5)
        self.listaReg.column('col3', width=5)
        self.listaReg.column('col4', width=5)
        self.listaReg.column('col5', width=5)
        self.listaReg.column('col6', width=60)
        self.listaReg.column('col7', width=20)
        self.listaReg.column('col8', width=20)
        self.listaReg.column('col9', width=20)
        self.listaReg.column('col10', width=50)

        self.listaReg.place(relx=0.025, rely=0.10, relwidth=0.95, relheight=0.73)

    def lista_FrameExit(self):
        self.lista_Exit = ttk.Treeview(self.frame_options, height=3, columns=('col1', 'col2', 'col3', 'col4'))
        self.lista_Exit.heading('#0')
        self.lista_Exit.heading('col1', text='Cod. Barras')
        self.lista_Exit.heading('col2', text='Loja')
        self.lista_Exit.heading('col3', text='Sequência')
        self.lista_Exit.heading('col4', text='Motivo')

        self.lista_Exit.column('#0', width=0)
        self.lista_Exit.column('col1', width=80)
        self.lista_Exit.column('col2', width=30)
        self.lista_Exit.column('col3', width=30)
        self.lista_Exit.column('col4', width=120)

        self.lista_Exit.place(relx=0.025, rely=0.18, relwidth=0.95, relheight=0.65)

    def lista_FrameZero(self):
        self.listaZero = ttk.Treeview(self.frame_options, height=3, columns=('col1', 'col2', 'col3', 'col4', 'col5'))
        self.listaZero.heading('#0')
        self.listaZero.heading('col1', text='Esférico')
        self.listaZero.heading('col2', text='Cilindro')
        self.listaZero.heading('col3', text='Material')
        self.listaZero.heading('col4', text='Laboratório')
        self.listaZero.heading('col5', text='Unidade')

        self.listaZero.column('#0', width=0)
        self.listaZero.column('col1', width=30)
        self.listaZero.column('col2', width=30)
        self.listaZero.column('col3', width=80)
        self.listaZero.column('col4', width=80)
        self.listaZero.column('col5', width=30)

        self.listaZero.place(relx=0.025, rely=0.20, relwidth=0.95, relheight=0.64)

    def listaFrame(self):  # FUNÇÃO CADASTRO TAMBÉM USA ESSA LISTA
        self.listaCli = ttk.Treeview(self.frame_options, height=3, columns=( 'col1', 'col2', 'col3', 'col4',
                                                                             'col5', 'col6', 'col7'))
        self.listaCli.heading('#0')
        self.listaCli.heading('col1', text='Esférico')
        self.listaCli.heading('col2', text='Cilíndro')
        self.listaCli.heading('col3', text='Adição')
        self.listaCli.heading('col4', text='Olho')
        self.listaCli.heading('col5', text='Material')
        self.listaCli.heading('col6', text='Laboratório')
        self.listaCli.heading('col7', text='Unidade')

        self.listaCli.column('#0', width=0)
        self.listaCli.column('col1', width=20)
        self.listaCli.column('col2', width=20)
        self.listaCli.column('col3', width=20)
        self.listaCli.column('col4', width=5)
        self.listaCli.column('col5', width=140)
        self.listaCli.column('col6', width=50)
        self.listaCli.column('col7', width=20)

        self.listaCli.place(relx=0.025, rely=0.26, relwidth=0.95, relheight=0.58)
        self.listaCli.bind('<Double-1>', self.double_ClickReserv)

    def lista_RegService(self):
        self.listaRegService = ttk.Treeview(self.frame_options, height=3, columns=('col1', 'col2', 'col3', 'col4',
                                                                            'col5', 'col6'))
        self.listaRegService.heading('#0')
        self.listaRegService.heading('col1', text='Data e Hora')
        self.listaRegService.heading('col2', text='Loja')
        self.listaRegService.heading('col3', text='Sequência')
        self.listaRegService.heading('col4', text='Tipo')
        self.listaRegService.heading('col5', text='Situação')
        self.listaRegService.heading('col6', text='Previsão')

        self.listaRegService.column('#0', width=0)
        self.listaRegService.column('col1', width=90)
        self.listaRegService.column('col2', width=20)
        self.listaRegService.column('col3', width=30)
        self.listaRegService.column('col4', width=60)
        self.listaRegService.column('col5', width=50)
        self.listaRegService.column('col6', width=50)

        self.listaRegService.place(relx=0.025, rely=0.26, relwidth=0.95, relheight=0.58)

    def lista_searchService(self, event=''):
        self.listSearchServ = ttk.Treeview(self.frame_services, height=3, columns=('col1', 'col2', 'col3', 'col4'))
        self.listSearchServ.heading('#0')
        self.listSearchServ.heading('col1', text='Loja')
        self.listSearchServ.heading('col2', text='Sequência')
        self.listSearchServ.heading('col3', text='Tipo')
        self.listSearchServ.heading('col4', text='Garantia')

        self.listSearchServ.column('#0', width=0)
        self.listSearchServ.column('col1', width=50)
        self.listSearchServ.column('col2', width=100)
        self.listSearchServ.column('col3', width=90)
        self.listSearchServ.column('col4', width=50)

        self.listSearchServ.place(relx=0.025, rely=0.07, relwidth=0.948, relheight=0.87)

        # BARRA DE ROLAGEM
        self.scrollLista = Scrollbar(self.listSearchServ, orient='vertical', jump=1)
        self.listSearchServ.configure(yscrollcommand=self.scrollLista.set)
        self.scrollLista.place(relx=0.967, rely=0.042, relwidth=0.03, relheight=0.956)

    def lista_Pesq(self):
        self.listaPesq = ttk.Treeview(self.frame_options, height=3, columns=('col1', 'col2', 'col3', 'col4', 'col5',
                                                                             'col6', 'col7', 'col8'))
        self.listaPesq.heading('#0')
        self.listaPesq.heading('col1', text='Loja')
        self.listaPesq.heading('col2', text='Seq.')
        self.listaPesq.heading('col3', text='Data e Hora')
        self.listaPesq.heading('col4', text='Tipo')
        self.listaPesq.heading('col5', text='Situação')
        self.listaPesq.heading('col6', text='Previsão')
        self.listaPesq.heading('col7', text='Observação')
        self.listaPesq.heading('col8', text='Status')

        self.listaPesq.column('#0', width=0)
        self.listaPesq.column('col1', width=10)
        self.listaPesq.column('col2', width=20)
        self.listaPesq.column('col3', width=80)
        self.listaPesq.column('col4', width=40)
        self.listaPesq.column('col5', width=45)
        self.listaPesq.column('col6', width=40)
        self.listaPesq.column('col7', width=40)
        self.listaPesq.column('col8', width=20)

        self.listaPesq.place(relx=0.025, rely=0.18, relwidth=0.95, relheight=0.65)
        self.listaPesq.bind('<Double-1>', self.Obs)
# =============================//=======================/FRONT END/=======================//============================
class Interface(Funcs):
# ==========================//========================/INICIALIZAÇÃO/========================//=========================
    def __init__(self):
        self.root = root
        self.tela()
        self.buttons()
        self.titulo()
        self.informations()
        self.options()
        self.services()
        self.button_Cadastrar()
        self.button_VisEstoque()
        self.button_LensZero()
        self.button_Retirar()
        self.button_RegSaida()
        self.button_RegService()
        self.button_Sair()
        self.logo()
        self.date_Today()
        self.date_hour()
        self.label_services()
        self.lista_searchService()
        self.button_Selecionar()
        self.button_Pesq()
        self.button_Rel()
        self.cont()
        self.label_Cont()
        root.mainloop()
# ==========================//===========================/FRAMES/========================//=============================

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # TELA PRINCIPAL
    def tela(self):  # CARACTERISTICAS DA TELA
        self.root.title("Gerenciamento Laboratório Carol")
        self.root.geometry("1300x720")
        self.root.resizable(True, True)
        self.root.minsize(width=800, height=500)
        self.root.configure(background="#0000cd")

    def titulo(self):  # FRAME DO TÍTULO
        self.frame_titulo = Frame(self.root, bd=-4, bg="#ffd700", highlightbackground="#1c1c1c",
                                  highlightthickness=2)
        self.frame_titulo.place(relx=0.13, rely=0.02, relwidth=0.45, relheight=0.15)

    def buttons(self):  # FRAME DOS BOTÕES
        self.frame_buttons = Frame(self.root, bd=-4, bg="#ffd700", highlightbackground="#1c1c1c",
                                   highlightthickness=2)
        self.frame_buttons.place(relx=0.01, rely=0.02, relwidth=0.11, relheight=0.96)

    def informations(self):  # FRAME DAS INFORMAÇÕES
        self.frame_informations = Frame(self.root, bd=-4, bg="#ffd700", highlightbackground="#1c1c1c",
                                        highlightthickness=2)
        self.frame_informations.place(relx=0.13, rely=0.19, relwidth=0.45, relheight=0.79)

    def services(self):  # FRAME DOS SERVIÇOS
        self.frame_services = Frame(self.root, bd=-4, bg="#ffd700", highlightbackground="#1c1c1c",
                                    highlightthickness=2)
        self.frame_services.place(relx=0.59, rely=0.02, relwidth=0.40, relheight=0.96)

    def options(self):  # FRAME DAS OPÇÕES
        self.frame_options = Frame(self.root, bd=-4, bg="#f0e68c", highlightbackground="#1c1c1c",
                                   highlightthickness=2)
        self.frame_options.place(relx=0.14, rely=0.21, relwidth=0.43, relheight=0.75)

    def logo(self):  # FRAME DO LOGO
        self.fontepadraoLogo = ('Miso', '40')
        self.logoText_1 = Label(self.frame_titulo, text='ÓTICAS', bg='#ffd700', font=self.fontepadraoLogo,
                                fg='white')
        self.logoText_2 = Label(self.frame_titulo, text='|', bg='#ffd700', font=self.fontepadraoLogo, fg='white')
        self.logoText_3 = Label(self.frame_titulo, text='CAROL', bg='#ffd700', font=self.fontepadraoLogo,
                                fg='#0000cd')
        self.logoText_1.place(relx=0.15, rely=0.03, relwidth=0.335, relheight=0.55)
        self.logoText_2.place(relx=0.485, rely=0.014, relwidth=0.03, relheight=0.53)
        self.logoText_3.place(relx=0.515, rely=0.03, relwidth=0.305, relheight=0.55)
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    def Obs(self, event=''):
        self.fontepadrao = ("Verdana", 10, "italic", 'bold')
        self.frame_Obs = Frame(self.frame_options, bd=-4, bg="#f0e68c", highlightbackground="#1c1c1c",
                                   highlightthickness=2)
        self.frame_Obs.place(relx=0.05, rely=0.50, relwidth=0.90, relheight=0.30)
        self.labelAlter_Status()
        self.button_Obs()
        self.insert_Obs()
# =========================//=========================/BOTÕES ENTER/========================//==========================
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #  BOTÃO ENTER DE CADASTRO DE LENTES
    def button_Ir(self):
        self.fontepadrao = ("Verdana", 10, "italic", 'bold')
        self.Ir = Button(self.frame_options, text='Cadastrar', font=self.fontepadrao, bg='#f0e68c',
                         command=self.option_Ir)
        self.Ir.bind("<Enter>", self.passou_por_cima)
        self.Ir.bind("<Leave>", self.saiu_de_cima)
        self.Ir.place(relx=0.425, rely=0.92, relwidth=0.15, relheight=0.05)
    # FUNÇÃO DO BOTÃO ENTER PARA CADASTRO DE LENTES
    def option_Ir(self, event=''):
        print("Botão 'ir' clicado!".title())
        self.verification_Code()
        self.captura_dados()
        self.button_Ir()
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #  BOTÃO ENTER DE RETIRADA DE LENTES
    def button_Exit(self):
        self.fontepadrao = ("Verdana", 10, "italic", 'bold')
        self.exitButton = Button(self.frame_options, text='Retirar', font=self.fontepadrao, bg='#f0e68c',
                         command=self.option_ButtonExit)
        self.exitButton.bind("<Enter>", self.passou_por_cima)
        self.exitButton.bind("<Leave>", self.saiu_de_cima)
        self.exitButton.place(relx=0.425, rely=0.92, relwidth=0.15, relheight=0.05)
    # FUNÇÃO DO BOTÃO ENTER PARA RETIRAR LENTES
    def option_ButtonExit(self, event=''):
        print("Botão 'ENTER/RETIRAR' clicado!")
        self.remove_LensAdd()
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #  BOTÃO ENTER DE VISUALIZAÇÃO DE LENTES
    def button_Vis(self):
        self.fontepadrao = ("Verdana", 10, "italic", 'bold')
        self.VisButton = Button(self.frame_options, text='Visualizar', font=self.fontepadrao, bg='#f0e68c',
                                 command=self.option_ButtonVis)
        self.VisButton.bind("<Enter>", self.passou_por_cima)
        self.VisButton.bind("<Leave>", self.saiu_de_cima)
        self.VisButton.place(relx=0.425, rely=0.92, relwidth=0.15, relheight=0.05)
    # FUNÇÃO DO BOTÃO ENTER PARA VISUALIZAR LENTES
    def option_ButtonVis(self, event=''):
        print("Botão 'ENTER/VISUALIZAR' clicado!")
        self.captura_dadosVis()
        self.option_VisLens()
        self.clear_dadosVis()
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #  BOTÃO ENTER DE BUSCAR LENTES ZERADAS
    def button_LensZeroEnter(self):
        self.fontepadrao = ("Verdana", 10, "italic", 'bold')
        self.lensZeroButton = Button(self.frame_options, text='Buscar', font=self.fontepadrao, bg='#f0e68c',
                         command=self.option_ButtonBuscar)
        self.lensZeroButton.bind("<Enter>", self.passou_por_cima)
        self.lensZeroButton.bind("<Leave>", self.saiu_de_cima)
        self.lensZeroButton.place(relx=0.425, rely=0.92, relwidth=0.15, relheight=0.05)
    # FUNÇÃO DO BOTÃO ENTER DE BUSCAR LENTES ZERADAS
    def option_ButtonBuscar(self, event=''):
        print("Botão 'ENTER/BUSCAR LENS ZERO' clicado!")
        self.captura_dadosLensZero()
        self.lensZero()
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # BOTÃO ENTER DE REGISTRAR LENTES
    def button_RegEnter(self):
        self.fontepadrao = ("Verdana", 10, "italic", 'bold')
        self.button_RegEn = Button(self.frame_options, text='Procurar', font=self.fontepadrao, bg='#f0e68c',
                                     command=self.option_ButtonReg)
        self.button_RegEn.bind("<Enter>", self.passou_por_cima)
        self.button_RegEn.bind("<Leave>", self.saiu_de_cima)
        self.button_RegEn.place(relx=0.425, rely=0.92, relwidth=0.15, relheight=0.05)
    # FUNÇÃO DO BOTÃO DE REGISTRAR LENTES
    def option_ButtonReg(self, event=''):
        print("Botão 'ENTER/REGISTRO' clicado!")
        self.captura_dadosRegSaida()
        self.print_RegSaida()
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # BOTÃO ENTER DE REGISTRAR SERVIÇOS
    def button_RegServiceEnter(self):
        self.fontepadrao = ("Verdana", 10, "italic", 'bold')
        self.RegServiceEnter = Button(self.frame_options, text='Registrar', font=self.fontepadrao, bg='#f0e68c',
                                   command=self.option_RegServiceEnter)
        self.RegServiceEnter.bind("<Enter>", self.passou_por_cima)
        self.RegServiceEnter.bind("<Leave>", self.saiu_de_cima)
        self.RegServiceEnter.place(relx=0.425, rely=0.92, relwidth=0.15, relheight=0.05)
    # FUNÇÃO DO BOTÃO DE REGISTRR SERVIÇOS
    def option_RegServiceEnter(self, event=''):
        print("Botão 'ENTER/REGISTRO DE SERVIÇOS' clicado!")
        self.captura_dadosRegServico()
        self.recording_RegService()
        self.cont()
        self.label_Cont()
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # BOTÃO ENTER DE ADICONAR SERVIÇOS
    def button_Selecionar(self):
        self.fontepadrao = ("Verdana", 10, "italic", 'bold')
        self.AddService = Button(self.frame_services, text='Adicionar', font=self.fontepadrao, bg='#f0e68c',
                                 command=self.option_AddService)
        self.AddService.bind("<Enter>", self.passou_por_cima)
        self.AddService.bind("<Leave>", self.saiu_de_cima)
        self.AddService.place(relx=0.425, rely=0.947, relwidth=0.15, relheight=0.04)
    # FUNÇÃO DO BOTÃO DE ADICIONAR SERVIÇOS
    def option_AddService(self, event=''):
        print("Botão 'ENTER/ADICONAR SERVIÇOS' clicado!")
        self.captura_ListService()
        self.cont()
        self.label_Cont()
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # BOTÃO ENTER DE PESQUISAR SERVIÇOS
    def button_PesqEnter(self):
        self.fontepadrao = ("Verdana", 10, "italic", 'bold')
        self.pesqService = Button(self.frame_options, text='Pesquisar', font=self.fontepadrao, bg='#f0e68c',
                                 command=self.option_buttonPesqEnter)
        self.pesqService.bind("<Enter>", self.passou_por_cima)
        self.pesqService.bind("<Leave>", self.saiu_de_cima)
        self.pesqService.place(relx=0.425, rely=0.92, relwidth=0.15, relheight=0.05)
    # FUNÇÃO DO BOTÃO DE PESQUISAR SERVIÇOS
    def option_buttonPesqEnter(self, event=''):
        print("Botão 'ENTER/PESQUISAR SERVIÇOS' clicado!")
        self.pesq_Capt()
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # BOTÕES ENTER DA OBS
    def button_Obs(self):
        self.button_Enter = Button(self.frame_Obs, font=self.fontepadrao, text='Inserir', bg='#f0e68c',
                                   command=self.alter_Obs)
        self.button_Enter.bind('<Enter>', self.passou_por_cima)
        self.button_Enter.bind('<Leave>', self.saiu_de_cima)
        self.button_Enter.place(relx=0.80, rely=0.09, relwidth=0.15, relheight=0.14)
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # BOTÃO ENTER DE RELATÓRIO
    def button_EnterRel(self):
        self.EnterRel = Button(self.frame_options, font=self.fontepadrao, text='Relatório', bg='#f0e68c',
                               command=self.option_EnterRel)
        self.EnterRel.bind('<Enter>', self.passou_por_cima)
        self.EnterRel.bind('<Leave>', self.saiu_de_cima)
        self.EnterRel.place(relx=0.425, rely=0.92, relwidth=0.15, relheight=0.05)
    def option_EnterRel(self, event=''):
        print('Botão ENTER RELATÓRIO clicado!')
        self.CaptDados_Rel()
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # EFEITOS NOS BOTÕES
    def passou_por_cima(self, event):
        event.widget.config(relief=GROOVE)
    def saiu_de_cima(self, event):
        event.widget.config(relief=RAISED)
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# =========================//============================/BOTÕES/===========================//==========================

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #  BOTÃO CADASTRAR
    def button_Cadastrar(self):
        self.CadastrarLente = Button(self.frame_buttons, text="Cadastrar", command=self.option_RegisterLens,
                                     bd=2, bg="#c0c0c0", fg="black")
        self.CadastrarLente["font"] = ("Verdana", 10, "italic", "bold")
        self.CadastrarLente.bind("<Enter>", self.passou_por_cima)
        self.CadastrarLente.bind("<Leave>", self.saiu_de_cima)
        self.CadastrarLente.bind("f1", self.option_RegisterLens)
        self.CadastrarLente.place(relx=0.05, rely=0.02, relwidth=0.90, relheight=0.05)
    #  OPÇOES DE CADASTRO DE LENTES
    def option_RegisterLens(self, event=''):
        print("Botão de cadastro clicado!".title())
        self.label_and_entry()
        self.button_Ir()
        self.clear()
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #  BOTÃO VISUALIZAR
    def button_VisEstoque(self):
        self.VisEstoque = Button(self.frame_buttons, text="Vis. Estoque", bd=2, bg="#c0c0c0", fg="black",
                                 command=self.exibirOpcoes_Vis)
        self.VisEstoque["font"] = ("Verdana", 10, "italic", "bold")
        self.VisEstoque.bind("<Enter>", self.passou_por_cima)
        self.VisEstoque.bind("<Leave>", self.saiu_de_cima)
        self.VisEstoque.place(relx=0.05, rely=0.08, relwidth=0.90, relheight=0.05)
    #  OPÇÕES DE VISUALIZAÇÃO DO ESTOQUE
    def exibirOpcoes_Vis(self):
        print("Botão visualizar estoque clicado!".title())
        self.options()
        self.label_VisEst()
        self.listaFrame()
        self.button_Vis() # BOTAO ENTER DE VISUALIZAR
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # BOTÃO LENTES ZERADAS
    def button_LensZero(self):
        self.LensZero = Button(self.frame_buttons, text="Lentes\nem\nFalta", bd=2, bg="#c0c0c0", fg="black",
                               command=self.zero_lens)
        self.LensZero["font"] = ("Verdana", 10, "italic", "bold")
        self.LensZero.bind("<Enter>", self.passou_por_cima)
        self.LensZero.bind("<Leave>", self.saiu_de_cima)
        self.LensZero.place(relx=0.05, rely=0.14, relwidth=0.90, relheight=0.10)
    #  OPÇÕES DE LENTES ZERADAS NO ESTOQUE
    def zero_lens(self):
        print("Botão lentes em falta clicado!".title())
        self.options()
        self.label_LensZero()
        self.lista_FrameZero()
        self.button_LensZeroEnter()
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #  BOTÃO RETIRAR
    def button_Retirar(self):
        self.Retirar = Button(self.frame_buttons, text="Retirar", bd=2, bg="#c0c0c0", fg="black",
                              command=self.lens_output)
        self.Retirar["font"] = ("Verdana", 10, "italic", "bold")
        self.Retirar.bind("<Enter>", self.passou_por_cima)
        self.Retirar.bind("<Leave>", self.saiu_de_cima)
        self.Retirar.place(relx=0.05, rely=0.25, relwidth=0.90, relheight=0.05)
    #  OPÇÕES DE RETIRAR LENTES
    def lens_output(self):
        print("Botão retirar lente clicado!".title())
        self.options()
        self.lista_FrameExit()
        self.label_lensOutput()
        self.button_Exit()
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #  BOTÃO REGISTRO DE SAÍDA
    def button_RegSaida(self):
        self.RegSaida = Button(self.frame_buttons, text="Registro\nde\nSaída", bg="#c0c0c0", fg="black",
                               command=self.reg_output)
        self.RegSaida["font"] = ("Verdana", 10, "italic", "bold")
        self.RegSaida.bind("<Enter>", self.passou_por_cima)
        self.RegSaida.bind("<Leave>", self.saiu_de_cima)
        self.RegSaida.place(relx=0.05, rely=0.31, relwidth=0.90, relheight=0.10)
    #  OPÇÕES DE REGISTRAR SAÍDAS DE LENTES
    def reg_output(self):
        print("Botão registro de saída clicado!".title())
        self.options()
        self.label_RegisSaida()
        self.listaFrame_Reg()
        self.button_RegEnter()
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # BOTÃO REGISTRAR SERVIÇOS
    def button_RegService(self):
        self.regService = Button(self.frame_buttons, text='Registrar\nServiços', bg='#c0c0c0', fg='black',
                                 command=self.option_buttonRegService)
        self.regService["font"] = ("Verdana", 10, "italic", "bold")
        self.regService.bind("<Enter>", self.passou_por_cima)
        self.regService.bind("<Leave>", self.saiu_de_cima)
        self.regService.place(relx=0.05, rely=0.42, relwidth=0.90, relheight=0.10)
    def option_buttonRegService(self):
        print('Botão Registrar Serviços clicado!')
        self.options()
        self.button_RegServiceEnter()
        self.label_RegService()
        self.lista_RegService()
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def button_Pesq(self):
        self.buttonObs = Button(self.frame_buttons, text='Pesquisar\nServiços', bg='#c0c0c0', fg='black',
                          command=self.option_buttonPesq)
        self.buttonObs["font"] = ("Verdana", 10, "italic", "bold")
        self.buttonObs.bind("<Enter>", self.passou_por_cima)
        self.buttonObs.bind("<Leave>", self.saiu_de_cima)
        self.buttonObs.place(relx=0.05, rely=0.53, relwidth=0.90, relheight=0.10)
    def option_buttonPesq(self):
        print('Botão Pesquisar Serviços clicado!')
        self.options()
        self.label_Pesq()
        self.lista_Pesq()
        self.button_PesqEnter()
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # BOTÃO RELATÓRIO
    def button_Rel(self):
        self.buttonRel = Button(self.frame_buttons, text='Relatório', bg='#c0c0c0', fg='black',
                                command=self.option_ButtonRel)
        self.buttonRel["font"] = ("Verdana", 10, "italic", "bold")
        self.buttonRel.bind("<Enter>", self.passou_por_cima)
        self.buttonRel.bind("<Leave>", self.saiu_de_cima)
        self.buttonRel.place(relx=0.05, rely=0.87, relwidth=0.90, relheight=0.05)
    def option_ButtonRel(self):
        print('Botão Relatório Clicado!')
        self.label_Rel()
        self.button_EnterRel()

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #  BOTÃO DE SAIR
    def button_Sair(self):
        self.Sair = Button(self.frame_buttons, text="Sair", bg="#c0c0c0", fg="black")
        self.Sair["font"] = ("Verdana", 10, "italic", "bold")
        self.Sair.bind("<Enter>", self.passou_por_cima)
        self.Sair.bind("<Leave>", self.saiu_de_cima)
        self.Sair.place(relx=0.05, rely=0.93, relwidth=0.90, relheight=0.05)
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

Interface()  # chamando a classe para iniciar

# sistema desencolvido por Matheus Brodt no ano de 2021 para fins de estudo e de uso próprio...
