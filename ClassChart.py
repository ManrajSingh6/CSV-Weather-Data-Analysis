class Chart:
    def drawBarChart(x,y,title,xlabel,ylabel):
        fig = pyplot.figure()
        pyplot.title(title)
        pyplot.ylabel(ylabel)
        pyplot.xlabel(xlabel)
        pyplot.bar(x,y)
        pyplot.show()

    def drawLineChart(x,y,title,xlabel,ylabel):
        fig = pyplot.figure()
        pyplot.title(title)
        pyplot.ylabel(ylabel)
        pyplot.xlabel(xlabel)
        pyplot.plot (x, y, marker='o')
        pyplot.show()
