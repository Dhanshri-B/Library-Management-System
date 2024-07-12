import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO


class LibraryManagementSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Library Management System")
        self.books = {}

        # Configure styles
        style = ttk.Style()
        style.configure("TLabel", font=("Helvetica", 12), background="#f0f0f0")
        style.configure(
            "TButton",
            font=("Helvetica", 10),
            background="#4CAF50",
            foreground="black",
            padding=6,
        )
        style.configure("TEntry", padding=6)
        style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"))

        # Load logo image
        logo_url = "https://storage.googleapis.com/ezap-prod/colleges/1863/st-john-college-logo.gif"
        response = requests.get(logo_url)
        image_data = BytesIO(response.content)
        logo_image = Image.open(image_data)
        logo_image = logo_image.resize((200, 120), Image.ANTIALIAS)
        self.logo_photo = ImageTk.PhotoImage(logo_image)

        self.label_logo = tk.Label(master, image=self.logo_photo, background="#f0f0f0")
        self.label_logo.grid(row=0, column=0, columnspan=4, pady=10)

        self.label_title = tk.Label(
            master,
            text="Library Management System Project (Group Lead: Dhanshri Badgujar)",
            font=("Helvetica", 16, "bold"),
            background="#f0f0f0",
        )
        self.label_title.grid(row=1, column=0, columnspan=4, pady=10)

        self.label_book_title = ttk.Label(master, text="Book Title:")
        self.label_book_title.grid(row=2, column=0, padx=10, sticky="e")
        self.entry_book_title = ttk.Entry(master)
        self.entry_book_title.grid(row=2, column=1, padx=10, sticky="w")

        self.label_author = ttk.Label(master, text="Author:")
        self.label_author.grid(row=3, column=0, padx=10, sticky="e")
        self.entry_author = ttk.Entry(master)
        self.entry_author.grid(row=3, column=1, padx=10, sticky="w")

        self.label_genre = ttk.Label(master, text="Genre:")
        self.label_genre.grid(row=4, column=0, padx=10, sticky="e")
        self.entry_genre = ttk.Entry(master)
        self.entry_genre.grid(row=4, column=1, padx=10, sticky="w")

        self.label_quantity = ttk.Label(master, text="Quantity:")
        self.label_quantity.grid(row=5, column=0, padx=10, sticky="e")
        self.entry_quantity = ttk.Entry(master)
        self.entry_quantity.grid(row=5, column=1, padx=10, sticky="w")

        self.button_add_book = ttk.Button(
            master, text="Add Book", command=self.add_book
        )
        self.button_add_book.grid(row=6, column=0, columnspan=2, pady=10)

        self.label_search = ttk.Label(master, text="Search Book:")
        self.label_search.grid(row=7, column=0, padx=10, sticky="e")
        self.entry_search = ttk.Entry(master)
        self.entry_search.grid(row=7, column=1, padx=10, sticky="w")

        self.button_search = ttk.Button(master, text="Search", command=self.search_book)
        self.button_search.grid(row=8, column=0, columnspan=2, pady=10)

        self.table = ttk.Treeview(
            master, columns=("Title", "Author", "Genre", "Quantity", "Available")
        )
        self.table.heading("#0", text="ID")
        self.table.column("#0", width=60)
        self.table.heading("Title", text="Title")
        self.table.heading("Author", text="Author")
        self.table.heading("Genre", text="Genre")
        self.table.heading("Quantity", text="Quantity")
        self.table.heading("Available", text="Available")
        self.table.grid(
            row=2, column=2, rowspan=7, columnspan=3, padx=10, sticky="nsew"
        )

        self.button_update_book = ttk.Button(
            master, text="Update Book", command=self.load_book_for_update
        )
        self.button_update_book.grid(row=9, column=0, columnspan=2, pady=10)

        self.button_delete_book = ttk.Button(
            master, text="Delete Book", command=self.delete_book
        )
        self.button_delete_book.grid(row=10, column=0, columnspan=2, pady=10)

        self.button_confirm_update = ttk.Button(
            master, text="Confirm Update", command=self.update_book
        )
        self.button_confirm_update.grid(row=11, column=0, columnspan=2, pady=10)
        self.button_confirm_update.grid_remove()  # Hide this button initially

        self.update_table()

        master.bind("<Configure>", self.resize_table)
        master.configure(background="#f0f0f0")

    def resize_table(self, event):
        table_width = event.width - 200  # Adjust for other widgets
        self.table.column("Title", width=int(table_width * 0.3))
        self.table.column("Author", width=int(table_width * 0.2))
        self.table.column("Genre", width=int(table_width * 0.2))
        self.table.column("Quantity", width=int(table_width * 0.1))
        self.table.column("Available", width=int(table_width * 0.2))

    def add_book(self):
        title = self.entry_book_title.get()
        author = self.entry_author.get()
        genre = self.entry_genre.get()
        quantity = self.entry_quantity.get()
        if title and author and genre and quantity:
            self.books[title] = {
                "Author": author,
                "Genre": genre,
                "Quantity": int(quantity),
                "Available": int(quantity),
            }
            self.update_table()
            messagebox.showinfo("Success", "Book added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please enter all book details.")

    def search_book(self):
        title = self.entry_search.get()
        self.table.delete(*self.table.get_children())
        for idx, (book_title, details) in enumerate(self.books.items(), start=1):
            if (
                book_title.lower().startswith(title.lower())
                and details["Available"] > 0
            ):
                self.table.insert(
                    "",
                    "end",
                    text=idx,
                    values=(
                        book_title,
                        details["Author"],
                        details["Genre"],
                        details["Quantity"],
                        details["Available"],
                    ),
                )
        if not self.table.get_children():
            messagebox.showinfo(
                "Book Not Found", f"No available book found starting with: {title}"
            )

    def update_table(self):
        self.table.delete(*self.table.get_children())
        for idx, (title, details) in enumerate(self.books.items(), start=1):
            self.table.insert(
                "",
                "end",
                text=idx,
                values=(
                    title,
                    details["Author"],
                    details["Genre"],
                    details["Quantity"],
                    details["Available"],
                ),
            )

    def clear_entries(self):
        self.entry_book_title.delete(0, tk.END)
        self.entry_author.delete(0, tk.END)
        self.entry_genre.delete(0, tk.END)
        self.entry_quantity.delete(0, tk.END)

    def load_book_for_update(self):
        selected_item = self.table.selection()
        if selected_item:
            item = self.table.item(selected_item)
            title = item["values"][0]
            author = item["values"][1]
            genre = item["values"][2]
            quantity = item["values"][3]
            self.entry_book_title.delete(0, tk.END)
            self.entry_book_title.insert(0, title)
            self.entry_author.delete(0, tk.END)
            self.entry_author.insert(0, author)
            self.entry_genre.delete(0, tk.END)
            self.entry_genre.insert(0, genre)
            self.entry_quantity.delete(0, tk.END)
            self.entry_quantity.insert(0, quantity)
            self.button_confirm_update.grid()  # Show the Confirm Update button
        else:
            messagebox.showerror("Error", "Please select a book to update.")

    def update_book(self):
        selected_item = self.table.selection()
        if selected_item:
            item = self.table.item(selected_item)
            old_title = item["values"][0]
            new_title = self.entry_book_title.get()
            author = self.entry_author.get()
            genre = self.entry_genre.get()
            quantity = self.entry_quantity.get()
            if new_title and author and genre and quantity:
                del self.books[old_title]
                self.books[new_title] = {
                    "Author": author,
                    "Genre": genre,
                    "Quantity": int(quantity),
                    "Available": int(quantity),
                }
                self.update_table()
                messagebox.showinfo("Success", "Book updated successfully!")
                self.clear_entries()
                self.button_confirm_update.grid_remove()  # Hide the Confirm Update button
            else:
                messagebox.showerror("Error", "Please enter all book details.")
        else:
            messagebox.showerror("Error", "Please select a book to update.")

    def delete_book(self):
        selected_item = self.table.selection()
        if selected_item:
            item = self.table.item(selected_item)
            del self.books[item["values"][0]]
            self.update_table()
            messagebox.showinfo("Success", "Book deleted successfully!")
        else:
            messagebox.showerror("Error", "Please select a book to delete.")


def main():
    root = tk.Tk()
    app = LibraryManagementSystem(root)
    root.resizable(False, False)
    root.geometry("1000x700")  # Adjusted to fit additional buttons
    root.mainloop()


if __name__ == "__main__":
    main()
