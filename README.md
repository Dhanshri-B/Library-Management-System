# Library-Management-System

This is a simple Library Management System implemented in Python using the Tkinter GUI library. The system allows you to perform CRUD (Create, Read, Update, Delete) operations on a collection of books in a library.

## Features

- **Add Book**: Add a new book with details such as title, author, genre, and quantity.
- **Search Book**: Search for a book by its title.
- **Update Book**: Update details of an existing book.
- **Delete Book**: Delete a book from the library.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/library-management-system.git
    cd library-management-system
    ```

2. Install the required dependencies:

    ```bash
    pip install pillow requests
    ```

3. Run the application:

    ```bash
    python lib_mgmt.py
    ```

## Usage

- **Add Book**: Enter the book details in the input fields and click "Add Book".
- **Search Book**: Enter the book title in the search field and click "Search".
- **Update Book**: Select a book from the table, click "Update Book", modify the details, and click "Confirm Update".
- **Delete Book**: Select a book from the table and click "Delete Book".

## Screenshots

![Library Management System](path_to_screenshot.png)

## Dependencies

- `tkinter`: Standard Python interface to the Tk GUI toolkit.
- `Pillow`: Python Imaging Library (PIL) fork for image processing.
- `requests`: HTTP library for downloading the logo image.

## Code Overview

The main application is implemented in the `lib_mgmt.py` file. The `LibraryManagementSystem` class contains all the methods and widgets needed for the application.

### Adding Books

The `add_book` method adds a new book to the `books` dictionary and updates the table view.

### Searching Books

The `search_book` method filters the books based on the search input and updates the table view accordingly.

### Updating Books

The `load_book_for_update` method loads the selected book's details into the input fields for editing. The `update_book` method saves the changes and updates the table view.

### Deleting Books

The `delete_book` method deletes the selected book from the `books` dictionary and updates the table view.

## License

This project is licensed under the MIT License.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.


