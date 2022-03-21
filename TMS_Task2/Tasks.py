# Создать 3 переменные с одинаковыми данными и одинаковыми идентификаторами
variable1 = 'TeachMeSkills'
variable2 = 'TeachMeSkills'
variable3 = 'TeachMeSkills'
print(id(variable1))
print(id(variable2))
print(id(variable3))
print(id(variable1) == id(variable2) == id(variable3))

# Создать 2 переменные с одинаковыми данными и разными идентификаторами
var_different_id1 = [1, 2]
var_different_id2 = [1, 2]
print(id(var_different_id1))
print(id(var_different_id2))
print(id(var_different_id1) == id(var_different_id2))

# Поменять их типы так, чтобы у 1х трех были разные идентификаторы, а у 2х последних были одинаковые
print(id(list(variable1)))
print(id(list(variable2)))
print(id(list(variable3)))
print(id(list(variable1)) == id(list(variable2)) == id(list(variable3)))

print(id(tuple(var_different_id1)))
print(id(tuple(var_different_id2)))
print(id(tuple(var_different_id1)) == id(tuple(var_different_id2)))
