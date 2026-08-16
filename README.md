# EnDek

EnDek is a lightweight terminal-based encryption tool written in Python. It lets you encrypt and decrypt text using a custom or randomly generated key, and it now includes a simple account system and a menu-driven configuration experience.

> **Project Status:** partial development 🚧

---

## New Features

- 🔐 Log in and log out of the application.
- 👤 Create new user accounts.
- 🧭 A user-friendly configuration menu for managing settings.
- 🛡️ Database-level access protection through account authentication.
- 🎲 Generate secure random encryption keys.
- 🔄 Encrypt and decrypt text using per-user stored keys.

---

## How It Works

1. Launch the app from the terminal.
2. Enter your username.
3. If the account already exists, log in with your password.
4. If the account does not exist, you can create a new one.
5. You do not need to log in or create an account to encrypt or decrypt text.
6. Creating an account only creates it locally on your device, where your encryption key can be remembered and securely stored for later reuse.
7. Use the configuration menu to manage your encryption key.
8. Encrypt or decrypt text from the main prompt.

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

- you do not need to be a user to encrypt or decrypt text
- creating an account is optional and only creates it locally on your device
- accounts are stored in a local SQLite database file named users.db
- each user has their own encryption key table in encyption_keys.db
- the main purpose of creating an account is so your encryption key can be remembered, securely stored, and reused later
- being a user is not required, but it can open up a world of possibilities for smoother and more personalized encryption workflows

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
