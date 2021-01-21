import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

legend = ['Our Model', 'CIZSL']
iterations = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000]
my_model_data = [ 22.166981,  31.188389,  31.391753,  35.473497,  37.699880,  38.659022,  39.090936,  39.090936,  39.699230,  39.699230,  39.699230,  39.699230,  39.699230,  39.875634,  39.875634,  39.875634,  39.875634,  39.875634,  39.875634,  39.875634,  39.875634,  39.875634,  39.875634,  39.875634,  39.875634,  39.875634,  39.875634,  39.875634,  39.875634,  39.875634]
CIZSL_data = [ 7.200454,  26.253353,  29.697839,  33.405874,  35.496389,  35.893107,  36.364501,  36.364501,  36.623839,  37.330055,  37.657163,  37.657163,  37.657163,  37.657163,  38.192566,  38.192566,  38.192566,  38.192566,  38.192566,  38.192566,  38.192566,  38.192566,  38.192566,  38.192566,  38.192566,  38.192566,  38.192566,  38.192566,  38.192566,  38.192566]

plt.plot(iterations[:15], my_model_data[:15])
plt.plot(iterations[:15], CIZSL_data[:15])

plt.legend(legend)
plt.xlabel('Number of Iterations')
plt.ylabel('Seen-Unseen AUC (%)')
plt.savefig('./plot/convergence.png') 
