import numpy as np
import matplotlib.pyplot as pyplot

class FileIO:
    def dataTable(file_path):
        dataTable = np.loadtxt(file_path, delimiter=',', skiprows=1, usecols=(0,1,2,3,4), dtype=np.float)
        return dataTable