class person:

    def __init__(self, name, age):
        self.name=name
        self.age=age

    def my_funcion(self):
      print("class object presentation "+self.age)

p1=person("ilkay","43")
p2=person("melis","12")
p3=person("mete","8")
p4=person("serpil","45")

class student(person):
    pass
