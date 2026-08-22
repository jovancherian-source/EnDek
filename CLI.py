def logos():
    orange = "\033[38;5;214m"
    reset = "\033[0m"

    print(orange)

    print(r"""
  ███████╗        
  ██╔════╝      ██████╗       ██╗  ██╗
  ██║    _ __   ██╔══██╗      ██║ ██╔╝
  █████╗| '_ \  ██║  ██║/ _ \ ██╠═██╔╝
  ██╔══╝| | | | ██║  ██║  __/ ██║╚██╗ 
  ██║   |_| |_| ██████╔╝\___| ██║ ╚██╗
  ███████╗      ╚═════╝       ╚═╝  ╚═╝
                 EnDek
    """)

    print(reset)

def EnDek_config_logo():
    orange = "\033[38;5;214m"
    reset = "\033[0m"

    print(orange)
    print(r"""╔══════════════════════════════╗
║         EnDek Config         ║
╠══════════════════════════════╣
║ 1. Encryption Settings       ║
║ 2. Account Settings          ║
║ 3. Database Settings         ║
║ 4. About EnDek               ║
║ 5. Exit                      ║
╚══════════════════════════════╝

Choice:""", end="")
    print(reset, end="")
    return ""

def EnDek_encyption_settings_menu():
    orange = "\033[38;5;214m"
    reset = "\033[0m"

    print(orange)
    print(r"""┌─────────────────────────────────────────────┐
│ 🔐 Encryption Settings                      │
├─────────────────────────────────────────────┤
│ 1 │ enter custom key                        │
│ 2 │ Generate Secure Random Key              │
| 3 │ Scramble settings                       │
│ 4 │ Export Key                              │
│ 5 │ Back                                    │
└─────────────────────────────────────────────┘

Enter selection: _""", end="")
    print(reset, end="")
    user_input_1= input()

    return user_input_1

def Database_settings_menu():
    orange = "\033[38;5;214m"
    reset = "\033[0m"

    print(orange)
    print(r"""╔═════════════════════════════════════╗
║         Database Settings           ║
╠═════════════════════════════════════╣
║ ⚠ Warning                           ║
║ Clearing the database permanently   ║
║ removes all stored data.            ║
╠═════════════════════════════════════╣
║ 1 │ Clear Database                  ║
║ 2 │ ← Back                          ║
╚═════════════════════════════════════╝
""", end="")
    print(reset, end="")
    user_input_1= input(r"Enter selection: _")

    return user_input_1
def Account_settings_menu():
    orange = "\033[38;5;214m"
    reset = "\033[0m"

    print(orange)
    print(r"""╔═════════════════════════════════════╗
║          Account Settings           ║
╠═════════════════════════════════════╣
║ General                             ║
║ ─────────────────────────────────── ║
║ 1 │ Log Out                         ║
║                                     ║
║ Danger Zone                         ║
║ ─────────────────────────────────── ║
║ 2 │ Delete Account                  ║
║                                     ║
║ 3 │ ← Back                          ║
╚═════════════════════════════════════╝

Select an option (1-3):
""", end="")
    print(reset, end="")
    user_input_1= input(r"Enter selection: _")

    return user_input_1
def Account_confirmation_menu():
    orange = "\033[38;5;214m"
    reset = "\033[0m"

    print(orange)
    print(r"""╔═════════════════════════════════════╗
║         Delete Account              ║
╠═════════════════════════════════════╣
║ This action cannot be undone.       ║
║                                     ║
║ Your account and all associated     ║
║ data will be permanently deleted.   ║
║                                     ║
║ 1 │ Yes, Delete My Account          ║
║ 2 │ Cancel                          ║
╚═════════════════════════════════════╝

Select an option:
""", end="")
    print(reset, end="")
    user_input_1= input(r"Enter selection: _")

    return user_input_1
def first_Scramble_settings_menu():
    orange = "\033[38;5;214m"
    reset = "\033[0m"

    print(orange)
    print(r"""╔══════════════════════════════════════╗
║          Scramble Settings           ║
╠══════════════════════════════════════╣
║ 1 │ Enable Text Scrambling           ║
║──────────────────────────────────────║
║ 2 │ ← Back                           ║
╚══════════════════════════════════════╝

Select an option (1-2):
""", end="")
    print(reset, end="")
    user_input_1= input(r"Enter selection: _")

    return user_input_1
def Scramble_settings_menu():
    orange = "\033[38;5;214m"
    reset = "\033[0m"

    print(orange)
    print(r"""╔══════════════════════════════════════╗
║         Scrambler Settings           ║
╠══════════════════════════════════════╣
║ 1 │ Change Scrambler                 ║
║──────────────────────────────────────║
║ 2 │ Disable Scrambler                ║
║──────────────────────────────────────║
║ 3 │ ← Back                           ║
╚══════════════════════════════════════╝

Select an option (1-3):
""", end="")
    print(reset, end="")
    user_input_1= input(r"Enter selection: _")

    return user_input_1

def new_Scramble_settings_menu():
    orange = "\033[38;5;214m"
    reset = "\033[0m"

    print(orange)
    print(r"""══════════════════════════════════════
          SCRAMBLER KEY
══════════════════════════════════════

[1] Enter Custom Scrambler Key
[2] Generate Random Scrambler Key
[3] Cancel

Select an option: 
""", end="")
    print(reset, end="")
    user_input_1= input(r"Enter selection: _")

    return user_input_1
def new_Scramble_key_for_pre_user():
    orange = "\033[38;5;214m"
    reset = "\033[0m"

    print(orange)
    print(r"""══════════════════════════════════════
       CUSTOM SCRAMBLER KEY
══════════════════════════════════════

""", end="")
    print(reset, end="")
    user_input_1= input(r"> ")

    return user_input_1