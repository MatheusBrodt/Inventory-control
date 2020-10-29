import mysql.connector

#  criando tabela do banco de dados

esferico = cilindro = pecas = cont = 0
try:
    conection = mysql.connector.connect(host='localhost', user='root', password='', database='estoque')
    cursor = conection.cursor()
    while True:
        cilindro -= float(0.25)
        cursor.execute(f"INSERT INTO positivo_alto_indice (esferico, cilindrico, pecas) "
                       f"VALUES ('{esferico:.2f}', '{cilindro:.2f}', '{pecas}')")
        cont += 1
        print(f'{esferico:.2f} / {cilindro:.2f}')
        print(cont)
        if cilindro == -4:
            esferico -= float(0.25)
            cilindro = 0
        elif esferico == -4.50:
            conection.commit()
            conection.close()
            break
except:
    print('\033[31mERRO\033[m')
else:
    print('\033[32mBanco de Dados criado com sucesso!\033[m')