import build.lib.cylowess as cyl
from pandas import *
import statsmodels.api as sm

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.style.use('ggplot')

mcycle = read_csv('mcycle.csv')
time = mcycle['times']
accel = mcycle['accel']
print (len(time.values), len(accel.values))

smlw = sm.nonparametric.lowess
sm_lowess = smlw(accel, time, frac = 0.1, it = 3)
new_lowess = cyl.lowess(accel.values, time.values, frac = 0.1, it = 3)
# Results from R: lowess(mcycle, delta = 0, f = 0.1, iter = 3)
r_lowess = read_csv("r_lowess_d0_it3_f0-01.csv")

plt.figure(figsize = (10, 7))
plt.plot(time, accel, '.', color = "steelblue", alpha = 0.25, label = 'Data')
plt.xlabel('Time after impact (ms)')
plt.ylabel('Acceleration (g)')
plt.plot(new_lowess[:,0], new_lowess[:,1], '-', color = 'orange', label = 'New lowess')
plt.plot(sm_lowess[:,0], sm_lowess[:, 1], '--r', label = 'Statsmodel lowess')
plt.plot(r_lowess['x'], r_lowess['y'], '+g', label = 'R lowess')
plt.legend(loc = 'upper left')
plt.savefig('motorcycle lowess comparisons.png')
