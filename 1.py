import cv2
from simple_facerec import SimpleFacerec

# Encode faces from a folder
RS = SimpleFacerec()
RS.load_encoding_images("images/")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = RS.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 200, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 5:
        break
    # else:
    #     try:
    #         var = input()
    #         # print('use keyboard interrupt')
    #     except KeyboardInterrupt:
    #         print('KeyboardInterrupt exception is caught')


cap.release()
cv2.destroyAllWindows()

# try:
#     var = input()
#     print('use keyboard interrupt')
# except KeyboardInterrupt:
#     print('KeyboardInterrupt exception is caught')
# else:
#     print('no exception found')
