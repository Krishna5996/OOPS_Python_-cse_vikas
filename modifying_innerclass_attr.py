class student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        self.l1=self.laptop()
    def display(self):
        #self.l1.brand="hp"
        print(self.name,self.roll)
        self.l1.display()
        
    class laptop:
        def __init__(self):
            self.brand="asus"
            self.ram="8gb"
        def display(self):
            print(self.brand,self.ram)
s1=student("Ramesh",21)
s1.display()
l2=student.laptop
l2.brand="lenovo"
print(l2.brand)
l3=student.laptop
print(l2.brand)
