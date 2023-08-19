import cv2
img=cv2.imread('c:/Users/saree_0rj353/Desktop/Coding/C104/solar-system.jpg')
cv2.putText(img,'Sun',(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,'Mercury',(110,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,'Venus',(195,330),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,'Earth',(290,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,'Mars',(360,330),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.imshow('Solar system',img)
cv2.waitKey(0)