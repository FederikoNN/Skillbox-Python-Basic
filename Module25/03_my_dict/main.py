class MyDict(dict):
    def get(self, key):
        return dict.get(self, key, 0)


families = MyDict()
families['Сидоров Никита'] = 35
families['Сидорова Алина'] = 34
families['Сидоров Павел'] = 10
print(families, type(families))
for key in families.keys():
    print(f'families.get({key}) -> {families.get(key)}')
key = 'Моня Иванов'
print(f'families.get({key}) -> {families.get(key)}')
