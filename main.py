from math import factorial

if __name__ == '__main__':
    #создание и заполенение коалиционной игры
    game = {"": 0}
    # заполнение участников игры
    members = ["1","2","3"]
    #описание выигрышей коалиционной игры(номера участников разделять знаком '_')
    game["1"] = 5
    game["2"] = 15
    game["3"] = 20
    game["1_2"] = 22
    game["1_3"] = 28.5
    game["2_3"] = 38
    game["1_2_3"] = 43.5

    n = len(members)
    Sheply = {}
    for member in members:
        Sheply[member] = 0

    #для каждого игрока считаем вклад в каждую коалицию, куда он входит
    for member in members:
        list = []# массив пар элементов. Первый элемент - вклад игрока в коалицию, второй - количество игроков в  коалиции
        #рассматриваем каждую коалиции и считаем вклад игрока в неё
        for key in game.keys():
            pos = key.find(member)
            if pos != -1 and len(key) == 1:
                list.append([game[key], 1])
            if pos != -1 and len(key) > 1:
                K_temp = key.split("_")
                K_num = len(K_temp)# количество участников коалиции
                K_temp.remove(member)
                K_without_i = K_temp.pop(0)
                while len(K_temp) > 0:
                    K_without_i = K_without_i+"_"+K_temp.pop(0)
                list.append([game[key] - game[K_without_i], K_num])
        print(list)
        #подсчет каждой компоненты вектора Шепли
        for i in list:
            Sheply[member] += i[0] * factorial(i[1]-1) * factorial(n - i[1]) / factorial(n)
    print(Sheply)