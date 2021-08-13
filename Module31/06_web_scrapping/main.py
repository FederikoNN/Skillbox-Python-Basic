import re
import requests

html = input('Введите адрес страницы: ')
tag = input('Какой тег будем искать? ')
pattern = f'<{tag}.*>(.*)</{tag}>'
html_req = requests.get(html)
result = re.findall(pattern, html_req.text)
print(result)
