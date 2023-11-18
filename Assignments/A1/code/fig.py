import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon,Wedge

ax = plt.gca()


#circle
w = Wedge((0,0), 13, 0, 360, fc='white', edgecolor='black')
ax.add_artist(w)

#chord1
pointB = [12, 5]
pointA = [-12, 5]
x_values = [pointB[0], pointA[0]]
y_values = [pointB[1], pointA[1]]
plt.plot(x_values, y_values,color='black', linestyle="-")
plt.text(pointB[0]-0.015, pointB[1]+0.25, "PointB")
plt.text(pointA[0]-0.050, pointA[1]-0.25, "PointA")

#chord2
pointD = [5, -12]
pointC = [-5, -12]
x_values = [pointD[0], pointC[0]]
y_values = [pointD[1], pointC[1]]
plt.plot(x_values, y_values,color='black', linestyle="-")
plt.text(pointD[0]-0.015, pointD[1]+0.25, "PointD")
plt.text(pointC[0]-0.050, pointC[1]-0.25, "PointC")

#required line segment
pointN = [0, 5]
pointM = [0,-12]
x_values = [pointN[0], pointM[0]]
y_values = [pointN[1], pointM[1]]
plt.plot(x_values, y_values,color='black', linestyle="-")
plt.text(pointN[0]-0.015, pointN[1]+0.25, "PointN")
plt.text(pointM[0]-0.050, pointM[1]-0.25, "PointM")

#plotting center points
plt.plot(0, 0, marker="o", markersize=2.5, markeredgecolor="black", markerfacecolor="black")


ax.set_xlim(-15, 20)
ax.set_ylim(-15, 15)

plt.show()
