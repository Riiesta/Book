class Book:
    counter = 0

    def __init__(self, title, author):
        Book.counter += 1
        self.id = Book.counter
        self.title = title
        self.author = author
        self.status = "доступна"

    def __str__(self):
        return f"ID: {self.id}, Название: {self.title}, Автор: {self.author}, Статус: {self.status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print("Книга успешно добавлена!")

    def get_book(self, book_id):
        for book in self.books:
            if book.id == book_id and book.status == "доступна":
                book.status = "взята"
                print("Книга успешно взята!")
                return
        print("Книга недоступна или не найдена.")

    def return_book(self, book_id):
        for book in self.books:
            if book.id == book_id and book.status == "взята":
                book.status = "доступна"
                print("Книга успешно возвращена!")
                return
        print("Книга не найдена.")

    def display_books(self):
        for book in self.books:
            print(book)

    def search_book(self, query):
        for book in self.books:
            if query.lower() in book.title.lower() or query.lower() in book.author.lower():
                print(book)


def main():
    library = Library()

    while True:
        print("""
1. Добавить книгу
2. Взять книгу
3. Вернуть книгу
4. Просмотреть все книги
5. Поиск книги
6. Выход
""")
        choice = int(input("Выберите действие: "))

        if choice == 1:
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            library.add_book(title, author)
        elif choice == 2:
            book_id = int(input("Введите ID книги: "))
            library.get_book(book_id)
        elif choice == 3:
            book_id = int(input("Введите ID книги: "))
            library.return_book(book_id)
        elif choice == 4:
            library.display_books()
        elif choice == 5:
            query = input("Введите название или автора книги для поиска: ")
            library.search_book(query)
        elif choice == 6:
            print("Выход из программы.")
            break
        else:
            print("Неправильный выбор. Пожалуйста, попробуйте еще раз.")


if __name__ == "__main__":
    main()

