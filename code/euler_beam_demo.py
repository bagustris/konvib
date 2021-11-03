# demo module continues_system.py

import matplotlib.pyplot as plt
import vibration_toolbox as vtb

# using default inputs
omega_n, x, U = vtb.euler_beam_modes()

plt.plot(x, U)

# for n=1
omega_n, x, U = vtb.euler_beam_modes(n=1)

# frequency response
fout, H = vtb.euler_beam_frf()

# universal bar modes
omega_n, x, U = vtb.uniform_bar_modes()

# torsional bar modes
omega_n, x, U = vtb.torsional_bar_modes()
