def add_note():
    note = input("Enter your note: ")

    file = open("notes.txt", "a")
    file.write(note + "\n")
    file.close()

    print("Note has been added successfully!\n")
