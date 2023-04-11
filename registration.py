import face_recognition
import cv2
import os

def enroll_user():
    # Prompt user for name and ID
    name = input("Enter name: ")
    id = input("Enter ID: ")
    
    # Take image from file
    image_path = input("Enter image path: ")
    image = face_recognition.load_image_file(image_path)
    
    # Save image with user's name as file name
    image_name = f"{name}.jpg"
    image_dir = "./user_images"
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
    image_path = os.path.join(image_dir, image_name)
    cv2.imwrite(image_path, image)

    print("User enrolled successfully.")

def scan_user():
    # Load images of enrolled users
    image_dir = "./user_images"
    image_files = os.listdir(image_dir)
    known_encodings = []
    known_names = []
    for image_file in image_files:
        image_path = os.path.join(image_dir, image_file)
        face_encoding = face_recognition.face_encodings(face_recognition.load_image_file(image_path))[0]
        print(f"Shape of {image_file}: {face_encoding.shape}")
        known_encodings.append(face_encoding)
        known_names.append(os.path.splitext(image_file)[0])

    # Capture image from webcam
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if not ret:
        print("Error capturing image.")
        return "unknown"
    
    # Find faces in captured image
    face_locations = face_recognition.face_locations(frame)
    if not face_locations:
        print("No face detected.")
        return "unknown"
    
    # Encode faces in captured image
    face_encodings = face_recognition.face_encodings(frame, face_locations)
    
    # Compare captured face to enrolled faces
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        if any(matches):
            index = matches.index(True)
            name = known_names[index]
            print(f"Welcome, {name}!")
            return name
        else:
            print(f"Shape of face encoding: {face_encoding.shape}")
    
    print("Unknown user.")

if __name__ == '__main__':
    while True:
        choice = input("Enter 'e' to enroll a new user or 's' to scan for a user: ")
        if choice == 'e':
            enroll_user()
        elif choice == 's':
            scan_user()
        else:
            print("Invalid choice. Try again.")
