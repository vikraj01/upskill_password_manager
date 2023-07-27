# upskill_password_manager

`upskill_password_manager` is a simple password manager application implemented in Python using the Tkinter library for the GUI and SQLite for database management. This password manager allows users to store and manage their passwords for various applications, websites, and services securely.

## Features

- User-friendly GUI: The password manager provides a user-friendly graphical interface to easily add, view, update, and delete password entries.
- Secure Password Storage: Passwords are encrypted using the Python cryptography package before being stored in the database, ensuring their security.
- Database Integration: The application utilizes SQLite to store and manage password entries in a structured manner.
- URL, Email, and Application Name Storage: The password manager allows users to store additional information, such as the website URL, email address, and application name associated with each password entry.
- Efficient URL Shortening: The password manager implements URL shortening functionality to create concise and manageable links for long URLs.

## Requirements

- Python 3.x
- Tkinter Library (Python Standard Library)
- SQLite (Python Standard Library)
- Cryptography Package (`pip install cryptography`)

## Usage

1. Clone the repository or download the source code.
2. Install the required packages using `pip` if you haven't already installed them.
3. Run the `password_manager.py` script using Python.

## Getting Started

1. Upon running the application, you will be presented with a user-friendly GUI for managing your passwords.
2. To add a new password entry, fill in the application name, URL, email address, and password, and click the "Add Record" button.
3. To view all stored passwords, click the "Show Records" button. This will display a list of all password entries in the application.
4. To update a password entry, enter the ID of the record to be updated in the "Update Record" section and click the "Update" button. Make the necessary changes in the pop-up window and click "Save Record."
5. To delete a password entry, enter the ID of the record to be deleted in the "Delete Record" section and click the "Delete" button.

## Contribution

Contributions to the `upskill_password_manager` project are welcome! If you find any issues or have ideas for improvements, feel free to create an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

Special thanks to the contributors and developers of the Python Tkinter library, SQLite, and the cryptography package for their valuable contributions to the Python ecosystem.

Happy password managing!
