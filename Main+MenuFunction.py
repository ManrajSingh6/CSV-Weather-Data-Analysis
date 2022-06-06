def menu ():
    print ('1- Get Minimum Temperature of 1990-2019')
    print ('2- Get Maximum Temperature of 1990-2019')
    print ('3- Get Minimum Temperature of 1990-2019 Annually')
    print ('4- Get Maximum Temperature of 1990-2019 Annually')
    print ('5- Get Average Snowfall between 1990-2019 Annually')
    print ('6- Get Average Temperature between 1990-2019 Annually')
    print ('7- LineChart Minimum Temperature of 1990-2019 Annually')
    print ('8- LineChart Maximum Temperature of 1990-2019 Annually')
    print ('9- Barchart Average Snowfall between 1990-2019 Annually')
    print ('10- Barchart Average Temperature between 1990-2019 Annually')
    print (" ")
    ans = int(input("Type in the one of the associated numbers in the menu:"))
    return ans

def main():
    print ("Hello user! Please pick one of the following functionalities!")
    ans = menu ()
    file_path = "CalgaryWeather.csv"
    data = FileIO.dataTable(file_path)
    Date_Case = Date(data)
    Weatherdata = TemperatureData(data,Date_Case)
    Weather_Case = WeatherAnalyzer(Weatherdata,Date_Case)

    while (ans <= 0) or (ans > 10):
        print (" ")
        print ("The value you have entered does not match our menu bar!")
        print ("Please try again!")
        print (" ")
        ans = menu ()

    else:
        while ans > 0 and ans <= 10:
            if ans == 1:
                print (" ")
                Weather_Case.getMinTemp()
                break
            elif ans ==2:
                print (" ")
                Weather_Case.getMaxTemp()
                break
            elif ans == 3:
                print (" ")
                Weather_Case.getMinTempAnnually()
                break
            elif ans == 4:
                print (" ")
                Weather_Case.getMaxTempAnnually()
                break
            elif ans == 5:
                print (" ")
                Weather_Case.AvgSnowFallAnnually()
                break
            elif ans == 6:
                print (" ")
                x = Weather_Case.AvgTemperatureAnnually()
                break
            elif ans == 7:
                print (" ")
                mintemparray = Weather_Case.getMinTempAnnually()
                x = mintemparray[0]
                y = mintemparray[1]
                xlabel = "Year 1990 - 2019"
                ylabel = "Min Temperature (C)"
                title = "Minimum Temperatures of 1990 - 2019 Annually"
                Chart.drawLineChart(x,y,title,xlabel,ylabel)
                break
            elif ans == 8:
                print (" ")
                maxtemparray = Weather_Case.getMaxTempAnnually()
                x = maxtemparray[0]
                y = maxtemparray[1]
                xlabel = "Year 1990 - 2019"
                ylabel = "Max Temperature (C)"
                title = "Maximum Temperatures of 1990 - 2019 Annually"
                Chart.drawLineChart(x,y,title,xlabel,ylabel)
                break
            elif ans == 9:
                print (" ")
                avgsnowarray = Weather_Case.AvgSnowFallAnnually()
                x = avgsnowarray[0]
                y = avgsnowarray[1]
                xlabel = "Year 1990 - 2019"
                ylabel = "Average Snowfall (cms)"
                title = "Average Snowfall in 1990 - 2019 Annually"
                Chart.drawBarChart(x,y,title,xlabel,ylabel)
                break
            else:
                if ans == 10:
                    print (" ")
                    avgtemparray = Weather_Case.AvgTemperatureAnnually()
                    x = avgtemparray[0]
                    y = avgtemparray[1]
                    xlabel = "Year 1990 - 2019"
                    ylabel = "Average Temperature (C)"
                    title = "Average Temperature in 1990 - 2019 Annually"
                    Chart.drawBarChart(x,y,title,xlabel,ylabel)
                    break
                
    print (" ")
    print ("Would you like to run this program again?")
    print ("Type in 1 for Yes, and 2 for No.")
    choice = int(input("Decision:"))
    if choice == 1:
        main ()
    else:
        print (" ")
        print ("Goodbye!")

if __name__ == "__main__":
    main()