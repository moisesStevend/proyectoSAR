import numpy as np
import cv2

img=cv2.imread('trauco.jpg',0)
cv2.imwrite('trauco.png',img)
cv2.imshow('grande trauco', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
