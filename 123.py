
#
#
#
#
#
#

n = int(input("Введите значение:"))

user_data = []
i = 0
while i < n:
    string = "Enter element" + str(i + 1) + ":"
    user_data.append(input(string))
    i += 1

print(user_data)