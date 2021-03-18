numbers = [1, 0, 4564, 4, 0, 48, 2, 45, 0, 0, 45, 1]  # N=12- кол-во целых чисел (размерность массива)

numbers = [num for num in numbers[:] if num != 0]  # - так можно решить задачу (окончательный ответ)

# for num in numbers:
#     if num == 0:
#         numbers.append(0)
#         numbers.remove(0)
# numbers = numbers[:len(numbers) - numbers.count(0)]
print(numbers)
