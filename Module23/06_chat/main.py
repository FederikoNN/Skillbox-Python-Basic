import os


def chat_view(path):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                print(line, end='')
    else:
        raise FileNotFoundError('История чата отсутствует/ошибка доступа.')


def send_msg(path, info):
    if os.path.exists(path):
        msg = input('Ваше сообщение: ')
        with open('chat.txt', 'a+', encoding='utf-8') as file:
            file.write(f'{info}: {msg}\n')
    else:
        raise FileNotFoundError('Ошибка доступа к чату')


user_name = input('Введите имя пользователя: ')
path_to_chat = os.path.abspath('chat.txt')
while True:
    try:
        print('Что Вы хотите сделать:')
        print('1. Посмотреть текущий текст чата.')
        print('2. Отправить сообщение')
        choice = int(input())
        if choice == 1:
            chat_view(path_to_chat)
        elif choice == 2:
            send_msg(path_to_chat, user_name)
        else:
            raise ValueError
    except ValueError as msg:
        print('Повторите выбор.')
    except FileNotFoundError as msg:
        print(msg)
    except IOError:
        print('то-то пошло не так')

# зачёт!
