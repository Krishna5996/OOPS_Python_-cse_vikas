class base:
    def __init__(self):
        self.__som=15
        print(self.__som)
     
class derived(base):
    def __init__(self):       
        print(self.__som)
 
u1=base()
#private members can not access in subclass or out of the class
d1=derived()
print(u1.__som)
  

