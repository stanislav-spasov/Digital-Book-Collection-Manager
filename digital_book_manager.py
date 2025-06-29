import random

title = []
authors = []
statuses = []


def add_book(add_title: str, add_author: str, title_list: list[str], author_list: list[str], status_list: list[str]):
    if f"Title: {add_title}" not in title_list:
        title_list.append(f"Title: {add_title}")
        author_list.append(f"Author: {add_author}")
        status_list.append("Status: Unread")
        print(f"\nThe book '{add_title}' from '{add_author}' has been added.")
        save_fail()
    else:
        print(f"\nThe book '{add_title}' exist in your book manager.")


def mark_as_read(title_read: str, title_list: list[str], status_list: list[str]):
    if f"Title: {title_read}" in title_list:
        title_index = title_list.index(f"Title: {title_read}")
        status_list[title_index] = "Status: Read"
        print(f"\nThe book '{title_read}' has been mark as read.")
        save_fail()
    else:
        print(f"\nThe book '{title_read}' is not exist in your book manager.")


def mark_as_unread(title_unread: str, title_list: list[str], status_list: list[str]):
    if f"Title: {title_unread}" in title_list:
        title_index = title_list.index(f"Title: {title_unread}")
        status_list[title_index] = "Status: Unread"
        print(f"\nThe book '{title_unread}' has been mark as unread.")
        save_fail()
    else:
        print(f"\nThe book '{title_unread}' is not exist in your book manager.")


def search_book(keyword: str, title_list: list[str], author_list: list[str], status_list: list[str]):
    book_find = False
    for current_title in title_list:
        if book_find:
            break
        for current_author in author_list:
            book_index = title_list.index(current_title)
            if f"title: {keyword.lower()}" in current_title.lower():
                print("Book is find.")
                print(f"Book info: {current_title} | {author_list[book_index]} | {status_list[book_index]}")
                book_find = True
                break
            elif f"author: {keyword.lower()}" in current_author.lower():
                print("Book is find.")
                print(f"Book info: {title_list[book_index]} | {current_author} | {status_list[book_index]}")
                book_find = True
                break
    if not book_find:
        print("No books found.")


def suggest_book(title_list: list[str], author_list: list[str], status_list: list[str]):
    book_suggest = []
    author_suggest = []
    for i in range(len(status_list)):
        if status_list[i] == "Status: Unread":
            book_suggest.append(title_list[i])
            author_suggest.append(author_list[i])

    random_book = random.choice(book_suggest)
    random_author = author_suggest[book_suggest.index(random_book)]
    if book_suggest:
        print(f"Suggested book for read: {random_book} | {random_author}")
    else:
        print("No unread books left.")


def delete_book(title_delete: str, title_list: list[str], author_list: list[str], status_list: list[str]):
    book_is_delete = False
    for current_title in title_list:
        if f"title: {title_delete.lower()}" == current_title.lower():
            delete_index = title_list.index(current_title)
            print(f"The Book: {current_title} from {author_list[delete_index]} was delete from book manager.")
            title_list.remove(title_list[delete_index])
            author_list.remove(author_list[delete_index])
            status_list.remove(status_list[delete_index])
            book_is_delete = True
            save_fail()
            break
    if not book_is_delete:
        print("Book not found.")


def open_file():
    f = open('storage.txt', 'r')
    print(f.read())
    f.close()


def save_fail():
    with open('storage.txt', 'w+') as f:
        store = False
        new_list = []
        for x in range(len(title)):
            if store:
                break
            for y in range(len(authors)):
                if store:
                    break
                for z in range(len(statuses)):
                    new_list.append(f"{title[x]} | {authors[y]} | {statuses[z]}")
                    x += 1
                    y += 1
                    if z == len(statuses) - 1:
                        store = True
                        break
        f.write("\n".join(new_list))
        print("File written successfully")
    f.close()


def process_command(current_choice: str, titles: list[str], author: list[str], status: list[str]):
    if current_choice == "1":
        new_title = input("Enter the book title: ")
        new_author = input("Enter the author's name: ")
        add_book(new_title, new_author, titles, author, status)

    elif current_choice == "2":
        read_title = input("Enter the title of the book to mark as read: ")
        mark_as_read(read_title, titles, status)
    elif current_choice == "3":
        unread_title = input("Enter the title of the book to mark as unread: ")
        mark_as_unread(unread_title, titles, status)
    elif current_choice == "4":
        search_keyword = input("Enter the keyword to search in book manager: ")
        search_book(search_keyword, titles, author, status)
    elif current_choice == "5":
        open_file()
    elif current_choice == "6":
        suggest_book(title, authors, status)
    elif current_choice == "7":
        delete_title = input("Enter the title of the book to delete: ")
        delete_book(delete_title, titles, author, status)
    elif current_choice == "8":
        exit()
    else:
        print("Invalid option. Please choose a number from 1 to 8.")


def load_file_data():
    with open("storage.txt", "r") as f:
        books = []
        for line in f:
            books.append(line.strip().split(" | "))
        for book_title in range(len(books)):
            title.append(books[book_title][0])
        for book_authors in range(len(books)):
            authors.append(books[book_authors][1])
        for book_status in range(len(books)):
            statuses.append(books[book_status][2])
        f.close()


def main():
    print("Welcome to the Digital Book Collection Manager \n")

    load_file_data()

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


main()
