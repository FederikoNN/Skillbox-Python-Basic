families = {
    'Сидоров Никита': 35,
    'Сидорова Алина': 34,
    'Сидоров Павел': 10
}
surname = input('Введите фамилию: ').lower()
if surname.endswith('а'):
    surname = surname[:-1]
for name in families.keys():
    if surname in name.lower():
        print(name, families.get(name))
