def check_ip(ip):
    for number in ip:
        if number.isdigit() is False:
            print(number + '-', 'не целое число')
            return True
        elif int(number) > 255:
            print(number, 'превышает 255')
            return True


while True:
    ip_address = input('Введите IP: ').split('.')
    if len(ip_address) != 4:
        print('Адрес - это четыре числа, разделенные точками')
    elif check_ip(ip_address):
        pass
    else:
        print('IP-адрес корректен')

# зачёт!
