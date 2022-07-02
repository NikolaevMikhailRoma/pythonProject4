my_str_1 = (input('Введите цифры через запятую: '))
# my_str_1 = '1;3;4;5;2'

sep = ''
for i in my_str_1:
    if i.isnumeric() != True:
        sep = i
        break

my_list_1 = my_str_1.split(sep)

my_str_2 = (input('Введите ещё цифры через запятую: '))
# my_str_2 = '2m3m5m6m1m5'

sep = ''
for i in my_str_2:
    if i.isnumeric() != True:
        sep = i
        break

my_list_2 = my_str_2.split(sep)

for i in my_list_2:
    if i in my_list_1:
        my_list_1.remove(i)

print(my_list_1)

