number = int(input('Введите кол-во элементов: '))

my_list = []
for i in range (0, number):
    elem = input('Элемент номер {}:'.format(i))
    my_list.append(elem)

my_list.sort()
print(my_list)

