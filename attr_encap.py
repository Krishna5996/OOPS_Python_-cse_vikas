class update:
    def __init__(self):
        self.name='bill'# public
        self.__firstversion="pytohn 2.7" #private
        #self.update_software()
    def update_software(self):
        print("updating")
        print(self.__firstversion) #private
        print(self.name)    #public
u1=update()
u1.__firstversion="python3.7"
print(u1.__firstversion)
u1.name='steve'
print(u1.name)
u1.update_software()

