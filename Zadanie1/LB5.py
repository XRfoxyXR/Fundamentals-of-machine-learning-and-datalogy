s = input("Введите строку: ")

count = s.count("a")
new_s = s.replace("a", "")

print("Исходная строка:", s)
print("Строка после удаления:", new_s)
print("Количество удаленных букв 'а':", count)