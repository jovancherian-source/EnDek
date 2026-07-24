# EnDek

EnDek is a terminal-based encryption application written in Python. It allows users to encrypt and decrypt English text using a unique encryption key. The project is intentionally designed as a command-line application, keeping it lightweight, simple, and easy to use.

> **Project Status:** Beta 🚧

---

## Features

- 🔒 Encrypt and decrypt English text
- 🔑 Generate secure random encryption keys
- 📥 Import encryption keys
- 📤 Export encryption keys
- ⚙️ Configuration menu for managing settings
- 👤 User account system *(currently in development)*
- 💻 Lightweight terminal interface

---

## Encryption Keys

Every encrypted message is tied to an encryption key.

From the **Configuration** menu, you can:

- Change the active encryption key
- Generate a new secure random key
- Import an existing encryption key
- Export your current encryption key

This allows EnDek users to securely exchange encrypted messages by sharing the same encryption key.

---

## User Accounts

The user account system is currently under development.

When completed, EnDek will prompt you to create a username and password the first time it is launched.

### Default Beta Account

| Username | Password |
|----------|----------|
| `jovancherian` | `3e3e3e` |

These credentials are included only for testing purposes and can be changed directly in the source code.

---

## Installation

### Windows

1. Install **Python 3**.
2. Install **Git** (or GitHub Desktop).
3. Open a terminal and run:

```bash
git clone https://github.com/yourusername/EnDek.git
cd EnDek
python Encrypter.py
```

### macOS

1. Install **Python 3** and **Git**.
2. Open **Terminal**.
3. Run:

```bash
git clone https://github.com/yourusername/EnDek.git
cd EnDek
python3 Encrypter.py
```

---

## Current Status

EnDek is an actively developed personal project. New features, improvements, and security enhancements are added regularly as the project evolves.

---

## Roadmap

- [ ] Complete the user account system
- [ ] Improve key management
- [ ] Enhance terminal user interface
- [ ] Add additional security improvements
- [ ] Improve documentation

---

## License

No license has been added yet.
