from array import array

arr = array('i', [10, 20, 30, 40, 50])

print(list(map(lambda x: x, arr)))

arr.insert(2, 25)
print(arr)

arr.remove(40)
print(arr)

print((lambda a, i: a[i])(arr, 3))

print(list(filter(lambda x: x == 30, arr)))

update = lambda a, i, v: a.__setitem__(i, v) or a
arr = update(arr, 1, 22)
print(arr)
