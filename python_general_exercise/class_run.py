import class_in

print(class_in.p1.age)
print(class_in.p2.name)

class_in.p1.my_funcion() # Calling the objext module.object.function
class_in.p4.age=40  #updating the existing objects attribute

print(class_in.p4.age)

x=class_in.person("hegele","22") #Calling the person class to create object outside of the class
x.my_funcion()
