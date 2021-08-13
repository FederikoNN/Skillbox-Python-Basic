import re

car_numbers = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'
sign_patern_private = r'\b[АВЕКМНОРСТУХ]{1}\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}'
sign_patern_taxi = r'\b[АВЕКМНОРСТУХ]{2}\d{5,6}'

print(f'Список номеров частных автомобилей: {re.findall(sign_patern_private, car_numbers)}')
print(f'Список номеров такси: {re.findall(sign_patern_taxi, car_numbers)}')
