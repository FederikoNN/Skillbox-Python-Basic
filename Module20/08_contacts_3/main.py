phone_book = {}

while True:
    choice = int(input('Добавить контакт/Найти контакт(1/0): '))
    if choice == 1:
        print('Добавление контакта')
        name = input('Введите имя и фамилию: ')
        phone = input('Введите номер телефона: ')
        if name in phone_book.keys():
            print('Изменена запись для', name)
        phone_book[name] = phone
        print(phone_book)
    elif choice == 0:
        print('Поиск в телефонной книге')
        name = input('Введите фамилию: ').lower()
        for entry in phone_book.keys():
            if name in entry.lower():
                print(entry, phone_book.get(entry))
        print('Поиск завершен!')

# зачёт!
