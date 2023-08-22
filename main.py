import random

# TASK №1

expression = input("Введіть арифметичний вираз (наприклад, 23+12): ")
result = eval(expression)                                           # Використовуємо функцію яка вирішує приклад(Ламається з буквами!)
print("Результат:", result)

# TASK №2

random_list = [random.randint(-100, 100) for _ in range(20)]        # Генеруємо список з випадковими цілими числами

min_element = min(random_list)                                      # Знаходимо мінімальний і максимальний елементи
max_element = max(random_list)

negative_count = sum(1 for num in random_list if num < 0)
positive_count = sum(1 for num in random_list if num > 0)           # Рахуємо кількість від'ємних, додатних та нульових елементів
zero_count = sum(1 for num in random_list if num == 0)


print("Список випадкових чисел:", random_list)
print("Мінімальний елемент:", min_element)
print("Максимальний елемент:", max_element)                         # Виводимо результати
print("Кількість від'ємних елементів:", negative_count)
print("Кількість додатних елементів:", positive_count)
print("Кількість нулів:", zero_count)
