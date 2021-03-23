#  CLASSES/FUNÇOES DO SISTEMA

def read_whole(txt):
        try:
            validate = str(input(txt)).replace(',', '.')
            if validate.isalpha() or validate.isspace():
                print('\033[31mEntrada Inválida\033[m')
            else:
                return int(validate)
        except (ValueError, TypeError):
            print('\033[31mEntrada Inválida\033[m')



def search(lab, material, sph_diopter, cyl_diopter, add, eye):
    import mysql.connector
    lens = {'1': 'Lente Vis Simples 1.50 c/A.R.', '2': 'Lente Vis Simples 1.56 c/A.R.',
            '3': 'Lente V.S. 1.56 Filtro Azul c/A.R.', '4': 'Lente Ac. Progressiva 1.56 c/A.R.',
            '5': 'Lente Vis Simp 1.59 Poly c/A.R.', '6': 'zeiss_platinum',
            '7': 'zeiss_silver', '8': 'zeiss_photo', '9': 'zeiss_blue'}
    laboratory = {'1': 'haytek', '2': 'zeiss'}
    try:
        lab_1 = read_whole(lab)
        material_1 = read_material(material)
        spheric = read_diopter(sph_diopter)
        cylinder = read_diopter(cyl_diopter)
        adicao = read_diopter(add)
        opt_eye = read_eye(eye)
        validate_material = lens[f'{material_1}']
        if validate_material == lens['1']:
            material_1 = f"'{lens['1']}' OR material = '{lens['2']}'"
        else:
            material_1 = lens[f'{material_1}']
        conection = mysql.connector.connect(host='localhost', user='root', password='', database='lab_carol')
        cursor = conection.cursor()
        cursor.execute(f"SELECT amount FROM stock WHERE spherical = {spheric} AND cylindrical = -{cylinder} "
                    f"AND eye = '{opt_eye}' AND material = {material_1} "
                    f"AND laboratory = '{laboratory[f'{lab_1}']}' AND adicao = {adicao}")
        result = cursor.fetchone()
        for r in result:
            if r <= 0:
                print('\033[33mALERTA! LENTE EM FALTA NO ESTOQUE.\033[m')
            else:
                print(f"\033[35m{r} unidade(s)\033[m")
        conection.close()
        return True
    except:
        print('Lente não localizada no estoque!')
        return False


#  dar atenção ainda nessa função, finalizado
def register_cod_one(cod):
    import mysql.connector
    try:

        codigos = []
        bar_code = read_whole(cod)
        conection = mysql.connector.connect(host='localhost', user='root', password='', database='lab_carol')

        cursor = conection.cursor()  # para examinar o código de barras
        cursor.execute(f"SELECT cod_barras FROM stock ")
        result = cursor.fetchall()
        for d in result:
            e = d
            for c in e:
                codigos.append(c)

        if bar_code in codigos:
            cursor = conection.cursor()  # para cadastrar a lente
            cursor.execute(f"UPDATE stock SET amount = amount+{1} WHERE cod_barras = {bar_code}")
            conection.commit()

            cursor = conection.cursor()  # para exibir qula lente foi cadastrada
            cursor.execute(f"SELECT material FROM stock WHERE cod_barras = {bar_code}")
            lens = cursor.fetchone()
            conection.close()
            print(f'\033[34m{lens[0]} cadastrada com sucesso!\033[m')
        else:
            sound()
            print('\033[31mCódigo não existe!\033[m')
            while True:
                print('\033[32mCadastrar código de barras?\033[m')
                print('\033[35m[1] para SIM\n[2] para NÃO\033[m')
                opt = read_whole('Digite: ')
                if opt == 1:
                    menu()  # para cadastrar se o código não existir
                    register_diopter('Digite o código de barras: ', 'Selecione o laboratório: ',
                                    'Selecione o material: ', 'Dioptria esférica: ', 'Dioptria cilindrica: ',
                                    'Digite a adição: ', 'Digite o lado: ', 'Digite a quantidade: ')
                    break
                elif opt == 2:
                    break
                else:
                    print('\033[33mOpção Inválida!\033[m')
    except:
        print('\033[31mErro ao cadastrar a lente!\033[m')


