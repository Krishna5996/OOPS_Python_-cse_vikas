class Person(object):
       
    # Constructor
    def __init__(self, name):
        self.name = name
   
    # To get name
    def getName(self):
        return self.name
   
    # To check if this person is an employee
    def display(self):
        return False
    def sample(self):
        print("sample method in base class")
   
   
# Inherited or Subclass (Note Person in bracket)
class Employee(Person):
   
    # Here we return true
    def isEmployee(self):
        return True
   
# Driver code
p1 = Person("Geek1")  # An Object of Person
#int(p1.getName(), p1.display())
e1=Employee("e1")
e1.sample()

'''  
e1 = Employee("Geek2") # An Object of Employee
print(e1.getName(), e1.isEmployee())

e2=Employee("Yourname")
e2.sample()
'''


