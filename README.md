# EnDek

EnDek is a lightweight terminal-based encryption tool written in Python. It lets you encrypt and decrypt text using a custom or randomly generated key, and it now includes a simple account system and a menu-driven configuration experience.

> **Project Status:** Active development 🚧

---

## New Features

- 🔐 Log in and log out of the application
- 👤 Create new user accounts
- 🧭 A user-friendly configuration menu for managing settings
- 🛡️ Database-level access protection through account authentication
- 🎲 Generate secure random encryption keys
- 🔄 Encrypt and decrypt text using per-user stored keys

---

## How It Works

1. Launch the app from the terminal.
2. Enter your username.
3. If the account already exists, log in with your password.
4. If the account does not exist, you can create a new one.
5. Use the configuration menu to manage your encryption key.
6. Encrypt or decrypt text from the main prompt.

---

## Features

- 🔒 Encrypt and decrypt English text
- 🔑 Use a custom encryption key
- 🎲 Generate a new random encryption key
- 📤 Export the current encryption key
- 🗑️ Clear the stored key data for the current account
- 👤 Delete an account from the user database
- 💾 Store data locally in SQLite database files

---

## Configuration Menu

The configuration menu is now menu-driven and intuitive, so it does not require much setup or extra documentation. From the menu, you can:

- update the active encryption key
- generate a new random key
- export the current key
- manage account options
- clear stored database data

---

## Account System

When you start EnDek:

- existing users can log in
- new users can create an account
- accounts are stored in a local SQLite database file named users.db
- each user has their own encryption key table in encyption_keys.db

---

## Security Notes

- Access to your encryption key data is protected by username and password authentication.
- The app uses local SQLite databases rather than a remote service.
- Exporting keys requires password confirmation.
- Use a strong password for your account to help protect your stored keys.

---

## Installation

### Windows

1. Install Python 3.
2. Install Git (or GitHub Desktop).
3. Open a terminal and run:

```bash
git clone https://github.com/yourusername/EnDek.git
cd EnDek
python Encrypter.py
```

### macOS

1. Install Python 3 and Git.
2. Open Terminal.
3. Run:

```bash
git clone https://github.com/yourusername/EnDek.git
cd EnDek
python3 Encrypter.py
```

---

## Project Status

EnDek is an actively developed personal project. New features, improvements, and security enhancements are added regularly as the project evolves.
