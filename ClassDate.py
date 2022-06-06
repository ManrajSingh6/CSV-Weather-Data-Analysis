class Date:
    def __init__ (self, dataTable):
        self.dataTable = dataTable
        month = []
        year = []

    def month (self):
        month = (self.dataTable[:,1])
        return month

    def year (self):
        year = (self.dataTable[:,0])
        return year