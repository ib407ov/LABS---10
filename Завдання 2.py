# Довідник автомеханіка. База даних запчастин:
# назва запчастини, марка автомобіля, рік випуску.
# Організувати вибір за довільним запитом.
# Дані зберігаються в масиві записів, який створюється динамічно.
arreyDetails = []

def serch(choose, creteria):
    if choose == 1:
        for i in range(len(arreyDetails)):
            if arreyDetails[i]["назва запчастини"] == creteria:
                print(arreyDetails[i])

    elif choose == 2:
        for i in range(len(arreyDetails)):
            if arreyDetails[i]["марка авто"] == creteria:
                print(arreyDetails[i])

    elif choose == 3:
        for i in range(len(arreyDetails)):
            if arreyDetails[i]["рік випуску"] == creteria:
                print(arreyDetails[i])






while True:
    choise = int(input('\n1.Вивести наявність деталей\n'
              '2.Ввести деталі\n'
              '3.Вивсти деталь\n'
              '4.Закінчити\n\nВведіть число : '))

    if choise == 1:
        print()
        for i in range(len(arreyDetails)):
            print(arreyDetails[i])

    elif choise == 2:
        nameDetail = input('Деталь : ')
        nameAuto = input('Марка авто : ')
        year = input('Рік : ')

        details = {"назва запчастини": nameDetail, "марка авто": nameAuto, "рік випуску": year}
        arreyDetails.append(details)

    elif choise == 3:
        choise2 = int(input('Знайти за : \n'
              '1. Назвою\n'
              '2. Маркою\n'
              '3. Роком\n\n'
              'Введіть число : '))
        print()

        if choise2 == 1:
            charakteristic = input('Введіть назву: ')
            serch(choise2, charakteristic)

        elif choise2 == 2:
            charakteristic = input('Введіть марку: ')
            serch(choise2, charakteristic)


        elif choise2 == 3:
            charakteristic = input('Введіть рік: ')
            serch(choise2, charakteristic)


    elif choise == 4:
        break

    else:
        print('Write normal number\n')