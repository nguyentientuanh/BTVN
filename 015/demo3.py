class Date:
    day=0
    month=0
    year=0

    def __init__(self,day,month,year):
        self.day=day
        self.month=month
        self.year=year

    def getDay(self):
        return self.day
    def getMonth(self):
        return self.month
    def getYear(self):
        return self.year

    def setDay(self,day):
        self.day=day
    def setDay(self,month):
        self.month=month
    def setDay(self,year):
        self.year=year
        
    def setDate(self,day,month,year):
        self.day=day
        self.month=month
        self.year=year

    def toString(self):
        return str(self.day) +'/'+ str(self.month)+'/'+str(self.year)
    
homnay=Date(8,3,2024)
print(homnay.toString())