import array as a

arr=a.array('i',[1,2,3,4,5,6])
print(arr)

arr.append(45)
print(arr)

arr.insert(2,45)
print(arr)

arr.remove(4)
print(arr)

arr.pop()
print(arr)

print(arr.index(45))


print("\nLIST")

lis=["pratik","farate","dyp","digraj","sangli"]

print(lis)

lis.append("kolhapur")
print(lis)

lis.insert(2,"satara")
print(lis)

lis.remove("satara")
print(lis)

lis.pop()
print(lis)

lis.reverse()
print(lis)

print("\nDictionary")

dict={
 "name":"pratik",
 "age":21,
 "College":"dyp"

}
print(dict)

print(dict.get("name"))
print(dict.keys())
print(dict.values())
print(dict.pop("age"))
dict.update({"name":"p"})
print(dict)
print(dict.clear())

print("\nstring")
text = "hello python programming"
print("Original String:", text)

print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title Case:", text.title())
print("Replace python with java:", text.replace("python", "java"))
print("Split:", text.split())

print("\ntuple")
t = (10, 20, 30, 20, 40, 20)
print("Original Tuple:", t)

print("Count of 20:", t.count(20))
print("Index of 30:", t.index(30))
print("Length:", len(t))
print("Max value:", max(t))
print("Min value:", min(t))

print("\nset")
s = {10, 20, 30, 40}
p = {10,30,40,50,60}
print("Original Set:", s)
print("Original Set:", p)


s.add(50)
print("After add(50):", s)

s.remove(20)
print("After remove(20):", s)

s.discard(100)
print("After discard(100):", s)

print("Union", s.union({p})) 	
print("Intersection with {40,50,80}:", s.intersection({40, 50, 80}))


























