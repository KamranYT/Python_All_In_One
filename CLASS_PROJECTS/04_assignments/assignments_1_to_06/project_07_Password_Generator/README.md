# CLI Password Generator

A simple yet powerful command-line interface (CLI) tool that generates random secure passwords based on user specifications.

## Features

- Generate multiple passwords at once
- Customizable password length
- Includes a mix of:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Special characters (!@$%&*().,?)

## How to Use

1. Run the script using Python:
   ```bash
   python main.py
   ```

2. When prompted, enter:
   - The number of passwords you want to generate
   - The desired length for each password

3. The program will display your generated passwords

## Example

```
Welcome To Your Password Generator
Enter Amount of passwords to generate: 3
Enter Your Password Length: 12

here are your passwords:
Kj@5nL$mP9&x
vT7*wQ2cR!4n
pY9$hB5vM@3k
```

## Requirements

- Python 3.x
- No additional packages required (uses only built-in Python libraries)

## Security Note

The password generator uses Python's `random` module to create passwords with a mix of characters. The generated passwords include a combination of uppercase letters, lowercase letters, numbers, and special characters to enhance security.
