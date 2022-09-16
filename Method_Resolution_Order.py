'''constructor behavior super() MRO LR'''
class a:  
    def __init__(self):
        print("am in a")
   
    def featuer1(self):
        print("in f1 a")     
        
class b:
    def __init__(self):        
        print("am in b")
    def featuer1(self):
        print("in f1 b")
        
class c(b,a):
    def __init__(self):
        super().__init__()
    
        print("am in c")
c1=c()
c1.featuer1()











