my_str = (input('Введите цифры через запятую: '))
my_str = '1;3;4;5;2'
sep = ''
for i in my_str:
    if i.isnumeric() != True:
        sep = i
        break

my_list = my_str.split(sep)
my_list = set(my_list)

print(my_list)