site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

import json


def change_sites(struct, tag, string):
    if tag in struct:
        struct[tag] = string
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = change_sites(sub_struct, tag, string)
            if result:
                break
    else:
        result = None

    return result

# TODO, Интересная идея. Молодец!
#  Пожалуйста, обратите внимание, функции для замены данных и для вывода данных обе должны включать
#  быть реализованы при помощи рекурсии. И не должны вызывать друг друга =)
def print_sites(struct, data_list):
    for data in data_list:
        tag_data = 'Куплю/продам {} недорого'.format(data)
        change_sites(struct, 'title', tag_data)
        tag_data = 'У нас самая низкая цена на {}'.format(data)
        change_sites(struct, 'h2', tag_data)
        print('Сайт для {}:'.format(data))
        print('site =', json.dumps(struct, ensure_ascii=False, indent=4))


sites_num = int(input('Сколько сайтов: '))
product = []
for _ in range(sites_num):
    site_name = (input('Введите название продукта для нового сайта: '))
    product.append(site_name)
    print_sites(site, product)

product.clear()
