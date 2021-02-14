# controle de estoque de lentes

from system.lens import *
from datetime import date
print(date.today())

loop = False

try:
    while not loop:
        print("""    [1] para cadastrar lente.
    [2] para visualizar estoque.
    [3] para exibir as lentes que não tem em estoque.
    [4] para retirar uma lente.
    [5] para sair.""")
        option = read_whole('Digite uma opção: ')
        if option == 1:  # para registrar uma lente
            record_type = read_whole('[1] para adicionar pelo código de barras.\n'
                                     '[2] para adicionar pela dioptria.\n'
                                     '[3] para retornar ao menu anterior: \nDigite: ')
            if record_type == 1:  # adicionar atraves do codigo de barras 1 a 1
                print('[1] para registrar uma à uma.'
                      '[2] para selecionar a quantidade.')
                register_type = read_whole('Digite: ')
                if register_type == 1:
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
            elif record_type == 2:  # adicionar atraves da dioptria e do material da lente
                while True:
                    menu()
                    register_diopter('Selecione o laboratório: ', 'Selecione o material: ', 'Dioptria esférica: ',
                                     'Dioptria cilindrica: ', 'Digite a adição: ', 'Digite o lado: ',
                                     'Digite a quantidade: ')
                    opt = int(input('[1] Para cotinuar. [2] Para sair.'))
                    if opt == 1:
                        continue
                    elif opt == 2:
                        break
                    else:
                        print('Opção Inválida')
            elif record_type == 3:
                break
            else:
                print('\033[33mOpção Inváida!\033[m')
        elif option == 2:  # para pesquisar uma lente
            while True:
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
        elif option == 3:  # para exibir as lentes em falta do estoque
            while True:
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
        elif option == 4:  # para retirar uma lente do estoque
            while True:
                record_type = read_whole('[1] para retirar pelo código de barras.\n'
                                         '[2] para retirar pela dioptria.\n'
                                         '[3] para voltar ao menu anterior. \nDigite: ')
                if record_type == 1:
                    exit_code('Digite o código de barras: ', 'Digite a filal: ', 'Motivo: ')
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
        elif option == 5:
            print('\033[33mFinalizando o sistema!\033[m')
            break
        else:
            print('Entrada inválida!')
except:
    print('\033[31mERRO ao iniciar o programa!\033[m')
