from view_notes import view_notes

def delete_note():
    view_notes()

    try:
        number = int(input("Enter note number to delete: "))

        file = open("notes.txt", "r")
        notes = file.readlines()
        file.close()

        if number < 1 or number > len(notes):
            print("Invalid note number.\n")
            return

        notes.pop(number - 1)

        file = open("notes.txt", "w")
        file.writelines(notes)
        file.close()

        print("Note deleted successfully!\n")

    except ValueError:
        print("Please enter a valid number.\n")
    except FileNotFoundError:
        print("Notes file not found.\n")
