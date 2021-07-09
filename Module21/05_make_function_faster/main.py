def calculating_math_func(data, fact_result={0: 1}):
    if data in fact_result.keys():
        result = fact_result[data]
    else:
        result = fact_result[max(fact_result.keys())]
        for index in range(max(fact_result.keys()) + 1, data + 1):
            result *= index
            fact_result[index] = result

    result /= data ** 3
    result = result ** 10
    return result


while True:
    number = int(input('Введите число: '))
    print('Результат:', calculating_math_func(number))
