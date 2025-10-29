from array import array

def traverse(arr):
    for x in arr:
        print(x, end=" ")
    print()

def insert(arr, pos, val):
    arr.insert(pos, val)
    return arr

def delete(arr, val):
    arr.remove(val)
    return arr

def access(arr, index):
    return arr[index]

def search(arr, val):
    return arr.index(val)

def update(arr, index, val):
    arr[index] = val
    return arr


arr = array('i', [10, 20, 30, 40, 50])

traverse(arr)
arr = insert(arr, 2, 25)
print(arr)
arr = delete(arr, 40)
print(arr)
print(access(arr, 3))
print(search(arr, 30))
arr = update(arr, 1, 22)
print(arr)
