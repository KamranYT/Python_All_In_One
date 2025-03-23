# 🔐 Password Strength Meter & Generator

A web-based password strength checker and generator built with Streamlit that helps users create and evaluate secure passwords.

## Features

### Password Strength Checker
- Analyzes password strength based on multiple security criteria:
  - Minimum length (8 characters)
  - Mix of uppercase and lowercase letters
  - Numbers (0-9)
  - Special characters (!@#$%^&*)
- Provides real-time feedback with color-coded strength indicators:
  - ✅ Strong (Green): Meets all security criteria
  - 💀 Moderate (Orange): Meets most security criteria
  - ❌ Weak (Red): Needs significant improvement
- Displays specific suggestions for improving password security

### Password Generator
- Generate secure passwords with customizable options:
  - Adjustable length (6-32 characters)
  - Optional inclusion of numbers
  - Optional inclusion of special characters
- Creates random, secure passwords instantly

## How to Use

1. **Check Password Strength:**
   - Enter your password in the secure input field
   - Get immediate feedback on password strength
   - View suggestions for improvement

2. **Generate Strong Password:**
   - Select desired password length using the slider
   - Choose to include numbers and/or special characters
   - Click "Generate Password" to create a secure password

## Security Tips
- Use passwords that are at least 8 characters long
- Combine uppercase and lowercase letters
- Include numbers and special characters
- Avoid using personal information
- Use unique passwords for different accounts

## Built With
- Python
- Streamlit
- Regular Expressions (re)

## Author
Built by [Muhammad Kamran](https://github.com/KamranYT)
