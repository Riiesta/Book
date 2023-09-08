import tkinter as tk
from tkinter import messagebox, simpledialog


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

    def get_book(self, book_id):
        for book in self.books:
            if book.id == book_id and book.status == "доступна":
                book.status = "взята"
                return "Книга успешно взята!"
        return "Книга недоступна или не найдена."

    def return_book(self, book_id):
        for book in self.books:
            if book.id == book_id and book.status == "взята":
                book.status = "доступна"
                return "Книга успешно возвращена!"
        return "Книга не найдена."

    def display_books(self):
        return '\n'.join(str(book) for book in self.books)


class LibraryApp:
    def __init__(self, root):
        self.library = Library()

        self.title_label = tk.Label(root, text="Библиотека книг", font=("Arial", 24))
        self.title_label.pack(pady=20)

        self.add_book_btn = tk.Button(root, text="Добавить книгу", command=self.add_book)
        self.add_book_btn.pack(pady=10)

        self.borrow_book_btn = tk.Button(root, text="Взять книгу", command=self.borrow_book)
        self.borrow_book_btn.pack(pady=10)

        self.return_book_btn = tk.Button(root, text="Вернуть книгу", command=self.return_book)
        self.return_book_btn.pack(pady=10)

        self.display_books_btn = tk.Button(root, text="Просмотреть все книги", command=self.display_books)
        self.display_books_btn.pack(pady=10)

    def add_book(self):
        title = simpledialog.askstring("Добавление книги", "Введите название книги:")
        author = simpledialog.askstring("Добавление книги", "Введите автора книги:")
        if title and author:
            self.library.add_book(title, author)
            messagebox.showinfo("Успех", "Книга успешно добавлена!")

    def borrow_book(self):
        book_id = simpledialog.askinteger("Взять книгу", "Введите ID книги:")
        if book_id:
            result = self.library.get_book(book_id)
            messagebox.showinfo("Информация", result)

    def return_book(self):
        book_id = simpledialog.askinteger("Вернуть книгу", "Введите ID книги:")
        if book_id:
            result = self.library.return_book(book_id)
            messagebox.showinfo("Информация", result)

    def display_books(self):
        books = self.library.display_books()
        messagebox.showinfo("Все книги", books or "Библиотека пуста")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Библиотека книг")
    root.geometry("300x300")
    app = LibraryApp(root)
    root.mainloop()
