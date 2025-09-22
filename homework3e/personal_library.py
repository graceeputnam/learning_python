
def get_books():
    print("Enter the title, author, and pages of each book.")
    print("End with a blank title.")
    responses = []
    while True:
        title = input("Title: ")
        if title == "":
            break
        author = input("Author: ")
        pages = input("Pages: ")
        book = (title, author, pages)
        responses.append(book)
    return responses


def get_author():
    print("Enter an author to report on.")
    author = input("Author: ")
    return author


def num_books_pages(author_main, books):
    book_count = 0
    page_count = 0
    for i in books:
        title, author, pages = i
        if author == author_main:
            book_count = book_count + 1
            page_count = page_count + int(pages)
    print(f"You have read {book_count} books by {author_main}.")
    print(f"You have read {page_count} pages by {author_main}.")


def main():
    books = get_books()
    author = get_author()
    num_books_pages(author, books)


if __name__ == '__main__':
    main()


