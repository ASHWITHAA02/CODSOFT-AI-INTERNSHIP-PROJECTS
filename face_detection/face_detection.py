import cv2

print("Starting Face Detection System...")

# Load the Haar Cascade model
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Start webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

print("Webcam started. Press 'Q' to exit.")

while True:

    # Capture frame
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30,30)
    )

    # Draw rectangles around faces
    for (x,y,w,h) in faces:
        cv2.rectangle(
            frame,
            (x,y),
            (x+w,y+h),
            (0,255,0),
            2
        )

    # Display number of faces
    text = f"Faces detected: {len(faces)}"

    cv2.putText(
        frame,
        text,
        (10,30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )

    # Show webcam window
    cv2.imshow("Real-Time Face Detection", frame)

    # Exit if Q pressed
    key = cv2.waitKey(1)

    if key == ord('q') or key == ord('Q'):
        print("Exit key pressed")
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

print("Program closed.")