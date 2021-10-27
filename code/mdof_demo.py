## library
# libray --> package (opsional) --> module (1 file) ---> methods (function, beberapa fn dlm 1 file)


## jupyterlab
# python3.7 -m pip install jupyterlab
# jupyterlab

import numpy as np
import vibration_toolbox as vtb

vtb.sdof()
vtb.mdof_cf()
vtb.analytical()
L = np.array([[2, -1, 0],
              [-4, 8, -4],
              [0, -4, 4]])

# eigen value and vectors, sorted
lam, P = vtb.mdof._eigen(L)

# compare to np.linalg.eig --> unsorted
# M = np.arange(0, 9).reshape(3, 3)

# _normalize --> to normalize (??)

## mode system --> damped
M = np.array([[1, 0],
              [0, 1]])

K = np.array([[2, -1],
              [-1, 6]])

C = np.array([[0.3, -0.02],
              [-0.02, 0.1]])

# mode system
wn, wd, zeta, x, y = vtb.modes_system(M, K, C)


# undamped
M = np.array([[4, 0, 0],
              [0, 4, 0],
              [0, 0, 4]])
K = np.array([[8, -4, 0],
              [-4, 8, -4],
              [0, -4, 4]])

w, p, s, Sinv = vtb.modes_system_undamped(M, K)


# analisa apa perbedaan kondisi mode damped vs. undamped (Misal: apakah karena tidak komponen C)


# respon sistem -- damped
# input: M, K, C, x0, v0, t, F

M = np.array([[9, 0],
              [0, 1]])
K = np.array([[27, -3],
              [-3, 3]])
C = K/10
x0 = np.array([0, 1])
v0 = np.array([1, 0])
t = np.linspace(0, 10, 100)
F = np.vstack([0*t, 3*np.cos(2*t)])

T, yout, xout = vtb.mdof.response_system(M, C, K, F, x0, v0, t)

plt.plot(T, yout)


# respon sistem --> undamped
M = np.array([[1, 0],
              [0, 4]])
K = np.array([[12, -2],
              [-2, 12]])
x0 = np.array([1, 1])
v0 = np.array([0, 0])
max_time = 10
t, X = vtb.mdof.response_system_undamped(M, K, x0, v0, max_time)
# first column is the initial conditions [x1, x2, v1, v2]
# X[:, 0] # doctest: +SKIP
# array([1., 1., 0., 0.])
# X[:, 1] # displacement and velocities after delta t
# array([ 1.  ,  1.  , -0.04, -0.01])

# Coba analisa apa perbedaan respon hasil undamped vs. damped