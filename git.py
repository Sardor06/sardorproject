def kavadrat(son):
    return son*son
my_tuple = (10, 4, 3, 5, 6, 7, 4, 1)
l = list(map(kavadrat, list(my_tuple)))
l.sort()
print(l)