class student:
    clg_name="vikas"
    def __init__(self,m1):
        self.m1=m1
    @classmethod
    def info(cls):
        return cls.clg_name
    @staticmethod
    def show():
        return 48

s1=student(15)
print(student.info())
print(student.show())
