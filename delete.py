import os

def delete_user():
    # Prompt user for name of user to delete
    name = input("Enter Name of user to delete: ")
    
    # Check if user image exists
    image_dir = "./user_images"
    image_name = f"{name}.jpg"
    image_path = os.path.join(image_dir, image_name)
    if not os.path.exists(image_path):
        print("User not found.")
        return
    
    # Delete user image file
    os.remove(image_path)
    
    print("User deleted successfully.")

    if __name__ == '__main__':
   
        delete_user()