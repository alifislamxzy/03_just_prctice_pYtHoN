class Employee:
    name = "Alif"
    def getInfo(self, name):
        print(f"Hello {self,name}")
    
class Man(Employee):
    def getcode(self):
        print("Hello moon")


e = Employee()
m = Man()

m.getcode()
