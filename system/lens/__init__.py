def read_whole(txt):
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


def search(lab, material, esf_diopter, cil_diopter):
    """
    Function for lens search in the database.
    :param lab: Laboratory.
    :param material: Material lens.
    :param diopter_esf: Spherical diopter.
    :param diopter_cil: Cylindrical diopter.
    :return: Return True if the lens is found or false if the lens not is found, if the lens is found displays quantity.
    """
    import mysql.connector
    lens = {'1': '1.56_ar', '2': '1.56_blue', '3': 'poly_ar', '4': '1.67', '5': 'zeiss_blue', '6': 'zeiss_platinum',
            '7': 'zeiss_silver', '8': 'zeiss_photo'}
    laboratory = {'1': 'haytek', '2': 'zeiss'}
    try:
        lab_1 = read_whole(lab)
        material_1 = read_whole(material)
        espheric = str(input(esf_diopter))
        cilinder = str(input(cil_diopter))
        c_diopeter = f'{espheric}/-{cilinder}'
        conection = mysql.connector.connect(host='localhost', user='root', password='', database='lab_carol')
        cursor = conection.cursor()
        cursor.execute(f"SELECT amount FROM stock "
                       f"WHERE diopter = '{c_diopeter}' AND material = '{lens[f'{material_1}']}'"
                       f" AND laboratory = '{laboratory[f'{lab_1}']}'")
        result = cursor.fetchone()
        for r in result:
            print(f"\033[1:31:40m|{c_diopeter}|{lens[f'{material_1}']}|{r} unidades|\033[m")
        conection.close()
        return True
    except:
        print('Lente não localizada no estoque!')
        return False


def register_cod(cod, amount):
    import mysql.connector
    try:
        bar_code = read_whole(cod)
        amount_1 = read_whole(amount)
        conection = mysql.connector.connect(host='localhost', user='root', password='', database='lab_carol')
        cursor = conection.cursor()
        cursor.execute(f"UPDATE stock SET amount = amount+{amount_1} WHERE cod_barras = {bar_code}")
        conection.commit()
        print('\033[34mLente cadastrada com sucesso!\033[m')
    except:
        print('\033[31mErro ao cadastrar a lente!\033[m')


def menu():
    lens = {'1': '1.56_ar', '2': '1.56_blue', '3': 'poly_ar', '4': '1.67', '5': 'zeiss_blue', '6': 'zeiss_platinum',
            '7': 'zeiss_silver', '8': 'zeiss_photo'}
    laboratory = {'1': 'haytek', '2': 'zeiss'}
    print(f'\033[33mLaboratórios\033[m\n'
          f'1 > {laboratory["1"].capitalize()}\n'
          f'2 > {laboratory["2"].capitalize()}\n')
    print(f'\033[33mLentes\033[m\n'
          f'1 > {lens["1"]}\n'
          f'2 > {lens["2"]}\n'
          f'3 > {lens["3"]}\n'
          f'4 > {lens["4"]}\n'
          f'5 > {lens["5"]}\n'
          f'6 > {lens["6"]}\n'
          f'7 > {lens["7"]}\n'
          f'8 > {lens["8"]}\n')


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
        cursor.execute(f"SELECT spherical, cylindrical FROM stock "
                       f"WHERE material = '{lens[f'{material_1}']}' AND laboratory = '{laboratory[f'{lab_1}']}'"
                       f" AND amount = '0'")
        result = cursor.fetchall()
        print(f'\033[34mLentes {lens[f"{material_1}"]} em falta:\033[m')
        for r in result:
            sphe = (r[0])
            cyl = (r[0+1])
            print(f'|ESFÉRICO: \033[31m{sphe:.2f}\033[m| CILINDRO: \033[31m{cyl:.2f}\033[m|')
        cursor.close()
    except:
        print(f'\033[31mErro ao pesquisar grade zerada no estoque!\033[m')


def exit_stock(lab, material, esf_diopter, cil_diopter, amount):
    import mysql.connector
    lens = {'1': '1.56_ar', '2': '1.56_blue', '3': 'poly_ar', '4': '1.67', '5': 'zeiss_blue', '6': 'zeiss_platinum',
            '7': 'zeiss_silver', '8': 'zeiss_photo'}
    laboratory = {'1': 'haytek', '2': 'zeiss'}
    lab_1 = read_lab(lab)
    mat = read_whole(material)
    espherical = str(input(esf_diopter))
    cylindrical = str(input(cil_diopter))
    c_diopter = f'{espherical}/-{cylindrical}'
    amount_1 = read_whole(amount)
    try:
        conection = mysql.connector.connect(host='localhost', user='root', password='', database='lab_carol')
        cursor = conection.cursor()
        cursor.execute(f"UPDATE stock SET amount = amount-{amount_1} WHERE diopter = '{c_diopter}' "
                       f"AND material = '{lens[f'{mat}']}' AND laboratory = '{laboratory[f'{lab_1}']}'")
        cursor.close()
        conection.commit()
    except:
        print('\033[31mErro ao retirar a lente do estoque!\033[m')


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
    try:
        loop = False
        while not loop:
            validate = str(input(txt)).replace(',', '.')
            if validate.isalpha() or validate.isspace():
                print('\033[31mDigite a dioptria de forma correta!\033[m')
                continue
            else:
                loop = True
                return float(validate)
    except (ValueError, TypeError):
        print('\033[31mDigite a dioptria de forma correta!\033[m')


def register_diopter(lab, material, sphe_diopter, cyl_diopter, amount):
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
        amount_1 = read_whole(amount)
        conection = mysql.connector.connect(host='localhost', user='root', password='', database='lab_carol')
        cursor = conection.cursor()
        cursor.execute(f"UPDATE stock SET amount = amount+{amount_1} WHERE laboratory = '{laboratory[f'{lab_1}']}' "
                       f"AND spherical = {spherical} AND cylindrical = {cylinder} AND "
                       f"material = '{lens[f'{material_1}']}'")
        conection.commit()
        print('\033[33mLente cadastrada com sucesso!\033[m')
    except:
        print('\033[31mErro ao cadastrar a lente!\033[m')
