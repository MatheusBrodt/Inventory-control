# controle de estoque de lentes

from system.lens import *
lens = {'1': '1.56_ar', '2': '1.56_blue', '3': 'poly_ar', '4': '1.67', '5': 'zeiss_blue', '6': 'zeiss_platinum',
        '7': 'zeiss_silver', '8': 'zeiss_photo'}
laboratory = {'1': 'haytek', '2': 'zeiss'}

try:
    while True:
        print("""    [1] para cadastrar lente.
    [2] para visualizar estoque.
    [3] para exibir as lentes que não tem em estoque.
    [4] para sair.""")
        option = read_whole('Digite uma opção: ')
        if option == 1:
            while True:
                menu()
                register('Selecione o labortório: ', 'Selecione o material: ', 'Digite a dioptria esferica: ',
                         'Digite a dioptria cilindrica: ', 'Digite a quantidade: ')
                opt = int(input('[1] Para cotinuar. [2] Para sair.'))
                if opt == 1:
                    continue
                elif opt == 2:
                    break
                else:
                    print('Opção Inválida')
        elif option == 2:
            while True:
                menu()
                search('Selecione o laboratório: ', 'Selecione o material: ', 'Digite a dioptria esférica: ',
                       'Digite a dioptria cilindríca: ')
                pesq_option = read_whole('Continuar pesquisando 1 > S / 2 > N: ')
                if pesq_option == 1:
                    continue
                elif pesq_option == 2:
                    break
                else:
                    print('\033[31mOpção Inválida!\033[m')
                    continue
        elif option == 3:
            while True:
                menu()
                zero('Selecione o laboratório: ', 'Selecione o material: ')
                pesq_option = read_whole('Continuar pesquisando 1 > S / 2 > N: ')
                if pesq_option == 1:
                    continue
                elif pesq_option == 2:
                    break
                else:
                    print('\033[31mOpção Inválida!\033[m')
                    continue
        elif option == 4:
            print('\033[33mFinalizando o sistema!\033[m')
            break
        else:
            print('Entrada inválida!')
except:
    print('\033[31mERRO ao iniciar o programa!\033[m')
