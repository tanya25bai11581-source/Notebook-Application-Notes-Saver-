from view_notes import view_notes

def edit_note():
    view_notes()

    try:
        number = int(input("Enter note number to edit: "))

        file = open("notes.txt", "r")
        notes = file.readlines()
        file.close()

        if number < 1 or number > len(notes):
            print("Invalid note number.\n")
            return

        new_text = input("Enter new text: ")
        notes[number - 1] = new_text + "\n"

        file = open("notes.txt", "w")
        file.writelines(notes)
        file.close()

        print("Note edited successfully!\n")

    except ValueError:
        print("Please enter a valid number.\n")
    except FileNotFoundError:
        print("Notes file not found.\n")
