containers = []
containers_quantity = int(input('Кол-во контейнеров: '))
container_count = 0
while containers_quantity != container_count:
    container_weight = int(input('Введите вес контейнера: '))
    if 0 > container_weight or container_weight > 200:
        print('Ошибка ввода!')
    elif container_count == 0:
        containers.append(container_weight)
        container_count += 1
    elif container_weight <= containers[container_count - 1]:
        containers.append(container_weight)
        container_count += 1
    else:
        print('Ошибка ввода!')

new_container = int(input('\nВведите вес нового контейнера: '))
for i in range(len(containers)):
    if new_container > containers[i]:
        print('\nНомер, куда встанет новый контейнер:', i + 1)
        break
