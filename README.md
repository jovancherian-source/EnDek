<p align="center">
<img width="451.5" height="219" alt="EnDek_logo" src="https://github.com/user-attachments/assets/23239267-cb61-4694-a8c8-b604b2445a49" />
</p>

## What is EnDek?

EnDek is a lightweight, command-line based encryption software written in Python.

It encrypts plain English text into ciphertext, making the original text unreadable through direct replacement. This provides a simple way to experiment with encryption through an interactive and user-friendly CLI.

EnDek currently uses its own lightweight encryption approach. It is **not intended to replace modern cryptographic standards yet**. A major upcoming update will introduce **AES-256-level encryption**.

EnDek also provides optional local user accounts, stored encryption keys, and an interactive configuration system.

## Why EnDek?

EnDek is designed to make encryption easy to experiment with directly from the terminal.

Instead of requiring complicated commands for every operation, EnDek provides an interactive CLI where you can:

- Encrypt and decrypt text
- Use a custom encryption key
- Generate a secure random key
- Export your current key
- Optionally create an account to store and reuse your key
- Manage encryption and account settings from one configuration menu

---

# Installation

Before installing EnDek, make sure **Python 3** is installed.

## With Git

### Windows

Open PowerShell or Command Prompt:

```powershell
cd <installation location>
git clone https://github.com/jovancherian-source/EnDek.git
cd EnDek
python Encrypter.py
```

### macOS

Open Terminal:

```bash
cd <installation location>
git clone https://github.com/jovancherian-source/EnDek.git
cd EnDek
python3 Encrypter.py
```

### Linux

Open your terminal:

```bash
cd <installation location>
git clone https://github.com/jovancherian-source/EnDek.git
cd EnDek
python3 Encrypter.py
```

---

## Without Git

You can download the repository directly as a ZIP file.

### macOS / Linux

```bash
cd <installation location>
curl -L https://github.com/jovancherian-source/EnDek/archive/refs/heads/main.zip -o EnDek.zip
unzip EnDek.zip
cd EnDek-main
python3 Encrypter.py
```

If your system uses `python` for Python 3:

```bash
cd EnDek-main
python Encrypter.py
```

### Windows PowerShell

```powershell
cd <installation location>
Invoke-WebRequest "https://github.com/jovancherian-source/EnDek/archive/refs/heads/main.zip" -OutFile "EnDek.zip"
Expand-Archive "EnDek.zip" -DestinationPath "."
cd EnDek-main
python Encrypter.py
```

---

# How to Use EnDek

EnDek is designed to be used interactively from the command line.

When you start the program, you can enter either **plain text or ciphertext**. EnDek automatically detects which type of input you have and performs the appropriate operation.

You do **not** need an account to use the basic encryption and decryption functions.

## Accounts

Accounts are optional.

Without an account, you can still encrypt and decrypt text, but some features are limited.

Creating an account stores it locally on your device. Your encryption key can then be remembered and reused later.

The account system uses local SQLite databases rather than a remote service.

- `users.db` stores local user account information.
- `encyption_keys.db` stores encryption keys associated with users.

Account authentication also protects access to stored key data, and exporting a key requires password confirmation.

---

# Configuration Menu

The configuration menu lets you manage the main settings of EnDek without needing to enter complicated commands.

| Option                     | What it does                                                   |
| -------------------------- | -------------------------------------------------------------- |
| **1. Encryption Settings** | Manage your encryption key and encryption options.             |
| **2. Account Settings**    | Log out or delete your current account.                        |
| **3. Database Settings**   | Clear locally stored database data.                            |
| **4. About EnDek**         | View information about the current EnDek version and settings. |
| **5. Exit**                | Exit the configuration menu.                                   |

### Encryption Settings

```text
1. Enter Custom Key
2. Generate Secure Random Key
3. Scramble Settings
4. Export Key
5. Back
```

### Account Settings

```text
1. Log Out
2. Delete Account
```

### Database Settings

```text
1. Clear Database
2. ← Back
```

The **Scramble Settings** option is intended for advanced users who want an additional layer of key transformation.

---

# Key Management

EnDek supports both custom and randomly generated encryption keys.

You can:

- Enter your own key
- Generate a secure random key
- Export your current key
- Store and reuse a key through an account

The encryption key format has also been changed to make the generated key harder to understand at a glance.

**Keep your encryption key safe.** Without the correct key, encrypted data may not be recoverable.

---

# User-Friendly CLI

EnDek is built to be interactive rather than command-heavy.

The program is designed to handle incorrect input without simply crashing. User input is protected throughout the application so that errors are displayed and the user can correct their input and continue using EnDek.

---

# Security

EnDek is an experimental encryption project and is still under active development.

Current security-related features include:

- Local storage through SQLite databases
- Account authentication
- Password confirmation when exporting keys
- Randomly generated encryption keys
- Per-user stored encryption keys
- Additional key-scrambling options for advanced users

The current encryption method is **not equivalent to AES-256**. AES-256-level encryption is planned as a major upcoming update.

Do not use the current version as a replacement for professionally audited cryptographic software for sensitive or critical information.

---

# Project Status

> **Project Status: Partial Development 🚧**

EnDek is an actively developed personal project. The project is evolving toward stronger cryptography while keeping its interactive CLI and user-friendly design.

The next major milestone is the introduction of **AES-256-level encryption**.