#  editar esssa função, finalizado
def register_cod(cod, amount):
    import mysql.connector
    try:

        codigos = []
        bar_code = read_whole(cod)
        amount_1 = read_whole(amount)
        conection = mysql.connector.connect(host='localhost', user='root', password='', database='lab_carol')

        cursor = conection.cursor()  # para examinar o código de barras
        cursor.execute(f"SELECT cod_barras FROM stock ")
        result = cursor.fetchall()
        for d in result:
            e = d
            for c in e:
                codigos.append(c)

        if bar_code in codigos:
            cursor = conection.cursor()  # para cadastrar a lente
            cursor.execute(f"UPDATE stock SET amount = amount+{amount_1} WHERE cod_barras = {bar_code}")
            conection.commit()

            cursor = conection.cursor()  # para exibir qula lente foi cadastrada
            cursor.execute(f"SELECT material FROM stock WHERE cod_barras = {bar_code}")
            lens = cursor.fetchone()
            conection.close()
            print(f'\033[34m{lens[0]} cadastrada com sucesso!\033[m')
        else:
            sound()
            print('\033[31mCódigo não existe!\033[m')
            while True:
                print('\033[32mCadastrar código de barras?\033[m')
                print('\033[35m[1] para SIM\n[2] para NÃO\033[m')
                opt = read_whole('Digite: ')
                if opt == 1:
                    menu()  # para cadastrar se o código não existir
                    register_diopter('Digite o código de barras: ', 'Selecione o laboratório: ',
                                    'Selecione o material: ', 'Dioptria esférica: ', 'Dioptria cilindrica: ',
                                    'Digite a adição: ', 'Digite o lado: ', 'Digite a quantidade: ')
                    break
                elif opt == 2:
                    break
                else:
                    print('\033[33mOpção Inválida!\033[m')
    except:
        print('\033[31mErro ao cadastrar a lente!\033[m')


def exit_code(cod, loja, sequencia, motivo):
    import mysql.connector
    from datetime import date
    try:
        bar_code = read_whole(cod)
        if read_zero_cod(bar_code):
            store = read_store(loja)
            seq = read_whole(sequencia)
            print('\033[35m[1] para quebra.\n'
                '[2] para montagem.\n'
                '[3] para garantia.\033[m')
            reason = read_reason(motivo)
            conection = mysql.connector.connect(host='localhost', user='root', password='', database='lab_carol')
            cursor = conection.cursor()  # para buscar o material da lente
            cursor.execute(f"SELECT material FROM stock WHERE cod_barras = {bar_code}")
            lens = cursor.fetchone()
            print(f"INSERT INTO store VALUES ({bar_code}, '{lens[0]}', {store}, {seq}, '{reason}', '{date.today()}')")

            cursor = conection.cursor()  # para retirar a lente do estoque
            cursor.execute(f"UPDATE stock SET amount = amount-{1} WHERE cod_barras = {bar_code}")
            conection.commit()
            print('\033[34mLente retirada do estoque com sucesso!\033[m')

            cursor = conection.cursor()  # para adicionar a lente na lista de saída
            cursor.execute(f"INSERT INTO store VALUES ({bar_code}, '{lens[0]}', {store}, {seq}, "
                        f"'{reason}', '{date.today()}')")
            conection.commit()
            print('\033[34mLente cadastrada na lista de saída!\033[m')
    except:
        print('\033[31mErro ao retirar a lente!\033[m')


