class student: # class
    def __init__(self): #constructor
        print("hello")
    def laugh(self): #method
        print("hello oops")
    def add(self,a,b):
        print(a+b)
        
s1=student() #object ##s1.init(s1)
s1.laugh()  ## s1.laugh(s1)


s2=student() 
s2.laugh() ## s2.laugh(s2)

s3=student() 
s3.laugh() ## s3.laugh(s3)

s4=student()
s4.add(1,5)
