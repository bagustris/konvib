import vibration_toolbox as vtb
import numpy as np

import scipy.io as sio

# load and plot data 1 (frf_data1.mat)
data_path = '/media/bagustris/atmaja/github/vibration_toolbox/vibration_toolbox/data/frf_data1.mat'
data = sio.loadmat(data_path)

# bisa juga spt ini
data2 = sio.loadmat(vtb.__path__[0] + "/data/frf_data1.mat")

type(data)

data.keys()


x = data['x']
f = data['f']
dt = data['dt']
n = data['n']

x = x.reshape(len(x))
x = np.squeeze(x)
f = np.squeeze(f)
dt = float(dt)
freq, mag, ang, coh = vtb.frf(x, f, dt)

# csv ---> pd.readcsv, np.loadtxt

# load and plot data 2 (case1.mat)
data3 = sio.loadmat(vtb.__path__[0] + '/data/case1.mat')
TF = data3['Hf_chan_2']
f = data3['Freq_domain']

z, nf, a = vtb.sdof_cf(f, TF, 500, 1000)

# load and plot data 3 (case2.mat)
data4 = sio.loadmat(vtb.__path__[0] + '/data/case2.mat')
TF2 = data4['Hf_chan_2']
f2 = data4['Freq_domain']

z2, nf2, a2 = vtb.mdof_cf(f2, TF2, 500, 1000)

# is is possible to plot curve fitting of mdof above?
