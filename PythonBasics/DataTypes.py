# List - Mutable
print("----------List----------")
values_list = [1, 2, "Sajan", 4, 5]

print(values_list[0])            # 1
print(values_list[2])            # Sajan
print(values_list[-1])           # 5
print(values_list[1:4])          # [2, 'Sajan', 4]

values_list.insert(3, "Sunny")
print(values_list)               # [1, 2, 'Sajan', 'Sunny', 4, 5]
values_list.append("End")
print(values_list)               # [1, 2, 'Sajan', 'Sunny', 4, 5, 'End']

values_list[2] = "SAJAN"
print(values_list)               # [1, 2, 'SAJAN', 'Sunny', 4, 5, 'End']

del values_list[0]
print(values_list)               # [2, 'SAJAN', 'Sunny', 4, 5, 'End']


# Tuple - Immutable
print("----------Tuple----------")

values_tuple = (1, 2, "Sajan", 4.5)
print(values_tuple[1])                 # 2

# values_tuple[2] = "SAJAN"              # TypeError: 'tuple' object does not support item assignment



# Dictionary
print("----------Dictionary----------")

dic = {"a": 2, 4: "abc", "c": "Hello world"}
print(dic[4])
print(dic["c"])

Person = {}
print(Person)

Person["Name"] = "Sajan"
Person["Age"] = 29
Person["Gender"] = "Male"
print(Person)
print(Person["Name"])

