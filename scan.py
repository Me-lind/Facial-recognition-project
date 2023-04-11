import face_recognition
import cv2
import os

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
            print(f"No match found for this face.")
    
    print("Unknown user.")
    return "unknown"



if __name__ == '__main__':
    scan_user()
