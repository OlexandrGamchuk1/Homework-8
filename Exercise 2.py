lst1 = [i for i in range(3, 1000, 3)]
lst2 = [i for i in range(5, 1000, 5)]
print(list(set(lst1) & set(lst2)))