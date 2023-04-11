'''
import face_recognition
import cv2
import os

def enroll_user():
    # Prompt user for name and ID
    name = input("Enter name: ")
    
    # Take image from file
    image_path = input("Enter image path: ")
    if not os.path.exists(image_path):
        print("Invalid path. Please enter a valid image path.")
        return
    image = face_recognition.load_image_file(image_path)
    
    # Save image with user's name as file name
    image_name = f"{name}.jpg"
    image_dir = "./user_images"
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
    image_path = os.path.join(image_dir, image_name)
    cv2.imwrite(image_path, image)

    print("User enrolled successfully.")

if __name__ == '__main__':
    enroll_user()
    '''
import face_recognition
import cv2
import os


def enroll_user():
    # Prompt user for name and ID
    name = input("Enter name: ")

    # Take image from file
    image_path = input("Enter image path: ")
    if not os.path.exists(image_path):
        print("Invalid path. Please enter a valid image path.")
        return

    # Load image and find faces
    image = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(image)
    if len(face_locations) != 1:
        print("Error: Please provide an image with exactly one face.")
        return

    # Compute face encoding and check for duplicates
    new_face_encoding = face_recognition.face_encodings(image)[0]
    for filename in os.listdir('./user_images'):
        if filename.endswith('.jpg'):
            image_path = os.path.join('./user_images', filename)
            existing_image = face_recognition.load_image_file(image_path)
            existing_face_encoding = face_recognition.face_encodings(existing_image)[0]
            if face_recognition.compare_faces([existing_face_encoding], new_face_encoding)[0]:
                print("Error: This face has already been enrolled under the name", os.path.splitext(filename)[0])
                return

    # Save image with user's name as file name
    image_name = f"{name}.jpg"
    image_dir = "./user_images"
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
    image_path = os.path.join(image_dir, image_name)
    cv2.imwrite(image_path, image)

    print("User enrolled successfully.")

if __name__ == '__main__':
    enroll_user()
