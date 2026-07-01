# EnDek

EnDek is a terminal-based Python application that encrypts English text using a randomly generated encryption key. Since the program solves a simple task, it is intentionally designed as a command-line application rather than a graphical user interface.

The application includes a configuration menu where you can change the active encryption key. You can either generate a new random key or import a key shared by another EnDek user, making it easy to exchange encrypted messages with others.

## User Accounts

When user accounts are fully implemented, EnDek will prompt you to create a username and password the first time you launch the program. This feature is currently in development.

For the current beta version, the default credentials are:

* **Username:** `jovancherian`
* **Password:** `3e3e3e`

You can change these values directly in the source code if you wish.

If you do not want to create or use a user account, you can still encrypt messages by generating or entering an encryption key manually. However, decrypting messages requires logging in with a valid user account (the default account can be used).

## Installation

### Windows

1. Install Python if it is not already installed.
2. Install Git, or use GitHub Desktop if you prefer.
3. Open Git Bash or another terminal and run:

```bash
git clone https://github.com/yourusername/EnDek.git
cd EnDek/EnDek-main
python Encrypter.py
```

### macOS

1. Ensure Python 3 and Git are installed.
2. Open Terminal and navigate to the folder where you want to install EnDek.
3. Run:

```bash
git clone https://github.com/yourusername/EnDek.git
cd EnDek/EnDek-main
python3 Encrypter.py
```


