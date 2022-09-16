class student:
    clg_name="vikas"
    def __init__(self,m1):
        self.m1=m1
    def a(self):
        pass
    @classmethod
    def info(cls):
        return cls.clg_name
    @staticmethod
    def show():
        return 48

s1=student(15)
print(s1.show())
print(student.clg_name)
print(student.show())
