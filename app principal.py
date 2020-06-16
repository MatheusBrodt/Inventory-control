
try:
    while True:
        print("""        [1] para orgânica
        [2] para poly
        [3] para orgânica blue cut
        [4] para poly blue cut
        [5] para alto índice
        [6] para zeiss blue protect
        [7] para zeiss silver
        [8] para zeiss platinum
        [9] para reiniciar""")
        material = int(input('Digite a opção: '))
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
        else:
            print('Saindo do sistema')
except TypeError:
    print('Erro!')