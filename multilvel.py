class greatgrandparent:
    def z(self):
        print("in greatgrandparent")
 
class grandparent(greatgrandparent):
    def a(self):
        print("in grandparent")
class parent(grandparent):
    def b(self):
        print("in parent")
    
class child(parent):
    def c(self):
        print("in child")
c1=child()
c1.z()
    

    
