# controle de estoque de lentes

from system.lens import *
import mysql.connector

try:
    while True:
        print("""    [1] para cadastrar lente.
        [2] para visualizar estoque.
        [3] para sair.""")
        option = read_whole('Digite uma opção: ')
        if option == 1:
            conection = mysql.connector.connect(host='localhost', user='root', password='', database='estoque')
            print('Option one')
            try:
                while True:
                    #  Menu
                    print("""                [1] para orgânica com AR
                    [2] para poly com AR
                    [3] para orgânica Blue Cut
                    [4] para Alto Índice
                    [5] para Zeiss Blue Protect
                    [6] para Zeiss Silver
                    [7] para Zeiss Platinum
                    [8] para reiniciar""")
                    material = int(input('Digite a opção: '))  # material option
                    if material == 1:
                        print('Add em orgânica')
                    elif material == 2:
                        print('Add em poly')
                    elif material == 3:
                        print('Add em organica blue cut')
                    elif material == 4:
                        print('Add em poly blue cut')
                    elif material == 5:
                        print('Add em alto índice')
                    elif material == 5:
                        print('Add em zeiss blue cut')
                    elif material == 6:
                        print('Add em zeiss silver')
                    elif material == 7:
                        print('Add em zeiss silver')
                    elif material == 8:
                        print('Add em zeiss platinum')
                    elif material == 9:
                        continue
            except (TypeError, ValueError):
                print('\033[31mErro ao cadastrar uma lente!\033[m')
        elif option == 2:
            print('Verificar estoque.')
        elif option == 3:
            print('\033[33mFinalizando o sistema!\033[m')
            break
        else:
            print('Entrada inválida!')
except:
    print('\033[31mERRO ao iniciar o programa!\033[m')
