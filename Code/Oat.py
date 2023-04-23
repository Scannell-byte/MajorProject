class Oat:


    def __init__(self,type,moment,area,perimeter):
        self.oatType = type
        self.moment= moment
        #self.averageRGB = averageRGB
        self.area = area
        self.perimeter = perimeter
    


    #setters
    def setMoment(self, moment):
        self.moment = moment
    
    def setAverageRGB(self,RGB):
        self.averageRGB = RGB

    def setArea(self,area):
        self.area = area
    
    def setPerimeter(self,perimeter):
        self.perimeter = perimeter

    #getters
    def getType(self):
        return(self.oatType)

    def getMoment(self):
        return(self.moment)
    
    def getAverageRGB(self):
        return(self.averageRGB)

    def getArea(self):
        return(self.area)
    
    def getPerimeter(self):
        return(self.perimeter)
