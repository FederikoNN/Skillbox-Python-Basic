def check_ip(ip):
    for number in ip:
        if number.isdigit() is False:
            print(number + '-', 'не целое число')
            return False
        elif int(number) > 255:
            print(number, 'превышает 255')
            return False


while True:
    ip_address = input('Введите IP: ').split('.')
    if len(ip_address) != 4:
        print('Адрес - это четыре числа, разделенные точками')
    elif check_ip(ip_address) is False:  # TODO, лучше " not check_ip(ip_address)"
        continue  # TODO, лучше pass. Т.к. continue ничего не пропускает. Код отработает чуть быстрее
    else:
        print('IP-адрес корректен')

