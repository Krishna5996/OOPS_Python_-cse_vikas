#Assigning instance variable using constructor
class student:
    clg_name='Vikas' #class attribute
    def __init__(self,idd,name,no): #setters/Mutator
        self.idd=idd #instance variables
        self.sname=name
        self.roll=no
    def setter(self,busno): #Attribute setter method
        self.bus=busno     
         
 
    # A sample method 
    def display(self): #getters/accessor
        print("student id",self.idd)
        print("student name",self.sname)
        print("student roll no",self.roll)
        print("student bus no",self.bus)
        #print("clg name",self.clg)   


s1 = student("1","virat","001")
s2=student("2","sachin","002")
s1.setter("308")
print("accessed using class name",student.clg_name)
print("accessed using object name",s1.clg_name)
s1.display() #display(s1)
print(s2.roll)
print(s1.roll)
print("accessing class variable out of class",student.clg_name)
















