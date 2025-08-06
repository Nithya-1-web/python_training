def printname(self,name):
    print(name)
  

class person():
    cityname = "mumbai"
    def printname(self,name):
        print(name)

class ashok(person):
    def printdetails(self):
        print("some message")

class anu(person):
    def printdetails(self):
        print("some message")


obj = ashok()
obj.cityname = "new city"
obj.printname("ashok")

obj1 = anu()
obj.cityname = "london"
obj.printname("anu")



        


    