def menu():
    lens = {'1': 'Lente Vis Simples 1.50 c/A.R.', '2': 'Lente Vis Simples 1.56 c/A.R.',
            '3': 'Lente V.S. 1.56 Filtro Azul c/A.R.', '4': 'Lente Ac. Progressiva 1.56 c/A.R.',
            '5': 'Lente Vis Simp 1.59 Poly c/A.R.', '6': 'zeiss_platinum',
            '7': 'zeiss_silver', '8': 'zeiss_photo', '9': 'zeiss_blue'}
    laboratory = {'1': 'haytek', '2': 'zeiss'}
    print(f'\033[33mLaboratórios\033[m\n'
        f'1 > {laboratory["1"].capitalize()}\n'
        f'2 > {laboratory["2"].capitalize()}')
    print(f'\033[33mLentes\033[m\n'
        f'1 > {lens["1"].capitalize()}\n'
        f'2 > {lens["2"].capitalize()}\n'
        f'3 > {lens["3"].capitalize()}\n'
        f'4 > {lens["4"].capitalize()}\n'
        f'5 > {lens["5"].capitalize()}\n'
        f'6 > {lens["6"].capitalize()}\n'
        f'7 > {lens["7"].capitalize()}\n'
        f'8 > {lens["8"].capitalize()}\n')

# APAGUEI A DEF ZERO PORUQE PRECISAVA DE EDIÇÃO E NÃO ESTA USÁVEL


def exit_stock(lab, material, sph_diopter, cyl_diopter, add, eye, amount, loja, motivo):
    import mysql.connector
    from datetime import date
    lens = {'1': 'Lente Vis Simples 1.50 c/A.R.', '2': 'Lente Vis Simples 1.56 c/A.R.',
            '3': 'Lente V.S. 1.56 Filtro Azul c/A.R.', '4': 'Lente Ac. Progressiva 1.56 c/A.R.',
            '5': 'Lente Vis Simp 1.59 Poly c/A.R.', '6': 'zeiss_platinum',
            '7': 'zeiss_silver', '8': 'zeiss_photo', '9': 'zeiss_blue'}
    laboratory = {'1': 'haytek', '2': 'zeiss'}
    lab_1 = read_lab(lab)
    mat = read_material(material)
    spherical = read_diopter(sph_diopter)
    cylindrical = read_diopter(cyl_diopter)
    adicao = read_diopter(add)
    opt_eye = read_eye(eye)
    amount_1 = read_whole(amount)
    store = read_store(loja)
    print('\033[35m[1] para quebra.\n'
        '[2] para montagem.\n'
        '[3] para garantia.\033[m')
    reason = read_reason(motivo)
    try:
        conection = mysql.connector.connect(host='localhost', user='root', password='', database='lab_carol')
        cursor = conection.cursor()  # para capturar o codigo da lente
        cursor.execute(f"SELECT cod_barras FROM stock WHERE spherical = {spherical} "
                    f"AND cylindrical = -{cylindrical} AND adicao = {adicao} AND eye = '{opt_eye}' "
                    f"AND material = '{lens[f'{mat}']}' AND laboratory = '{laboratory[f'{lab_1}']}'")
        cod = cursor.fetchone()
        conection.close()
        if read_zero_cod(cod[0]):
            conection = mysql.connector.connect(host='localhost', user='root', password='', database='lab_carol')
            cursor = conection.cursor()  # para retirar a lente
            cursor.execute(f"UPDATE stock SET amount = amount-{amount_1} WHERE spherical = {spherical} "
                        f"AND cylindrical = -{cylindrical} AND adicao = {adicao} AND eye = '{opt_eye}' "
                        f"AND material = '{lens[f'{mat}']}' AND laboratory = '{laboratory[f'{lab_1}']}'")
            print('\033[34mLente retirarda do estoque com sucesso!\033[m')
            conection.commit()

            cursor = conection.cursor()  # para adicionar à tabela de saída
            cursor.execute(f"INSERT INTO store "
                        f"(cod_barras, lens, store, reason, data) "
                        f"VALUES "
                        f"({cod[0]}, '{lens[f'{mat}']}', {store}, '{reason}', '{date.today()}')")
            print('\033[34mLente cadastrada na tabela de saída!\033[m')
            conection.commit()
    except:
        print('\033[31mErro ao acessar o banco de dados!\033[m')


def read_lab(txt):
    loop = False
    while not loop:
        try:
            var = str(input(txt))
            if var == str(1) or var == str(2):
                loop = True
                return int(var)
            else:
                print('\033[31mErro ao selecionar o laboratório!\033[m')
                continue
        except(ValueError, TypeError):
            print('\033[31mErro ao selecionar o laboratório!\033[m')


