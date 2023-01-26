l1 = [x**3 for x in range(10)]
print(l1)

l2 = filter(lambda x: not x%2, l1)
print(l2)

l3 = map(lambda x: x*3, l2)
print(l3)
