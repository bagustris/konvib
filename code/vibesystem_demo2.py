# from https://nbviewer.org/github/vibrationtoolbox/vibration_toolbox/blob/binder/vibesystem_notebook.ipynb

import numpy as np
import vibration_toolbox as vtb

m0, m1, m2 = (1, 1, 1)
k0, k1, k2 = (1600, 1600, 1600)
alpha, beta = 1e-3, 1e-3

# C=αM+βK
M = np.array([[m0, 0, 0],
              [0, m1, 0],
              [0, 0, m2]])
K = np.array([[k0+k1, -k1,   0],
              [-k1, k1+k2, -k2],
              [0,     -k2,  k2]])
C = alpha*M + beta*K

# input to vtb vibesystem
sys = vtb.VibeSystem(M, C, K, name='3 dof system')

sys.wn
sys.wd

ax = sys.plot_freq_response(0, 0)

## change value of C
sys.C = 20*C
sys.wd
sys.wn

sys.C = C
axs = sys.plot_freq_response_grid([0, 1], [0, 1])

ax = sys.plot_freq_response(0, 0, modes=[0, 1], 
                            color='r', linestyle='--',
                            label='Modes 0 and 1')
ax = sys.plot_freq_response(0, 0, ax0=ax[0], ax1=ax[1], 
                            color='b', label='All modes')
ax[1].legend()

t = np.linspace(0, 25, 1000)
# force array with len(t) rows and len(inputs) columns
F1 = np.zeros((len(t), 3))
# in this case we apply the force only to the mass m1
F1[:, 1] = 1000*np.sin(40*t) 

# plot time response at m0
t, yout, xout = sys.time_response(F1, t)
ax = vtb.plot_fft(t, time_response=yout[:, 0])  # change to m1, m2