def search_note():
    keyword = input("Enter a word to search: ")
    found = False

    try:
        file = open("notes.txt", "r")
        notes = file.readlines()
        file.close()

        for index, note in enumerate(notes, start=1):
            if keyword.lower() in note.lower():
                print(f"Found in note {index}: {note.strip()}")
                found = True

        if not found:
            print("No matching note found.\n")

    except FileNotFoundError:
        print("Notes file not found.\n")

