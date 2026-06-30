# Password Generator

A simple Python utility to generate random passwords of any desired length.

## Description

Password Generator is a lightweight command-line tool that creates secure random passwords. You can specify the length of your password, and the tool will generate a random password using a combination of uppercase letters, lowercase letters, digits, and special characters.

## Features

- 🔐 Generate cryptographically random passwords
- 📏 Custom password length configuration
- 🔤 Mix of uppercase and lowercase letters
- 🔢 Includes digits (0-9)
- ✨ Includes special characters for enhanced security
- ⚡ Simple and lightweight
- 💻 Easy-to-use command-line interface

## Requirements

- Python 3.x
- No external dependencies required

## Installation

1. Clone the repository:
```bash
git clone https://github.com/argz-code/Password-Generator.git
cd Password-Generator
```

2. Ensure you have Python 3 installed on your system.

## Usage

Run the script:
```bash
python random_pass.py
```

When prompted, enter the desired length of your password:
```
Kindly mention the length of your password: 16
```

The script will generate and display a random password of the specified length.

### Example

```bash
$ python random_pass.py
Kindly mention the length of your password: 12
k9@mP#xL$vQw
```

## How It Works

The Password Generator works by:

1. Prompting the user to input the desired password length
2. Creating a pool of characters including:
   - ASCII letters (a-z, A-Z)
   - Digits (0-9)
   - Punctuation symbols (!@#$%^&*, etc.)
3. Randomly selecting characters from this pool for the specified length
4. Displaying the generated password

## Technical Details

- **Language:** Python 3
- **Main File:** `random_pass.py`
- **Dependencies:** Standard library only (random, string)

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## License

This project is open source and available under the MIT License.

## Author

Created by argz-code

## Disclaimer

This tool generates random passwords suitable for most use cases. For highly sensitive applications, consider using dedicated password managers with additional security features.
