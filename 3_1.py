# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def div(*args):

    try:
        number_one = int(input("Введите первое число: "))
        number_two = int(input("Введите второе число: "))
        score = number_one / number_two

    except ValueError:
        return "Value error"

    except ZeroDivisionError:
        return "Деление на ноль"
    return score


print(f'result  {div()}')





