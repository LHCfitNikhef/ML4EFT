import numpy as np
from matplotlib.patches import Ellipse
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
#ax = fig.add_subplot(211, aspect='auto')

e1 = Ellipse((-0.5, 0.1), 1.0, 0.5, angle=30, fill=True)
ax.add_patch(e1)
ax.axhline(0.25, 0, 1, color='black', linestyle='dashed')
ax.axhline(-0.25, 0, 1, color='black', linestyle='dashed')
ax.axvline(0.5, 0, 1, color='black', linestyle='dashed')
ax.axvline(-0.5, 0, 1, color='black', linestyle='dashed')
ax.set_aspect('equal')
ax.set_xlim((-1, 1))
ax.set_ylim((-1, 1))
plt.show()