import numpy as np
class Ensemble(object):
    
    def __init__(self,data,header):
        

        self.data = np.copy(data)
        self.n = len(data)
        
        self.header = header
    def average(self):
        vals = [self.data[i][1] for i in range(self.n)]
        return np.average(vals)
    def error(self):
        values = [self.data[i][1] for i in range(self.n)]
        std = np.std(values,ddof=1)
        return std/np.sqrt(self.n)
    @staticmethod
    def load(data):
        header = "h"
        data_ = [[0,data[i]] for i in range(len(data))]
        return Ensemble(data_,header)
    @staticmethod
    def read(path):
        data = np.loadtxt(path,skiprows=1)
        with open(path,"r") as f:
            header = f.readline()

        
        return Ensemble(data,header)
    def average_error(self):
        pass

    def write(self,path):
        with open(path,"w") as f:
            f.write(self.header )
            for i in range(len(self.data)):
                f.write(" "+str(int(self.data[i][0])) + " " +str(self.data[i][1] )+ "\n")
def scale_ensebmle(ensemble,factor):
    data_tmp = np.copy(ensemble.data)
    header = ensemble.header
    values = [data_tmp[i][1] for i in range(len(data_tmp))]
    index_t =  [data_tmp[i][0] for i in range(len(data_tmp))]
    avg = np.average(values)
    
    for i in range(len(data_tmp)):
        data_tmp[i][1] = avg + (data_tmp[i][1]-avg)*factor
    return Ensemble(data_tmp,header)
def apply_function_two_ensembles(ensemble_one,ensemble_two,g):
    n_1 = ensemble_one.n
    n_2 = ensemble_two.n
    if n_1 != n_2:
        raise ValueError("Ensembles not of same length")
    data_one = np.copy(ensemble_one.data)
    data_two = np.copy(ensemble_two.data)
    header = ensemble_one.header
    for i in range(len(data_one)):
        data_one[i][1] = g(data_one[i][1],data_two[i][1])
    return Ensemble(data_one,header)
def apply_function_ensemble(ensemble,g):
    data_ = np.copy(ensemble.data)
    for i in range(len(data_)):
        data_[i][1] = g(data_[i][1])
    return Ensemble(data_,ensemble.header)
def scale_ensemble_down(ensemble):

    f = -(ensemble.n-1)
    return scale_ensebmle(ensemble,1/f) 
def scale_ensemble_up(ensemble):
    f = -(ensemble.n-1)
    return scale_ensebmle(ensemble,f) 

def Z_ensemble(path_z_ensemble,path_m_ensemble,t0):
    ensemble_z = Ensemble.read(path_z_ensemble)
    ensemble_m = Ensemble.read(path_m_ensemble)
    scale_down_z = scale_ensemble_down(ensemble_z)
    scale_down_m = scale_ensemble_down(ensemble_m)
    def Z(z,m):
        return z*np.exp(m*t0/2)
    ensemble_down_Z = apply_function_two_ensembles(scale_down_z,scale_down_m,Z)
    ensemble_Z = scale_ensemble_up(ensemble_down_Z)
    return ensemble_Z