def read_material(txt):
    validate_1 = read_whole(txt)
    try:
        loop = False
        while not loop:
            validate = int(validate_1)
            if validate >= 1 or validate <= 8:
                loop = True
                return int(validate)
            else:
                print('\033[31mErro ao selecionar o material!\033[m')
                continue
    except(ValueError, TypeError):
        print('\033[31mErro ao selecionar o material!!\033[m')


def read_diopter(txt):
    while True:
        try:
            loop = False
            while not loop:
                validate = str(input(txt)).replace(',', '.')
                if validate.isalpha() or validate.isspace():
                    print('\033[31mDigite a dioptria de forma correta!\033[m')
                    continue
                elif validate == '':
                    loop = True
                    return float(0)
                else:
                    loop = True
                    return float(validate)
        except:
            print('\033[31mDigite a dioptria de forma correta!\033[m')
            continue
        else:
            break


def register_diopter(codigo, lab, material, sphe_diopter, cyl_diopter, add, eye, amount):
    import mysql.connector
    lens = {'1': 'Lente Vis Simples 1.50 c/A.R.', '2': 'Lente Vis Simples 1.56 c/A.R.',
            '3': 'Lente V.S. 1.56 Filtro Azul c/A.R.', '4': 'Lente Ac. Progressiva 1.56 c/A.R.',
            '5': 'Lente Vis Simp 1.59 Poly c/A.R.', '6': 'zeiss_platinum',
            '7': 'zeiss_silver', '8': 'zeiss_photo', '9':'zeiss_blue'}
    laboratory = {'1': 'haytek', '2': 'zeiss'}
    try:
        cod = read_whole(codigo)
        lab_1 = read_lab(lab)
        material_1 = read_material(material)
        spherical = read_diopter(sphe_diopter)
        cylinder = read_diopter(cyl_diopter)
        adicao = read_diopter(add)
        opt_eye = read_eye(eye)
        amount_1 = read_whole(amount)
        conection = mysql.connector.connect(host='localhost', user='root', password='', database='lab_carol')
        cursor = conection.cursor()  # verificar essa parte
        cursor.execute(f"INSERT INTO stock VALUES "
                    f"('{cod}' , '{spherical}', '{cylinder}', '{adicao}', '{opt_eye}', '{lens[f'{material_1}']}', "
                    f"'{laboratory[f'{lab_1}']}', '{amount_1}')")
        conection.commit()
        print('\033[33mLente cadastrada com sucesso!\033[m')
    except:
        print('\033[31mErro ao cadastrar a lente!\033[m')


def read_zero_cod(value):
    import mysql.connector
    loop = False
    while not loop:
        try:
            conection = mysql.connector.connect(host='localhost', user='root', password='', database='lab_carol')
            cursor = conection.cursor()
            cursor.execute(f"SELECT amount FROM stock WHERE cod_barras = {value}")
            result = cursor.fetchone()
            if result[0] <= 0:
                print('\033[31mNão existe a lente em estoque\033[m')
                loop = True
                return False
            elif result[0] > 0:
                loop = True
                return True
        except:
            print('\033[31mErro ao contar lentes!\033[m')


def read_eye(value):
    validate = str(input(value).upper())
    try:
        loop = False
        while not loop:
            if validate == 'D' or validate == 'E':
                loop = True
                return str(validate)
            elif validate == '':
                loop = True
                return str(validate)
            else:
                print('\033[33mDigite "D" ou "E".\033[m')
                continue
    except:
        print('\033[31mERRO ao identificar lado da lente!\033[m')


def read_reason(value):
    dic = {'1': 'QUEBRA', '2': 'MONTAGEM', '3': 'GARANTIA'}
    loop = False
    while not loop:
        try:
            read = read_whole(value)
            if 0 < read <= 3:
                var = dic[f'{read}']
                load = var
                if load == 'QUEBRA' or load == 'MONTAGEM' or load == 'GARANTIA':
                    loop = True
                    return load
                else:
                    print('\033[31mMotivo Inválido!\033[m')
                    loop = True
            else:
                print('\033[31mMotivo Inválido!\033[m')
        except:
            print('\033[31mErro ao ler o motivo!\033[m')


