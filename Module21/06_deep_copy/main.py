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


def print_sites(struct, data_list):
    for data in data_list:
        struct['html']['head']['title'] = 'Куплю/продам {} недорого'.format(data)
        struct['html']['body']['h2'] = 'У нас самая низкая цена на {}'.format(data)
        print('Сайт для {}:'.format(data))
        print('site =', json.dumps(struct, ensure_ascii=False, indent=4))


sites_num = int(input('Сколько сайтов: '))
product = []
for _ in range(sites_num):
    product.append(input('Введите название продукта для нового сайта: '))
    print_sites(site, product)
product.clear()
