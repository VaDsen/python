# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

my_list = [14, 12, 3100, 123, 71, 53, 64, 130]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]

print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')

# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.

print(f'Числа от 20 до 240 кратные 20 или 21 - {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')