Workers1 = {"Pass": "", "Osvita": 0, "Specialnist": "", "Posada": 0, "Oklad": 0}
arrayWorkers = []

def serch(choose, criteria):
    if choose == 1:
        for i in range(len(arrayWorkers)):
            if arrayWorkers[i]["Pass"] == criteria:
                print(arrayWorkers[i])
    if choose == 2:
        for i in range(len(arrayWorkers)):
            if arrayWorkers[i]["Osvita"] == criteria:
                print(arrayWorkers[i])
    if choose == 3:
        for i in range(len(arrayWorkers)):
            if arrayWorkers[i]["Specialnist"] == criteria:
                print(arrayWorkers[i])
    if choose == 4:
        for i in range(len(arrayWorkers)):
            if arrayWorkers[i]["Posada"] == criteria:
                print(arrayWorkers[i])

    if choose == 5:
        for i in range(len(arrayWorkers)):
            if arrayWorkers[i]["Oklad"] == criteria:
                print(arrayWorkers[i])


while True:
    print("\n")
    print("1. Вивести всю інформацію\n"
          "2. Ввести данні about worker\n"
          "3. Знайти workera\n"
          "4. Вийти\n")

    choose = int(input("Виберіть номер:"))

    if choose == 1:
        print()
        for i in range(len(arrayWorkers)):
            print(arrayWorkers[i])

    elif choose == 2:
        Dani = int(input('Pass : '))
        Osvita = input('Osvita :')
        Specialnit = input('Specialnist : ')
        Posada = input('Posada : ')
        Oklad = input('Oklad : ')

        Workers1 = {"Pass": Dani, "Osvita": Osvita, "Specialnist": Specialnit, "Posada": Posada, "Oklad": Oklad}

        # Workers1["Pass"] = Dani
        # Workers1["Osvita"] = Osvita
        # Workers1["Specialnist"] = Specialnit
        # Workers1["Posada"] = Posada
        # Workers1["Oklad"] = Oklad
        arrayWorkers.append(Workers1)
        print(Workers1)
        print(arrayWorkers)

    elif choose == 3:
        print("Знайти за:\n"
              "1.Паспортом\n"
              "2.Освітою\n"
              "3.Спеціальністю\n"
              "4.Посала\n"
              "5.Оклад\n")

        choose2 = int(input('Введыть критерій : '))
        if choose2 == 1:
            characteristic = int(input())
            serch(1, characteristic)

        elif choose2 == 2:
            characteristic = input()
            serch(2, characteristic)

        elif choose2 == 3:
            characteristic = input()
            serch(3, characteristic)

        elif choose2 == 4:
            characteristic = input()
            serch(4, characteristic)

        elif choose2 == 5:
            characteristic = input()
            serch(5, characteristic)

    elif choose == 4:
        break
    else:
        print('Write norlmal number\n')