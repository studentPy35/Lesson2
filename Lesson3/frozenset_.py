myset1 = frozenset([1, 1, 2, 3, 4, 4, 4, 5, 6, 6])
myset2 = frozenset('aabcccddee')

print(myset1)
print(myset2)


print(myset2.union(myset1))


print(myset2.intersection(myset1))
