fact_result = [1]


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
