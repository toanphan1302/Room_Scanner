from convert import convert
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D

#read from text file
file = open("distance.txt", "r")
distance = file.read()
distance=distance.splitlines()
i = 0
while i < len(distance):
    distance[i]=float(distance[i])
    i = i+1

#generate_angle_matrix
angles = [[],[]]
phi = 23.7
while phi <= 155:
    phi = phi +1.3
    theta = -65
    while theta <= 65:
        angles[0].extend([theta])
        angles[1].extend([phi])
        theta = theta + 1.3

#convert spherical coor to car
coor = [distance,angles[0],angles[1]]
coorarray=np.asarray(coor)#just to debug
xyz = convert(coor)
xyzarray = np.asarray(xyz)#just to debug

#plot
fig=plt.figure()
ax=Axes3D(fig)
ax.scatter(xyz[0], xyz[1], xyz[2],c= np.linalg.norm([xyz[0], xyz[1], xyz[2]], axis=0 ))
plt.show()
