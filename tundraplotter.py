import matplotlib.pyplot as plt
from scipy.misc import imread
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
level = open("tundra feather and gems.fbx")
lines = level.readlines()
translines = [line for line in lines if "Translation" in line]
xyz = [line[:-1].split(",")[-3:] for line in translines]
x = np.array([-float(x[0]) for x in xyz])
y = np.array([float(x[1]) for x in xyz])
z = np.array([float(x[2]) for x in xyz])
x1 = x[1]
z1 = z[1]
print(len(x))
scale = -297.2/-567.3
xoffset = -22.8
zoffset = 85.5
plt.scatter((x-x1)*scale+xoffset,(z-z1)*scale+zoffset)
plt.figure()
mountainsmap = imread("tundra.png",mode="RGB")
plt.imshow(mountainsmap,extent=(-1920/2,1920/2,-1080/2,1080/2))
plt.scatter((x-x1)*scale+xoffset,(z-z1)*scale+zoffset)
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x,z,y)
plt.show()

# 59->56 (-379,-451)

# -571.3787,-655.3562