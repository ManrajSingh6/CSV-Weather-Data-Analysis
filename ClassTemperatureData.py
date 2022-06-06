class TemperatureData:    
    def __init__ (self,dataTable,date):
        self.dataTable = dataTable
        self.date = date
        date_obj = self.date
        minTemperature = []
        maxTemperature = []
        snowFall = []

    def minTemperature (self): 
        minTemperature = (self.dataTable[:,3])
        return (minTemperature)

    def maxTemperature (self):
        maxTemperature = (self.dataTable[:,2])
        return (maxTemperature)

    def snowFall (self):
        snowFall = (self.dataTable[:,4])
        return (snowFall)