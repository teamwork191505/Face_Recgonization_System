import cv2

# Create the haar cascade
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Read the video
video = cv2.VideoCapture("images/video.mp4")
while True:
    # Capture frame-by-frame
    ret, frame = video.read()

    # Detect faces in the frame
    faces = faceCascade.detectMultiScale(frame, scaleFactor = 1.1, minNeighbors = 5)

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Save the detected faces into images
    for (x, y, w, h) in faces:
        # Generate the file name
        filename = "face_" + str(y) + ".jpg"
        # Save the image file
        # cv2.imwrite(filename, frame[y:y+h, x:x+w])
        cv2.imwrite('images/image{0}.jpg', frame)

        print("[INFO] Saved {}".format(filename))

    # Break the loop
    if not ret:
        break

# When everything done, release the video capture object
video.release()