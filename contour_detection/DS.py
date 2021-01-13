import numpy as np
import cv2
img = np.zeros((200,200), dtype=np.uint8)
img[50:150, 50:150] = 255
img[0:25, 0:25] = 255
ret, threshold = cv2.threshold(img, 127,255, 0)
contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(contours)
color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
img = cv2.drawContours(color, contours, -1, (0,255,0), 2)
cv2.imshow("contours", img)
cv2.imwrite('/home/delameta/Desktop/coba/flask/contours1.jpg', img)
if cv2.waitKey(0) & 0xFF == ord('q'):
	cv2.destroyAllWindows()
