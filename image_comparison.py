import cv2
import face_recognition
import numpy as np
from numpy import ndarray

img = cv2.imread("Images/RDJ new.jpg")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding: ndarray = face_recognition.face_encodings(rgb_img)[0]

img2 = cv2.imread("images/Rdj.jpg")
rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img_encoding2: ndarray = face_recognition.face_encodings(rgb_img2)[0]

result = face_recognition.compare_faces([img_encoding], img_encoding2)
print("Result: ", result)
if result == [True]:
    from plyer import notification
    import time

    while True:
        time.sleep(2)
        notification.notify(
            title='Alert From Police HQ',
            message='Suspected person found in your area'
                    '\nshowed image of suspected person',
            app_icon="Notif.ico",
            timeout=8,
        )
        cv2.imshow("Img", img)
        cv2.imshow("Img 2", img2)

else:
    cv2.imshow("Img", img)
    cv2.imshow("Img 2", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
