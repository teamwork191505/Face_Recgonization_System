import cv2
import face_recognition
from certifi.__main__ import args

# read 1st image and store encodings
image = cv2.imread(args["Jeff_Bezoz.jpg"])  # args
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

boxes = face_recognition.face_locations(rgb, model=args["detection_method"])  # args
encodings1 = face_recognition.face_encodings(rgb, boxes)

# read 2nd image and store encodings
image = cv2.imread(args["images"])
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

boxes = face_recognition.face_locations(rgb, model=args["detection_method"])  # args
encodings2 = face_recognition.face_encodings(rgb, boxes)

# now you can compare two encodings
# optionally you can pass threshold, by default it is 0.6
matches = face_recognition.compare_faces(encodings1, encodings2)
