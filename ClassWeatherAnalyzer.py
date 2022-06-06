class WeatherAnalyzer:
    def __init__ (self,weatherdata,date_obj):
        self.weatherdata = weatherdata
        self.date_obj = date_obj

    def getMinTemp(self):
        minTemperature = np.min(self.weatherdata.minTemperature())
        print("The minimum temperature between the years 1990 and 2019 was:", minTemperature,"degrees.")
        
    def getMaxTemp(self):
        maxTemperature = np.max(self.weatherdata.maxTemperature())
        print("The maximum temperature between the years 1990 and 2019 was:", maxTemperature,"degrees.")

    def getMaxTempAnnually(self):
        maxTemperature = self.weatherdata.maxTemperature()
        #date_month = self.date_obj.month()
        date_year = self.date_obj.year()
        i = 0
        MaxTemp = [[],[]]
        temperature = []
        while i < 359:
            for x in range (0,12):
                temperature.append(maxTemperature [i])
                if i <= 357:
                    i += 1
                else:
                    Max = np.max(temperature)
                    Year = int(date_year[i])
                    MaxTemp[0].append(Year)
                    MaxTemp[1].append(Max)
                    print ("The maximum temperature in year", Year, end = " ")
                    print ("was:", Max,"degrees.")
                    i = 360
                    break
                if x==11:
                    Max = np.max(temperature)
                    Year = int(date_year[i])-1
                    MaxTemp[0].append(Year)
                    MaxTemp[1].append(Max)
                    print ("The maximum temperature in year", Year, end = " ")
                    print ("was:", Max,"degrees.")
                    list.clear(temperature)
        #print (MaxTemp[0],MaxTemp[1]) Shows the 2D array with information regarding Year, and appropriate Temperature.
        return MaxTemp

    def getMinTempAnnually(self):
        minTemperature = self.weatherdata.minTemperature()
        #date_month = self.date_obj.month()
        date_year = self.date_obj.year()
        i = 0
        MinTemp = [[],[]]
        temperature = []
        while i < 359:
            for x in range (0,12):
                temperature.append(minTemperature[i])
                if i <= 357:
                    i += 1
                else:
                    Min = np.min(temperature)
                    Year = int(date_year[i])
                    MinTemp[0].append(Year)
                    MinTemp[1].append(Min)
                    print ("The minimum temperature in year", Year,end = " ")
                    print ("was:", Min,"degrees.")
                    i = 360
                    break
                if x==11:
                    Min = np.min(temperature)
                    Year = int(date_year[i])-1
                    MinTemp[0].append(Year)
                    MinTemp[1].append(Min)
                    print ("The minimum temperature in year", Year,end = " ")
                    print ("was:", Min,"degrees.")
                    list.clear(temperature)
        #print (MinTemp[0],MinTemp[1]) Shows the 2D array with information regarding Year, and appropriate Temperature.
        return MinTemp

    def AvgSnowFallAnnually(self):
        snowFall = self.weatherdata.snowFall()
        #date_month = self.date_obj.month()
        date_year = self.date_obj.year()
        AvgSnow = [[],[]]
        SnowFallAnnual = []
        
        i = 0
        while i < 359:
            for x in range (0,12):
                SnowFallAnnual.append(snowFall[i])
                if i <= 357:
                    i += 1
                else:
                    Avg = np.average(SnowFallAnnual)
                    Year = int(date_year[i])
                    AvgSnow[0].append(Year)
                    AvgSnow[1].append(Avg)
                    print ("The average snowfall in year", Year,end = " ")
                    print ("was:", Avg,"cms.")
                    i = 360
                    break
                if x==11:
                    Avg = np.average(SnowFallAnnual)
                    Year = int(date_year[i])-1
                    AvgSnow[0].append(Year)
                    AvgSnow[1].append(Avg)
                    print ("The average snowfall in year", Year,end = " ")
                    print ("was:", Avg,"cms.")
                    list.clear(SnowFallAnnual)
        #print(AvgSnow[0], AvgSnow[1]) #Shows the 2D array with information regarding Year, and appropriate SnowFall.
        return AvgSnow

    def AvgTemperatureAnnually(self):
        maxTemperature = self.weatherdata.maxTemperature()
        minTemperature = self.weatherdata.minTemperature()
        #date_month = self.date_obj.month()
        date_year = self.date_obj.year()
        AvgTemp = [[],[]]
        TemperatureAnnual = []

        i = 0
        while i < 359:
            for x in range (0,12):
                TemperatureAnnual.append(maxTemperature[i])
                TemperatureAnnual.append(minTemperature[i])
                if i <= 357:
                    i += 1
                else:
                    Avg = np.average(TemperatureAnnual)
                    Year = int(date_year[i])
                    AvgTemp[0].append(Year)
                    AvgTemp[1].append(Avg)
                    print ("The average temperature in year", Year,end = " ")
                    print ("was:", Avg,"degrees.")
                    i = 360
                    break
                if x==11:
                    Avg = np.average(TemperatureAnnual)
                    Year = int(date_year[i])-1
                    AvgTemp[0].append(Year)
                    AvgTemp[1].append(Avg)
                    print ("The average temperature in year", Year,end = " ")
                    print ("was:", Avg,"degrees.")
                    list.clear(TemperatureAnnual)
        #print(AvgTemp[0], AvgTemp[1]) #Shows the 2D array with information regarding Year, and appropriate Avg Temperature.
        return AvgTemp