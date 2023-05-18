# Дан список из 7 различных элементов. Используя функции (не использовать цикл), необходимо найти:
# минимальный и максимальный элементы списка;
# сумму и среднее арифметическое с округлением до 2 знаков после запятой;

from statistics import mean
def get_list_info(lst):
    min_elemnt = min(lst)
    max_elemnt = max(lst)
    sum_list = sum(lst)
    average = round(sum(lst) / len(lst), 2)
    return min_elemnt, max_elemnt, sum_list, average

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    [1, 2, 3, 4, 5, 6, 7],
    [-1, -2, -3, -4, -5, -6, -7],
    [99, 56, 209, -308, -12, -18, 42],
    [-1, -2, -3, 0, 1, 2, 3],
]

test_data = [
    (1, 7, 28, 4.0), (-7, -1, -28, -4.0), (-308, 209, 68, 9.71), (-3, 3, 0, 0.0)
]


for i, d in enumerate(data):
    assert get_list_info(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
