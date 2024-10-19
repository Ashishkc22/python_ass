def menu():
    print("\nFile Handling Menu:")
    print("1. Open File")
    print("2. Write to File")
    print("3. Read from File")
    print("4. Write Line to File")
    print("5. Read Line from File")
    print("6. Close File")
    print("7. Rename File")
    print("8. Exit")

def file_handling():
    file = None
    while True:
        menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            filename = input("Enter the file name to open: ")
            file = open(filename, 'a+')
            print(f"Opened file: {filename}")
        
        elif choice == '2':
            if file:
                content = input("Enter content to write: ")
                file.write(content + '\n')
                print("Content written to file.")
            else:
                print("File not opened.")
        
        elif choice == '3':
            if file:
                file.seek(0)
                print("File Content:\n", file.read())
            else:
                print("File not opened.")
        
        elif choice == '4':
            if file:
                content = input("Enter line to write: ")
                file.write(content + '\n')
                print("Line written to file.")
            else:
                print("File not opened.")
        
        elif choice == '5':
            if file:
                file.seek(0)
                line = file.readline()
                print("Read line:", line.strip())
            else:
                print("File not opened.")
        
        elif choice == '6':
            if file:
                file.close()
                print("File closed.")
                file = None
            else:
                print("File not opened.")
        
        elif choice == '7':
            if file:
                old_name = input("Enter the old file name: ")
                new_name = input("Enter the new file name: ")
                file.close()
                import os
                os.rename(old_name, new_name)
                print(f"Renamed file from {old_name} to {new_name}.")
                file = open(new_name, 'a+')
            else:
                print("File not opened.")
        
        elif choice == '8':
            if file:
                file.close()
            print("Exiting.")
            break
        
        else:
            print("Invalid choice. Please try again.")

file_handling()
