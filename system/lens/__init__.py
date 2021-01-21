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
            print(f'\033[34mTem {r} unidade(s) no estoque.\033[m')
        conection.close()
        return True
    except:
        print('Lente não localizada no estoque!')
        return False

def register(lab, material, esf_diopter, cil_diopter, amount):
    """
    Function for lens register in the database.
    :param lab: Laboratory.
    :param material: Lens material.
    :param esf_diopter: spherical diopter.
    :param cil_diopter: cylindrical diopter.
    :param amount: Quantities added.
    :return: Register lens in the database.
    """
    import mysql.connector
    from datetime import date
    lens = {'1': '1.56_ar', '2': '1.56_blue', '3': 'poly_ar', '4': '1.67', '5': 'zeiss_blue', '6': 'zeiss_platinum',
            '7': 'zeiss_silver', '8': 'zeiss_photo'}
    laboratory = {'1': 'haytek', '2': 'zeiss'}
    data = date.today()
    try:
        lab_1 = read_whole(lab)
        material_1 = read_whole(material)
        espheric = str(input(esf_diopter))
        cilinder = str(input(cil_diopter))
        c_diopter = f'{espheric}/-{cilinder}'
        amount_1 = read_whole(amount)
        conection = mysql.connector.connect(host='localhost', user='root', password='', database='lab_carol')
        cursor = conection.cursor()
        cursor.execute(f"INSERT IGNORE INTO stock "
                       f"VALUES ('{c_diopter}', '{lens[f'{material}']}', '{laboratory[f'{lab}']}', "
                       f"'{amount_1}', '{data}')")
        conection.close()
        conection.commit()
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
    lens = {'1': '1.56_ar', '2': '1.56_blue', '3': 'poly_ar', '4': '1.67', '5': 'zeiss_blue', '6': 'zeiss_platinum',
            '7': 'zeiss_silver', '8': 'zeiss_photo'}
    laboratory = {'1': 'haytek', '2': 'zeiss'}
    lab_1 = read_whole(lab)
    material_1 = read_whole(material)
    try:
        conection = mysql.connector.connect(host='localhost', user='root', password='', database='lab_carol')
        cursor = conection.cursor()
        cursor.execute(f"SELECT diopter, data FROM stock "
                       f"WHERE material = '{lens[f'{material_1}']}' AND laboratory = '{laboratory [f'{lab_1}']}'"
                       f" AND amount = '0'")
        result = cursor.fetchall()
        print(f'\033[33mLentes com \033[31m0\033[m \033[33munidades em estoque.\033[m')
        for r in result:
            print(f'Dioptria = {r[0]} - DATA = {r[1]}')
        cursor.close()
    except:
        print(f'\033[31mErro ao pesquisar grade zerada no estoque!\033[m')
