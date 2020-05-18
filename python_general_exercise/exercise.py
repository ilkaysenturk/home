
array = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
tuple = (1,2,3)
if "appel" in array:
    print("yes")
else:
    print("no")
var="1"
tuple3=array+tuple

print(type(array))
print(type(var))
print(tuple3)

print(array.count("melon"))

print(array.len())
####




cars={"brand": "ford",
      "model": "mustang",
      "year": "1964"}
array=[1,2,3,4,5,6]
array[5]=7
print(array)

for x in cars:
    print(cars[x])

for y in array[0:3]:
    print(y)

for x,y in cars.items():
    print(x,y)

if "model" in cars:
    print("mustang is exist in cars")

    print(len(cars))
cars["color"]="red"
print(cars)

del cars["model"]

print(cars)


new_cars=cars.copy()
print(new_cars)



ChildrenList={
"child1":{"name":"ilkay",
           "age":"43"},
"child2":{"name":"ahmet",
           "age":"40"},
"child3":{"name":"mehmet",
           "age":"27"}
 }

print(ChildrenList)
