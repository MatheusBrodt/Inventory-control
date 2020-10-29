def read_whole(txt):
    try:
        loop = False
        while not loop:
            validate = str(input(txt)).replace(',', '.')
            if validate.isalpha() or validate.isspace():
                print('Digite o número da opção: ')
                continue
            else:
                loop = True
                return int(validate)
    except (ValueError, TypeError):
        print('\033[33mErro ao identificar o valor digitado na opção.\033[m')
