import vibration_toolbox as vtb
import numpy as np
import matplotlib.pyplot as plt

# define mass
# both are connected to wall
# ---)-----|m0|--)---|m1|---)--#
# ---vvv--|m0|--vvv--|m1|--vv--#

m0, m1 = 1, 1
c0, c1, c2 = 5, 5, 5
k0, k1, k2 = 1e3, 1e3, 1e3

# array mass
M = np.array([[m0, 0], 
              [0, m1]])

C = np.array([[c0+c1, -c2],
              [-c2, c2+c2]])

K = np.array([[k0+k1, -k2],
              [-k2, k2+k2]])

# input ke system
sys = vtb.VibeSystem(M, C, K) 

# output
# sys.evalues
# sys.evectors
# sys.wn
# sys.wd
# sys.damping_ratio
# sys.lti

# frequency response
omega, magdb, phase = sys.freq_response()

# plot response at m0
sys.plot_freq_response(0, 0)

# plot grid
sys.plot_freq_response_grid(outs=[0, 1], inps=[0, 1])

# plot time response
t = np.linspace(0, 25, 1000)
F1 = np.zeros((len(t), 2))

F1[:, 1] = 1000*np.sin(40*t) # force applied on m1
sys.plot_time_response(F1, t)