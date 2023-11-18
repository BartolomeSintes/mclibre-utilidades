my_list = [20, 30, 40]
print("1", my_list)
for i in range(len(my_list)):
    my_list[i] = my_list[i] + 1
print("1", my_list)

my_list = [20, 30, 40]
print("2", my_list)
for i in range(len(my_list) - 1, -1, -1):
    if my_list[i] == 30:
        del my_list[i]
    else:
        my_list[i] = my_list[i] + 1
print("2", my_list)

my_list = [20, 30, 40]
print("3", my_list)
for index, value in enumerate(my_list[::-1]):
    rev_index = len(my_list) - 1 - index  # Calculate the original index from reversed iteration
    if value == 30:
        del my_list[rev_index]
    else:
        my_list[rev_index] = value + 1
print("3", my_list)

# Incorrecto
# my_list = [20, 30, 40]
# print("4", my_list)
# for index, value in enumerate(my_list[::-1]):
#     if value == 30:
#         del my_list[index]
#     else:
#         my_list[index] = value + 1
# print("4", my_list)


# Resultado incorrecto
my_list = [20, 30, 40]
print("5", my_list)
for index, value in enumerate(my_list):
    rev_index = len(my_list) - 1 - index  # Calculate the original index from reversed iteration
    if value == 30:
        del my_list[rev_index]
    else:
        my_list[rev_index] = value + 1
print("5", my_list)
