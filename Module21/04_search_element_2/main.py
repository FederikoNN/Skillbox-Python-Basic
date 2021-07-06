site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find_key(struct, key, levels=1001, count_level=0):
    if count_level > levels:
        return None
    elif key in struct:
        return struct[key]

    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key, levels, count_level=count_level + 1)
            if result:
                break

    else:
        result = None

    return result


value = ''
user_key = input('Какой ключ ищем? ')
depth_level = int(input('Глубина поиска (0- по умолчанию): '))
if depth_level == 0:
    value = find_key(site, user_key)
else:
    value = find_key(site, user_key, depth_level)

if value:
    print(value)
else:
    print('Ключ не найден!')
