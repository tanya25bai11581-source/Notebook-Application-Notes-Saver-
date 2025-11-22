from add_note import add_note
from view_notes import view_notes
from search_note import search_note
from edit_note import edit_note
from delete_note import delete_note

def main_menu():
    while True:
        print("======== NOTEBOOK APPLICATION ========")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Search Note")
        print("4. Edit Note")
        print("5. Delete Note")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            search_note()
        elif choice == "4":
            edit_note()
        elif choice == "5":
            delete_note()
        elif choice == "6":
            print("Thank you for using the Notebook Application!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Start the program
main_menu()
