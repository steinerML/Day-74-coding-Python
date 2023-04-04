class Shark:
    def __init__(self,name,age, origin):
        self.name = name
        self.age = age
        self.origin = origin
    
    def swim(self):
        print(self.name,"is swimming.")
    
    def is_awesome(self):
        print(self.name, 'is awesome')
    
    def old(self):
        print(self.name, 'is', self.age, 'years old')
    
    def sea(self):
        print(self.name, 'comes from', self.origin)

#Instance/objects creation
jimmy = Shark("Jimmy", 45, 'Atlantic Ocean')
timmy = Shark('Timmy', 14, 'Pacific Ocean')
johnny = Shark('Johnny', 27, 'Egean Sea')
peter = Shark("Peter",19, 'Black Sea')

#Calling methods for each Shark

jimmy.swim()
jimmy.is_awesome()
jimmy.old()
jimmy.sea()

timmy.swim()
timmy.is_awesome()
timmy.old()
timmy.sea()

#Modifying an attribute directly as we call a Method

johnny.swim()
johnny.is_awesome()
johnny.age = 69
johnny.origin = 'Bering Sea'
johnny.old()
johnny.sea()

peter.swim()
peter.is_awesome()
peter.old()
peter.sea()