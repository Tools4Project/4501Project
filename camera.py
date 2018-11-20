import numpy as np
import cv2

cap = cv2.VideoCapture(0)
count = 1
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret == True:
        # Our operations on the frame come here

        # Display the resulting frame
        cv2.imshow('frame',frame)
        k = cv2.waitKey(33)
        if k == ord('q'):
            break
        elif k == ord('c'):
            cv2.imwrite('./pic'+str(count)+'.jpg', frame) 
            count += 1


# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()



