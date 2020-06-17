def read_whole(txt):
    option = txt
    if option.isalpha():
        print('Digite o número da opção: ')
    else:
        return int(option)
