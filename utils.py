
import numpy as np
def calc(file):
    """
    Function used to calculate the average and error of the data in a file
    :param file: The name of the file to be read
    :return: The average and error of the data in the file
    """
    data = np.loadtxt(file,skiprows=1)
    n = len(data)
    avg = 0
    err = 0
    for i in range(n):
        avg += data[i][1]/n
    for i in range(n):
        err += (data[i][1]-avg)**2
    err = np.sqrt(err/(n*(n-1)))
    return avg,err