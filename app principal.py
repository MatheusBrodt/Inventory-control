# controle de estoque de lentes

from system.lens import *
import mysql.connector
import datetime

data = datetime.date.today()
lens = {'1': '1.56_ar', '2': '1.56_blue', '3': 'poly_ar', '4': '1.67', '5': 'zeiss_blue', '6': 'zeiss_platinum',
        '7': 'zeiss_silver', '8': 'zeiss_photo'}
laboratory = {'1': 'haytek', '2': 'zeiss'}

try:
    while True:
        print("""    [1] para cadastrar lente.
    [2] para visualizar estoque.
    [3] para sair.""")
        option = read_whole('Digite uma opção: ')
        if option == 1:
            while True:
                print(f'\033[33mLentes\033[m\n'
                      f'1 > {lens["1"]}\n'
                      f'2 > {lens["2"]}\n'
                      f'3 > {lens["3"]}\n'
                      f'4 > {lens["4"]}\n'
                      f'5 > {lens["5"]}\n'
                      f'6 > {lens["6"]}\n'
                      f'7 > {lens["7"]}\n'
                      f'8 > {lens["8"]}\n')
                print(f'\033[33mLaboratórios\033[m\n'
                      f'1 > {laboratory["1"].capitalize()}\n'
                      f'2 > {laboratory["2"].capitalize()}\n')
                lab = read_whole('Digite o laboratório: ')
                material = read_whole('Material da lente: ')
                diopter = str(input('Digite a diotria da lente: '))
                amount = read_whole('Digite a quantidade de lente: ')
                conection = mysql.connector.connect(host='localhost', user='root', password='', database='lab_carol')
                cursor = conection.cursor()
                cursor.execute(f"INSERT IGNORE INTO stock "
                               f"VALUES ('{diopter}', '{lens[f'{material}']}', '{laboratory[f'{lab}']}', "
                               f"'{amount}', '{data}')")
                opt = int(input('[1] Para cotinuar. [2] Para sair.'))
                if opt == 1:
                    continue
                elif opt == 2:
                    break
                else:
                    print('Opção Inválida')
        elif option == 2:
            while True:
                print('Pesquisa de Lentes!')
                print(f'\033[33mLentes\033[m\n'
                      f'1 > {lens["1"]}\n'
                      f'2 > {lens["2"]}\n'
                      f'3 > {lens["3"]}\n'
                      f'4 > {lens["4"]}\n'
                      f'5 > {lens["5"]}\n'
                      f'6 > {lens["6"]}\n'
                      f'7 > {lens["7"]}\n'
                      f'8 > {lens["8"]}\n')
                print(f'\033[33mLaboratórios\033[m\n'
                      f'1 > {laboratory["1"].capitalize()}\n'
                      f'2 > {laboratory["2"].capitalize()}\n')
                try:
                    lab = read_whole('Digite o laboratório: ')
                    material = read_whole('Material da lente: ')
                    diopter = str(input('Digite a dioptria da lente: '))
                    conection = mysql.connector.connect(host='localhost', user='root', password='', database='lab_carol')
                    cursor = conection.cursor()
                    cursor.execute(f"SELECT amount FROM stock "
                                   f"WHERE diopter = '{diopter}' AND material = '{lens[f'{material}']}'"
                                   f" AND laboratory = '{laboratory[f'{lab}']}'")
                    print('checkpoint')
                    result = cursor.fetchone()
                    for r in result:
                        print(f'\033[34mTem {r} unidade(s) no estoque.\033[m')
                except:
                    print('\033[mLente não encontrada\033[m')
                    continue
                else:
                    pesq_option = read_whole('Continuar pesquisando 1 > S / 2 > N: ')
                    if pesq_option == 1:
                        continue
                    elif pesq_option == 2:
                        break
                    else:
                        print('\033[31mOpção Inválida\033[m')
                        break
        elif option == 3:
            print('\033[33mFinalizando o sistema!\033[m')
            break
        else:
            print('Entrada inválida!')
except:
    print('\033[31mERRO ao iniciar o programa!\033[m')
