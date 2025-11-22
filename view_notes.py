def view_notes():
    try:
        file = open("notes.txt", "r")
        notes = file.readlines()
        file.close()

        if len(notes) == 0:
            print("No notes found.\n")
        else:
            print("\nYour Notes:")
            for index, note in enumerate(notes, start=1):
                print(f"{index}. {note.strip()}")
            print()
    except FileNotFoundError:
        print("Notes file not found.\n")
