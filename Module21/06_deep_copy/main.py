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


def print_struct(struct, tab=1):
    for key, value in struct.items():
        print('\t' * tab + '\'{}\''.format(key) + ':', end=' ')
        if isinstance(value, dict):
            print('{')
            print_struct(value, tab + 1)
        else:
            print('\'{}\''.format(value))
    print('\t' * (tab - 1) + '}')


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


sites_num = int(input('Сколько сайтов: '))
product = []
for _ in range(sites_num):
    site_name = (input('Введите название продукта для нового сайта: '))
    product.append(site_name)
    for i_product in product:
        tag_data = 'Куплю/продам {} недорого'.format(i_product)
        change_sites(site, 'title', tag_data)
        tag_data = 'У нас самая низкая цена на {}'.format(i_product)
        change_sites(site, 'h2', tag_data)
        print('Сайт для {}:'.format(i_product))
        print('site = {')
        print_struct(site)

product.clear()
