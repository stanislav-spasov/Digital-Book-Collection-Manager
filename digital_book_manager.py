from store import title, authors, statuses


def add_book(add_title: str, add_author: str, title_list: list[str], author_list: list[str], status_list: list[str]):
    if add_title not in title_list:
        title_list.append(add_title)
        author_list.append(add_author)
        status_list.append("Unread")
        print(f"\nThe book '{add_title}' from '{add_author}' has been added.")
    else:
        print(f"\nThe book '{add_title}' exist in your book manager.")


def mark_as_read(title_read: str, title_list: list[str], status_list: list[str]):
    if title_read in title_list:
        title_index = title_list.index(title_read)
        status_list[title_index] = "Read"
        print(f"\nThe book '{title_read}' has been mark as read.")
    else:
        print(f"\nThe book '{title_read}' is not exist in your book manager.")


def process_command(current_choice: str, titles: list[str], author: list[str], status: list[str]):
    if current_choice == "1":
        new_title = input("Enter the book title: ")
        new_author = input("Enter the author's name: ")
        add_book(new_title, new_author, titles, author, status)

    elif current_choice == "2":
        read_title = input("Enter the title of the book to mark as read: ")
        mark_as_read(read_title, titles, status)
    elif current_choice == "3":
        ...
    elif current_choice == "4":
        ...
    elif current_choice == "5":
        ...
    elif current_choice == "6":
        ...
    elif current_choice == "7":
        ...
    elif current_choice == "8":
        ...
    else:
        print("Invalid option. Please choose a number from 1 to 8.")


def main():
    print("Welcome to the Digital Book Collection Manager \n")

    while True:
        print("\nPlease choose an option:")
        print("1. Add a new book")
        print("2. Mark a book as read")
        print("3. Mark a book as unread")
        print("4. Search for a book")
        print("5. List all books")
        print("6. Suggest a book to read")
        print("7. Delete a book")
        print("8. Exit")

        choice = input("\nEnter your choice (1-8): ")

        process_command(choice, title, authors, statuses)
        print(title)


main()
