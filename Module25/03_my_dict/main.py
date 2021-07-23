class MyDict(dict):
    def __init__(self):
        super().__init__()

    def get(self, key):
        if key in self.keys():
            return self[key]
        else:
            return 0


families = MyDict()
families['Сидоров Никита'] = 35
families['Сидорова Алина'] = 34
families['Сидоров Павел'] = 10
print(families, type(families))
for key in families.keys():
    print(f'families.get({key}) -> {families.get(key)}')
key = 'Моня Иванов'
print(f'families.get({key}) -> {families.get(key)}')
