# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

production_in_hours, rate_per_hour, bonus = argv
try:
    production_in_hours = int(production_in_hours)
    rate_per_hour = int(rate_per_hour)
    bonus = int(bonus)
    res = production_in_hours * rate_per_hour + bonus

    print(f'заработная плата сотрудника  {res}')
except ValueError:
    print('Not a number')


