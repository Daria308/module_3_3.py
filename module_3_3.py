# Создаём функцию print_params
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params(b = 25)
print_params(c = [1,2,3])
# распаковка параметров
values_list = ['Магнолия', 1985, [1, 2, 3]]
values_dict = {'a': [1, 2, 3], 'b': 'Магнолия', 'c': 1985}
print_params(*values_list)
print_params(**values_dict)
# Распаковка + отдельные параметры:
values_list_2 = ['Фиалка', [4, 5, 6]]
print_params(*values_list_2, 42)