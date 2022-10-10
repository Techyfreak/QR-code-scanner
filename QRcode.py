import cv2
import numpy as np
from pyzbar.pyzbar import decode

#img =cv2.imread('')
#info= decode(img)
#print(info)

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    success,img = cap.read()
    for qrcode in decode(img):
        print(qrcode.data)
        Mydata = qrcode.data.decode('utf-8')
        print(Mydata)
        pts=np.array([qrcode.polygon],np.int32)
        pts=pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(255,0,255),5)
        pts2=qrcode.rect
        cv2.putText(img, Mydata, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX,
                    0.9, (255, 0, 255), 2)

    cv2.imshow('result',img)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break



