import numpy as np
import cv2

cap = cv2.VideoCapture(0)  

while True:
    ret, frame = cap.read()  
    frame[:, :, 0] = 200
    #Here 0,1,2 represent BGR respectively and 200 is the specified value

    cv2.imshow('Blue Filter',frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()  
cv2.destroyAllWindows()    