def read_store(value):
    print('[1] > 2064\n[2] > 1432\n[3] > 2007\n[4] > 1518\n[5] > 1571\n[6] > 1744\n[7] > 1574\n[8] > 1648\n[9] > 2226\n'
        '[10] > Laboratório')
    store = {'1': '2064', '2': '1432', '3': '2007', '4': '1518', '5': '1571', '6': '1744', '7': '1574', '8': '1648',
            '9': '2226', '10': '0000'}
    try:
        loop = False
        while not loop:
            load = read_whole(value)
            if load > 10:
                print('\033[31mLoja não existe!\033[m')
                continue
            elif load >= 1:
                loop = True
                var = store[f'{load}']
                if '0000' in var:
                    print('\033[34mLaboratótio selecionado.\033[m')
                else:
                    print(f'\033[34mLoja selecionada {var}.\033[m')
                return int(var)
            else:
                print('\033[31mLoja não existe!\033[m')
                continue
    except:
        print('\033[31mErro ao reconhecer lojas!\033[m')


def cont_reasons():
    import mysql.connector
    lista = (2064, 1432, 2007, 1518, 1571, 1744, 1574, 1648, 2226, 0000)
    lista_reason = ('MONTAGEM', 'QUEBRA', 'GARANTIA')
    for e in lista:
        store = e
        for x in lista_reason:
            reason = x
            conection = mysql.connector.connect(host='localhost', user='root', password='', database='lab_carol')
            cursor = conection.cursor()
            cursor.execute(f"SELECT COUNT(reason) FROM store "
                        f"WHERE store = {store} AND reason = '{reason}' "
                        f"GROUP BY reason")
            result = cursor.fetchone()
            if store == 0000:
                if result is None:
                    print(f'\033[32mLaboratório não tem {reason.title()}.\033[m')
                else:
                    if result[0] > 1:
                        print(f'\033[32mLaboratório tem {result[0]} {reason.title()}s.\033[m')
                    else:
                        print(f'\033[32mLaboratório tem {result[0]} {reason.title()}.\033[m')
            else:
                if result is None:
                    print(f'\033[32m{store} não tem {reason.title()}.\033[m')
                else:
                    if result[0] > 1:
                        print(f'\033[32m{store} tem {result[0]} {reason.title()}s.\033[m')
                    else:
                        print(f'\033[32m{store} tem {result[0]} {reason.title()}.\033[m')
            conection.close()
        print('-' * 22)


def detailed_consulation(store):
    import mysql.connector
    try:
        store_1 = read_store(store)
        print('\033[32mDigite o período:\033[m')
        day = read_whole('Dia: ')
        month = read_whole('Mês: ')
        year = read_whole('Ano: ')
        date = f"'{year}-{month}-{day}'"
        print('\033[32mAté o dia: \033[m')
        day_1 = read_whole('Dia: ')
        month_1 = read_whole('Mês: ')
        year_1 = read_whole('Ano: ')
        date_1 = f"'{year_1}-{month_1}-{day_1}'"
        conection = mysql.connector.connect(host='localhost', user='root', password='', database='lab_carol')
        cursor = conection.cursor()
        cursor.execute(f"SELECT a.store, a.lens, a.sequencia, b.spherical, b.cylindrical, b.adicao, b.eye, a.reason, "
                    f"a.data "
                    f"FROM store AS a INNER JOIN stock AS b "
                    f"ON a.cod_barras = b.cod_barras "
                    f"WHERE a.store = {store_1} AND data BETWEEN {date} AND {date_1}")
        result = cursor.fetchall()
        if not result:
            print('\033[33mNão tem serviços cadastrados nesse perído!\033[m')
        else:
            for r in result:
                loja = (r[0])
                lab = (r[1])
                seq = (r[2])
                sphe = (r[3])
                cyl = (r[4])
                add = (r[5])
                eye = (r[6])
                mot = (r[7])
                dat = (r[8])
                print(f'Loja: {loja}, Lente: {lab}, Sequência: {seq}, Esférico: {sphe}, Cilindro: {cyl}, '
                    f'Adição: {add}, Olho: {eye}, Motivo: {mot}, Data: {dat}')
            conection.close()
    except:
        print('\033[31mErro ao análisar detalhadamente as lentes que foram usadas!\033[m')


