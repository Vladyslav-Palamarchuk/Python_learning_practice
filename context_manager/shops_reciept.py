menu = {"хліб": 20, "молоко": 40, "яблуко": 30, "сік": 50}
total_price = 0
receipt = []

print("Вітаю у магазині!")
print(f"Сьогоднішнє меню {list(menu.keys())}")


while True:
    shops = input("Введіть товар або -оплата- для чеку?")

    if shops == "оплата":
        break

    if shops in menu:
        price = menu[shops]
        try:
            quantity = int(input(f"Яка кількість '{shops}'? "))

            cost = price * quantity
            total_price += cost


            receipt.append(f"{shops} x {quantity} = {cost} грн")
            print("Додано до кошика!")

        except ValueError:
            print("Помилка! Введіть кількість цифрами.")
            continue
    else:
        print("На жаль, такого товару немає.")


with open("receipt.txt", 'w', encoding="utf-8") as file:
    file.write("---  ВАШ ЧЕК  ---\n")
    for line in receipt:
        file.write(line + "\n")
    file.write(f"Разом: {total_price} грн \n")