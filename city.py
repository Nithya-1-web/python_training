#class 
class city:
    def addcitydetails(self,name,country):
        self.name = name
        self.country = country

    def printcitydetails(self):
        print("city name:" + self.name)
        print("country:" + self.country)


# object creation
# delhi = city()
# # calling the method 
# delhi.addcitydetails("delhi","india")
# delhi.printcitydetails()        
        
# mumbai = city()
# # calling the method 
# mumbai.addcitydetails("mumbai","india")
# mumbai.printcitydetails()        
        
karnataka = city()
# calling the method
karnataka.addcitydetails("karnataka","india")
karnataka.addcitydetails("london","india")
karnataka.printcitydetails()