def sound():
    #  reproduz três bips em sequência
    import winsound
    for c in range(3):
        b = winsound.Beep(332, 200)



class App():
    def __init__(self):
        from datetime import date
        date = (date.today())
        def register(self):
            option = read_whole('Digite uma opção: ')
            if option == 1:  # para registrar uma lente
                print('[1] para registrar uma à uma.'
                    '[2] para selecionar a quantidade.')
                register_type = read_whole('Digite: ')
                if register_type == 1:
                    print('\033[33mDigite "0" para voltar ao menu anterior.\033[m')
                    while True:
                        cod_barras = read_whole('Digite o código de barras: ')
                        if cod_barras == 0:
                            break
                        register_cod_one(cod_barras)
                elif register_type == 2:
                    while True:
                        cod_barras = read_whole('Digite o código de barras: ')
                        amount = read_whole('Digite a quantidade: ')
                        register_cod(cod_barras, amount)
                        print('[1] para continuar: '
                            '[2] para finalizar: ')
                        opt = read_whole('Digite: ')
                        if opt == 1:
                            continue
                        elif opt == 2:
                            break
                        else:
                            print('\033[33mOpção Inválida!\033[m')
                else:
                    print('\033[31mOpção Inválida\033[m')
        def searchLens(self):  # para pesquisar uma lente
            menu()
            search('Selecione o laboratório: ', 'Selecione o material: ', 'Digite a dioptria esférica: ',
                'Digite a dioptria cilindríca: ', 'Digite a adição: ', 'Digite o olho D ou E: ')
            opt = read_whole('Continuar pesquisando 1 > S / 2 > N: ')
            if opt == 1:
                continue
            elif opt == 2:
                break
            else:
                print('\033[31mOpção Inválida!\033[m')
                continue
        def searchLensZero(self):  # para exibir as lentes em falta do estoque
            menu()
            zero('Selecione o laboratório: ', 'Selecione o material: ')
            opt = read_whole('Continuar pesquisando 1 > S / 2 > N: ')
            if opt == 1:
                continue
            elif opt == 2:
                break
            else:
                print('\033[31mOpção Inválida!\033[m')
                continue
        def retireLens(self):  # para retirar uma lente do estoque
            record_type = read_whole('[1] para retirar pelo código de barras.\n'
                                    '[2] para retirar pela dioptria.\n'
                                    '[3] para voltar ao menu anterior. \nDigite: ')
            if record_type == 1:
                exit_code('Digite o código de barras: ', 'Digite a filal: ', 'Sequência: ', 'Motivo: ')
            elif record_type == 2:
                menu()
                exit_stock('Selecione o laboratório: ', 'Selecione o material: ', 'Digite a dioptria esférica: ',
                        'Digite a dioptria cilindrica: ', 'Digite a adição: ', 'Digite o lado: ',
                        'Digite a quantidade: ', 'Digite a filial: ', 'Motivo: ')
                opt = read_whole('Continuar retirando 1 > S / 2 > N: ')
                if opt == 1:
                    continue
                elif opt == 2:
                    break
                else:
                    print('\033[31mOpção Inválida!\033[m')
                    continue
            elif record_type == 3:
                break
            else:
                print('\033[33mOpção Inváida!\033[m')
        def registro_Saida(self):  # para ver o registro de saída de lentes e quebras
            print('[1] para pesquisa rápida.\n[2] para pesquisa detalhada.\n[3] pra volta ao menu anterior.')
            opt = read_whole('Digite: ')
            if opt == 1:
                cont_reasons()
            elif opt == 2:
                detailed_consulation('Digite a loja: ')
            elif opt == 3:
                break
            else:
                print('\033[33mOpção Inválida!\033[m')