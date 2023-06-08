# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases


three_most_expensive_purchase = []
with open('test_file/task_3.txt', 'r', encoding='utf-8') as file:
    purchase = []
    for line in file:
        numm = line.replace('\n', '')
        if numm:
            purchase.append(int(numm))

purchase = sorted(purchase, reverse=True)
three_most_expensive_purchase = purchase[:3]
print(sum(three_most_expensive_purchase))
