from re import search

while True:
    print("\n -- Password manager --")

    print("1. Додати пароль - ")
    print("2. Переглянути всі паролі -")
    print("3. Пошук пароля -")
    print("4. Вихід.")

    choice = input("Обери один з варіантів від 1-4:")

    if choice == "1":
        print("обрали додати пароль")
        serviсe = input("Яка соціальна мережа?")
        password = input(f"Який пароль до {serviсe}?")

        with open("passwords", 'a', encoding="utf-8") as file:
            file.write(f"{serviсe} - {password}\n" )
        print(f"додано пароль до {serviсe}!")



    elif choice == "2":
        print("обрали Переглянути всі паролі")
        try:
            with open("passwords.txt", "r", encoding="utf-8") as file:
                for line in file:
                    # Розрізаємо рядок на частини за розділювачем |
                    parts = line.split("|")
                    if len(parts) == 2:
                        serv = parts[0].strip()
                        pw = parts[1].strip()
                        print(f"Сервіс: {serv} ---> Пароль: {pw}")
        except FileNotFoundError:
            print("База паролів ще не створена.")


    elif  choice == "3":
        print("обрали Пошук пароля")
        search_servise = input("Напишіть назву сервісу?").lower()#lower- з маленької шукало

        found = False
        try:
            with open("passwords", 'r', encoding="utf-8") as file:
                for parol in file:
                    if "Інстаграм" in parol:
                        print(parol)
            if not found:
                print("Такого сервісу не знайдено!")


        except FileNotFoundError:
            print("Файл з паролями не створено!!")


    elif  choice == "4":
        print("Вихід")
        break

    else:
        print("неправильний вибір, оберіть від 1-4!!!")

