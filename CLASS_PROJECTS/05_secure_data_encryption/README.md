# Secure Data Encryption System

## Overview

The **Secure Data Encryption System** is a web application built using Streamlit that allows users to securely register, log in, and store encrypted data. The application utilizes strong encryption techniques to ensure that user data remains confidential and protected from unauthorized access.

## Features

- **User Registration**: Users can create an account with a unique username and password.
- **User Login**: Secure login functionality with lockout mechanism after multiple failed attempts.
- **Data Encryption**: Users can encrypt sensitive data using a passphrase before storing it.
- **Data Retrieval**: Users can retrieve and decrypt their stored data using the correct passphrase.
- **Session Management**: Maintains user sessions to ensure a seamless experience.

## Technologies Used

- **Python**: The primary programming language for the application.
- **Streamlit**: A framework for building web applications in Python.
- **Cryptography**: Utilizes the `cryptography` library for secure encryption and decryption.
- **JSON**: Data is stored in a JSON file for easy access and manipulation.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install the required packages**:
   Make sure you have Python installed, then run:
   ```bash
   pip install streamlit cryptography
   ```

3. **Run the application**:
   Start the Streamlit server with the following command:
   ```bash
   streamlit run main.py
   ```

4. **Access the application**:
   Open your web browser and go to `http://localhost:8501`.

## Usage

1. **Register a New User**:
   - Navigate to the "Register" section.
   - Enter a unique username and password.
   - Click on "Register" to create your account.

2. **Login**:
   - Go to the "Login" section.
   - Enter your username and password.
   - Click on "Login" to access your account.

3. **Store Encrypted Data**:
   - After logging in, navigate to the "Stored Data" section.
   - Enter the data you want to encrypt and a passphrase.
   - Click on "Encrypt and Save" to store the encrypted data.

4. **Retrieve Data**:
   - Go to the "Retrieve Data" section.
   - Enter the encrypted text and the passphrase used for encryption.
   - Click on "Decrypt" to view the original data.

## Security Considerations

- Passwords are hashed using PBKDF2 with a secure salt to protect against brute-force attacks.
- Data is encrypted using the Fernet symmetric encryption method, ensuring confidentiality.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Streamlit](https://mk-data-encryption.streamlit.app/) for providing an easy way to create web applications.
- [Cryptography](https://cryptography.io/en/latest/) for secure encryption and decryption methods.