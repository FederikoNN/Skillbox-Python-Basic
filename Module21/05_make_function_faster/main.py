fact_result = [1]


# TODO, стоит добавить в функцию параметр с пустым словарём, как значение по умолчанию,
#  и добавлять в него факториал числа.
#  Если мы уже производили вычисление факториала числа, повторно производить не нужно,
#  стоит просто взять факториал из словаря и использовать его в остальных вычислениях. =)
#  Список fact_result вне функции, получился лишним.

def calculating_math_func(data, data_max=1):
    print(data_max)
    if data > data_max:
        result = max(fact_result)
        for index in range(data_max, data + 1):
            result *= index
            fact_result.append(result)
    else:
        result = fact_result[data]
    result /= data ** 3
    result = result ** 10
    return result


while True:
    number = int(input('Введите число: '))
    print('Результат:', calculating_math_func(number, len(fact_result)))
    print(fact_result)
