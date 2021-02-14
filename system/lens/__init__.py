def read_whole(txt):
    while True:
        try:
            loop = False
            while not loop:
                validate = str(input(txt)).replace(',', '.')
                if validate.isalpha() or validate.isspace():
                    print('\033[31mEntrada Inválida\033[m')
                    continue
                else:
                    loop = True
                    return int(validate)
        except (ValueError, TypeError):
            print('\033[33mErro ao identificar o valor digitado na opção.\033[m')
            continue
        else:
            break


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


def register_cod_one(cod):
    import mysql.connector
    try:
        bar_code = cod
        conection = mysql.connector.connect(host='localhost', user='root', password='', database='lab_carol')
        cursor = conection.cursor()
        cursor.execute(f"UPDATE stock SET amount = amount+{1} WHERE cod_barras = {bar_code}")
        conection.commit()
        print('\033[34mLente cadastrada com sucesso!\033[m')
    except:
        print('\033[31mErro ao cadastrar a lente!\033[m')


def register_cod(cod, amount):
    import mysql.connector
    try:
        bar_code = cod
        amount_1 = amount
        conection = mysql.connector.connect(host='localhost', user='root', password='', database='lab_carol')
        cursor = conection.cursor()
        cursor.execute(f"UPDATE stock SET amount = amount+{amount_1} WHERE cod_barras = {bar_code}")
        conection.commit()
        print('\033[34mLente cadastrada com sucesso!\033[m')
    except:
        print('\033[31mErro ao cadastrar a lente!\033[m')


def exit_code(cod, loja, motivo):
    import mysql.connector
    from datetime import date
    try:
        bar_code = read_whole(cod)
        if read_zero_cod(bar_code):
            store = read_store(loja)
            print('\033[35m[1] para quebra.\n'
                  '[2] para montagem.\n'
                  '[3] para garantia.\033[m')
            reason = read_reason(motivo)
            conection = mysql.connector.connect(host='localhost', user='root', password='', database='lab_carol')
            cursor = conection.cursor()  # para buscar o material da lente
            cursor.execute(f"SELECT material FROM stock WHERE cod_barras = {bar_code}")
            lens = cursor.fetchone()

            cursor = conection.cursor()  # para retirar a lente do estoque
            cursor.execute(f"UPDATE stock SET amount = amount-{1} WHERE cod_barras = {bar_code}")
            conection.commit()
            print('\033[34mLente retirada do estoque com sucesso!\033[m')

            cursor = conection.cursor()  # para adicionar a lente na lista de saída
            cursor.execute(f"INSERT INTO store VALUES ({bar_code}, '{lens[0]}', {store}, '{reason}', '{date.today()}')")
            conection.commit()
            print('\033[34mLente cadastrada na lista de saída!\033[m')
    except:
        print('\033[31mErro ao retirar a lente!\033[m')


def menu():
    lens = {'1': '1.56_ar', '2': '1.56_blue', '3': 'poly_ar', '4': '1.67', '5': 'zeiss_blue', '6': 'zeiss_platinum',
            '7': 'zeiss_silver', '8': 'zeiss_photo'}
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


def zero(lab, material):
    """
    Lens search function does not exist in the database.
    :param lab: Laboratory.
    :param material:Material lens
    :return: The lents you don't have in the database.
    """
    import mysql.connector
    lens = {'1': 'Lente Vis Simples 1.50 c/A.R.', '2': 'Lente Vis Simples 1.56 c/A.R.',
            '3': 'Lente V.S. 1.56 Filtro Azul c/A.R.', '4': 'Lente Ac. Progressiva 1.56 c/A.R.',
            '5': 'Lente Vis Simp 1.59 Poly c/A.R.', '6': 'zeiss_platinum',
            '7': 'zeiss_silver', '8': 'zeiss_photo', '9': 'zeiss_blue'}
    laboratory = {'1': 'haytek', '2': 'zeiss'}
    lab_1 = read_whole(lab)
    material_1 = read_material(material)
    try:
        conection = mysql.connector.connect(host='localhost', user='root', password='', database='lab_carol')
        cursor = conection.cursor()
        cursor.execute(f"SELECT spherical, cylindrical, adicao, eye FROM stock "
                       f"WHERE material = '{lens[f'{material_1}']}' AND laboratory = '{laboratory[f'{lab_1}']}'"
                       f" AND amount = '0' OR amount < '0'")
        result = cursor.fetchall()
        print(f'\033[34mLentes {lens[f"{material_1}"]} zeradas:\033[m')
        for r in result:
            sphe = (r[0])
            cyl = (r[0+1])
            add = (r[0+2])
            eye = (r[0+3])
            if add is None:
                add = 0
            if eye == '':
                eye = 'VS'
            print(f'|ESFÉRICO: \033[31m{sphe:.2f}\033[m| CILINDRO: \033[31m{cyl:.2f}\033[m| '
                  f'ADIÇÃO: \033[31m{add:.2f}\033[m| OLHO: \033[31m{eye}\033[m')
        cursor.close()
    except:
        print(f'\033[31mErro ao pesquisar grade zerada no estoque!\033[m')


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


def register_diopter(lab, material, sphe_diopter, cyl_diopter, add, eye, amount):
    import mysql.connector
    lens = {'1': 'Lente Vis Simples 1.50 c/A.R.', '2': 'Lente Vis Simples 1.56 c/A.R.',
            '3': 'Lente V.S. 1.56 Filtro Azul c/A.R.', '4': 'Lente Ac. Progressiva 1.56 c/A.R.',
            '5': 'Lente Vis Simp 1.59 Poly c/A.R.', '6': 'zeiss_platinum',
            '7': 'zeiss_silver', '8': 'zeiss_photo', '9':'zeiss_blue'}
    laboratory = {'1': 'haytek', '2': 'zeiss'}
    try:
        lab_1 = read_lab(lab)
        material_1 = read_material(material)
        spherical = read_diopter(sphe_diopter)
        cylinder = read_diopter(cyl_diopter)
        adicao = read_diopter(add)
        opt_eye = read_eye(eye)
        amount_1 = read_whole(amount)
        conection = mysql.connector.connect(host='localhost', user='root', password='', database='lab_carol')
        cursor = conection.cursor()
        cursor.execute(f"UPDATE stock SET amount = amount+{amount_1} WHERE laboratory = '{laboratory[f'{lab_1}']}' "
                       f"AND spherical = {spherical} AND cylindrical = {cylinder} AND "
                       f"material = '{lens[f'{material_1}']}' AND eye = '{opt_eye}' AND adicao = {adicao}")
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
