import matplotlib.pyplot as plt

fig, ax=plt.subplots(1,2,figsize=(7, 2.5))
ax[0].scatter([1,2], [1,2])
ax[0].scatter([1.2,2.5], [1.2,2.5])
plt.show()