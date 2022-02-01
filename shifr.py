# В переменной text мы используем начальную строку
text: str = input()
glasnye: str = "АУОИЭЫЯЮЕЁауоиэыяюеё"
result: str = ""
# В переменной letter будет содержатся каждая буква строки
for letter in text:
    if letter in glasnye:
        result = result + letter + 'с' + letter
    else:
        result = result + letter
print(result)
