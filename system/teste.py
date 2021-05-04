from datetime import datetime

str_data = '2021-06-01'

data = datetime.strptime(str_data, '%Y-%m-%d').date()

print(data)

data_hoje = datetime.date(datetime.today())
print(data_hoje)

if data < data_hoje:
    print('Menor')
else:
    print('Maior')
