import numpy as np
import matplotlib.pyplot as plt

tc_data = []
for i in range (1, 100):
    tc = np.load('tc_{}.npy'.format(i))
    tc_data.append(tc)
tc_data = np.array(tc_data)

fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(tc_data, bins= 30)
plt.show()