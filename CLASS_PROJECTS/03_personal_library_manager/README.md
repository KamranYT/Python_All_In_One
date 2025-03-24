# Personal Library Management System

A command-line application for managing your personal book collection, helping you keep track of your reading materials and progress.

## Features

- **Add Books**: Easily add new books to your collection with details like:
  - Title
  - Author
  - Publication Year
  - Genre
  - Reading Status (Read/Unread)

- **Search Functionality**: Find books in your collection by:
  - Title
  - Author

- **Collection Management**:
  - View all books in your collection
  - Update book details
  - Remove books from your collection
  - Track reading progress

- **Data Persistence**: All data is automatically saved to a JSON file, ensuring your collection is preserved between sessions

## Getting Started

### Prerequisites
- Python 3.x

### Installation
1. Clone this repository:
```bash
git clone https://github.com/yourusername/personal-library-management.git
cd personal-library-management
```

### Usage
Run the application:
```bash
python main.py
```

## How to Use

The application presents a user-friendly menu with the following options:

1. **Add a New Book**: Enter book details when prompted
2. **Remove a Book**: Delete books by title
3. **Search for Books**: Find books by title or author
4. **Update Book Details**: Modify existing book information
5. **View All Books**: Display your entire collection
6. **View Reading Progress**: See statistics about your reading progress
7. **Exit**: Save and quit the application

## Data Storage

Books are stored in `books_data.json` in the following format:
```json
[
    {
        "title": "Book Title",
        "author": "Author Name",
        "year": "Publication Year",
        "genre": "Book Genre",
        "read": true/false
    }
]
```

## Contributing

Feel free to fork this repository and submit pull requests to contribute to this project. You can also open issues for bugs or feature requests.

## License

This project is open source and available under the MIT License.
