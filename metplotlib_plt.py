import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([0,1,2,4,8,16,32,64,128])
ax.set_xlabel('Label')
ax.set_ylabel('Value')
plt.show()
