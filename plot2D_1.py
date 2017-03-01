import numpy as np
import matplotlib.pyplot as plt

xi =  -2.0
xf =  2.0
yi =  0.0
yf =  20.0

#Imagen=np.array([[1,2,3,4,5],[4,5,6,7,8],[7,8,9,10,11]])
'''
Imagen=np.array([
				[1,2,3,4,5,1,2],
				[4,5,6,7,8,4,5],
				[7,8,9,10,11,7,12]
				])
'''
Imagen=np.array([
		[1, 20, 1], 
        [20, 1, 60], 
        [30, 60, 30],
        [6,7,8],
        [10,49,60]
        ])
        
print Imagen.shape

fig = plt.figure(1)
im = plt.imshow(np.flipud(Imagen), origin='lower', interpolation='nearest', cmap = 'jet', aspect = 'auto', extent = [xi,xf,yi,yf])
cbar = plt.colorbar(im, orientation = 'vertical')
plt.ylabel('Range (m)', fontsize = 14)
plt.xlabel('Cross-range (m)', fontsize = 14)
plt.show()
fig.clear()
