# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.

x = int(input('Сколько километров пробежали за 1 день? '))
y = int(input('Не менее скольки километров Вы пробежали? '))
day = 0
while y - x >= 0:
    x = x + (x * 0.1)
    day += 1
print(day)
