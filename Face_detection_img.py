import cv2

# Load the cascade classifier
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Read the input image
img = cv2.imread("smiles.jpg")

# Convert into grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)

# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

# Display the output
cv2.imshow("Faces", img)

# Wait for the 'q' key press
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
