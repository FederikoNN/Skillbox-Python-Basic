def calculating_math_func(data, fact_result=None):  # TODO, вместо None стоит указать {}

    # TODO, блок if ниже получился лишний =)
    if fact_result is None:
        fact_result = {0: 1}
    if data > len(fact_result) - 1:
        result = fact_result[len(fact_result) - 1]
        for index in range(len(fact_result), data + 1):
            result *= index
            fact_result[int(index)] = result  # TODO, index приводить к числе ну нужно, т.к. и так число =)

    else:
        result = fact_result[data]

    result /= data ** 3
    result = result ** 10
    return result


while True:
    number = int(input('Введите число: '))
    print('Результат:', calculating_math_func(number))
