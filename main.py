import enroll
import scan
import update
import delete


def main():
    while True:
        print("Please choose an option:")
        print("1. Enroll user")
        print("2. Scan face")
        print("3. Update user info")
        print("4. Delete user info")
        print("5. Exit")

        option = input("Option: ")
        if option == "1":
            enroll.enroll_user()       
        elif option == "2":
            scan.scan_user()
        elif option == "3":
            update.update_user()
        elif option == "4":
            delete.delete_user()
        elif option == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()
