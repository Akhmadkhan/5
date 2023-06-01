print("Здесь вы можете конвертировать")


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def main():
    while True:
        print("Выберите опцию:")
        print("1. Конвертировать из г. C в г. F")
        print("2. Конвертировать из г. C в г. F")
        print("3. Выйти")

        option = input("Введите номер опции: ")

        if option == "1":
            celsius = float(input("Введите г. C: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius} г. C = {fahrenheit} г. F")
        elif option == "2":
            fahrenheit = float(input("Введите г. F: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit} г. F = {celsius} г. C")
        elif option == "3":
            print("До свидания!")
            break
        else:
            print("Неверный номер опции. ")


if __name__ == "__main__":
    main()
