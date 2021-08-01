import cv2
import numpy

img = cv2.imread('.\\test.jpg')
img2 = cv2.imread('.\\test2.jpg')
difference = cv2.subtract(img,img2)
result =not numpy.any(difference)
if result is True:
    print('Y')
    print(difference)
else:
    cv2.imwrite('result.jpg',difference)
    print(difference)
    print('N')