import scipy.io as sio
#import numpy as np

#load data from DS1 file (training data)
data = sio.loadmat ('../data/p300_DS1.mat')
X = data['X']
Y = data['Y']
