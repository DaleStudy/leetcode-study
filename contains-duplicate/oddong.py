a = [1, 2, 3, 5, 4]

a.sort()

print(a)
print(set(a))
print(type(set(a)))

convert_list_to_set = list(set(a))

print()
print(a)
print(convert_list_to_set)
print()

if a == convert_list_to_set:
    print(True)
else:
    print(False)