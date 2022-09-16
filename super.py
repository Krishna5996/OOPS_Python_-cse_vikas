class a:
    def __init__(self):
        print("in a")
        
class b(a):
    def __init__(self):
        super().__init__() 
    #pass
b1=b()
