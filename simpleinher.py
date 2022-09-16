class Person: #base/parent/super class
       
      
    def sample(self):
        print("sample method in base class")
   
   
# Inherited or Subclass (Note Person in bracket)
class Employee(Person): #derived/child/sub class
    pass

p1 = Person()  # An Object of Person
e1=Employee()
e1.sample()




