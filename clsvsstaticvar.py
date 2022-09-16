class student:
    course="AI ML" #class Attribute or static attribute
    __abc="vikas"
    print(__abc)
    def __init__(self,name,year,branch):  #Setter or Mutator
        self.name=name #Instance Atrribute
        self.year=year
        self.branch=branch
        self.pin=52121
    def getattr(self): #getter or Accessor
        print(self.name,self.year,self.branch,student.course)
s1=student("ram","FY","Agri")
s2=student("sham","FY","EEE")
s1.getattr()
s2.getattr()
print(s2.course)

print(__abc)
