def is_prime(number):
    if number == 0 or number == 1:
        return False
    elif number == 2:
        return True
    else:
        for i_number in range(2, number):
            if number % i_number == 0:
                return False
        return True


def list_prime(my_object):
    return [i_object for object_index, i_object in enumerate(my_object) if is_prime(object_index) is True]


array_my = (1, 3, 5, 6, 8, 9, 2, 1, 3, 0)

new_array = list_prime(array_my)

print(new_array)
