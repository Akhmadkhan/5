print("Здесь вы можете конвертировать единицы измерения температуры.")

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    while True:
        print("Выберите опцию:")
        print("1. Конвертировать из градусов Цельсия в градусы Фаренгейта")
        print("2. Конвертировать из градусов Фаренгейта в градусы Цельсия")
        print("3. Выйти")

        option = input("Введите номер опции: ")

        if option == "1":
            celsius = float(input("Введите градусы Цельсия: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius} градусов Цельсия = {fahrenheit} градусов Фаренгейта")
        elif option == "2":
            fahrenheit = float(input("Введите градусы Фаренгейта: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit} градусов Фаренгейта = {celsius} градусов Цельсия")
        elif option == "3":
            print("До свидания!")
            break
        else:
            print("Неверный номер опции. Попробуйте снова.")

if __name__ == "__main__":
    main()
