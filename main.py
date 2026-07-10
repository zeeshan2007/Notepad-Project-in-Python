import os

while True:
    print("\n========== NOTEPAD APP ==========")
    print("1. Create New Note")
    print("2. View Notes")
    print("3. Add More Text")
    print("4. Search Word")
    print("5. Clear All Notes")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        file_name = input("Enter file name: ") + ".txt"
        note = input("Enter your note: ")

        with open(file_name, "w") as f:
            f.write(note)

        print("File created successfully!")

    elif choice == "2":
        file_name = input("Enter file name: ") + ".txt"

        if os.path.exists(file_name):
            with open(file_name, "r") as f:
                print("\n----- Notes -----")
                print(f.read())
        else:
            print("File not found!")

    elif choice == "3":
        file_name = input("Enter file name: ") + ".txt"

        if os.path.exists(file_name):
            text = input("Enter text: ")

            with open(file_name, "a") as f:
                f.write("\n" + text)

            print("Text added successfully!")
        else:
            print("File not found!")

    elif choice == "4":
        file_name = input("Enter file name: ") + ".txt"

        if os.path.exists(file_name):
            word = input("Enter word to search: ")

            with open(file_name, "r") as f:
                data = f.read()

            if word in data:
                print("✅ Word Found")
            else:
                print("❌ Word Not Found")
        else:
            print("File not found!")

    elif choice == "5":
        file_name = input("Enter file name: ") + ".txt"

        if os.path.exists(file_name):
            with open(file_name, "w") as f:
                f.write("")

            print("All notes cleared successfully!")
        else:
            print("File not found!")

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid choice. Please try again.")