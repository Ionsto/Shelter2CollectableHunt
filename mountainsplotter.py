import matplotlib.pyplot as plt
from scipy.misc import imread
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
level = open("leaves.txt")
lines = level.readlines()
translines = [line for line in lines if "Translation" in line]
xyz = [line[:-1].split(",")[-3:] for line in translines]
x = np.array([-float(x[0]) for x in xyz])
y = np.array([float(x[1]) for x in xyz])
z = np.array([float(x[2]) for x in xyz])
x1 = -105.9313
z1 = -154.1481
print(len(x))
xscale = -376/-571.3787
zscale = -440/-655.3562
xoffset = 27
zoffset = -4
zoffset = -4
plt.scatter((x-x1)*xscale+xoffset,(z-z1)*zscale+zoffset)
plt.xlim(-750,750)
plt.ylim(-750,750)
mountainsmap = imread("mountains.png",mode="RGB")
plt.imshow(mountainsmap,extent=(-1920/2,1920/2,-1080/2,1080/2))
plt.scatter((x-x1)*xscale+xoffset,(z-z1)*zscale+zoffset)
xnew,ynew,znew = 6664850e-4,403809e-4,974380e-4
plt.scatter((-xnew-x1)*xscale+xoffset,(znew-z1)*zscale+zoffset,color="r")
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x,z,y, picker=50)
ax.scatter(xnew,znew,ynew,color="r")


plt.show()

# 59->56 (-379,-451)

# -571.3787,-655.3562