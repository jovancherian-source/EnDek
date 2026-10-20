import time
import json
import sys

_ENDEK_BLOCK_LOGO = [
    "                                            ",
    "  ███████╗███╗   ██╗██████╗ ███████╗██╗  ██╗",
    "  ██╔════╝████╗  ██║██╔══██╗██╔════╝██║ ██╔╝",
    "  █████╗  ██╔██╗ ██║██║  ██║█████╗  █████╔╝ ",
    "  ██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔═██╗ ",
    "  ███████╗██║ ╚████║██████╔╝███████╗██║  ██╗",
    "  ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝",
]

_GRADIENT_STEPS = [
    "\033[0m",
    "\033[38;2;238;175;110m",
    "\033[38;2;225;145;98m", 
    "\033[38;2;215;130;94m", 
    "\033[38;2;204;120;92m",  
    "\033[38;2;185;102;76m", 
    "\033[38;2;169;88;62m",
]
def claude_logo():
    for i in range(len(_ENDEK_BLOCK_LOGO)):
        print(_GRADIENT_STEPS[i],_ENDEK_BLOCK_LOGO[i])
        time.sleep(0.025)
    reset = "\033[0m"
    print(reset)

def original_logos():
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

def theme_choice_maker(choice):
    choice_json = {
        "theme" : choice
    }
    with open("config.json", "w") as choice_data:
        json.dump(choice_json, choice_data, indent=2)

def choice_extracter():
    try:
        with open("config.json", "r") as choice_date:
            choice = json.load(choice_date)
            return choice["theme"]
    except FileNotFoundError:
        theme_choice_maker("default")
        return "default"
        
def logo():
    if choice_extracter() == "default":
        original_logos()
    elif choice_extracter() == "claude":
        claude_logo()


def EnDek_config_logo():
    orange = "\033[38;2;238;175;110m"
    reset = "\033[0m"

    print(orange)
    print(r"""╔══════════════════════════════╗
║         EnDek Config         ║
╠══════════════════════════════╣
║ 1. Encryption Settings       ║
║ 2. Account Settings          ║
║ 3. Database Settings         ║
║ 4. EnDek Setttings           ║
║ 5. Exit                      ║
╚══════════════════════════════╝

Choice:""", end="")
    print(reset, end="")
    return ""

def EnDek_encyption_settings_menu():
    orange = "\033[38;2;238;175;110m"
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
    orange = "\033[38;2;238;175;110m"
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
    orange = "\033[38;2;238;175;110m"
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
    orange = "\033[38;2;238;175;110m"
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
    orange = "\033[38;2;238;175;110m"
    reset = "\033[0m"

    print(orange)
    print(r"""╔══════════════════════════════════════╗
║          Scramble Settings           ║
╠══════════════════════════════════════╣
║ 1 │ Enable Text Scrambling           ║
║──────────────────────────────────────║
║ 2 │ ← Back                           ║
╚══════════════════════════════════════╝

Select an option (1/2):
""", end="")
    print(reset, end="")
    user_input_1= input(r"Enter selection: _")

    return user_input_1
def Scramble_settings_menu():
    orange = "\033[38;2;238;175;110m"
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
    orange = "\033[38;2;238;175;110m"
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
    orange = "\033[38;2;238;175;110m"
    reset = "\033[0m"

    print(orange)
    print(r"""══════════════════════════════════════
       CUSTOM SCRAMBLER KEY
══════════════════════════════════════

""", end="")
    print(reset, end="")
    user_input_1= input(r"> ")

    return user_input_1
def endek_dual_settings():
    orange = "\033[38;2;238;175;110m"
    reset = "\033[0m"

    print(orange)
    print(r"""╔═════════════════════════════════════╗
║          EnDek Settings             ║
╠═════════════════════════════════════╣
║                                     ║
║ 1 │ About EnDek                     ║
║ 2 │ Check for Updates               ║
║ 3 │ Clear Cache                     ║
║ 4 │ Theme                           ║
║ 5 │ ← Back                          ║
╚═════════════════════════════════════╝

Select an option (1-5):
""", end="")
    print(reset, end="")
    user_input_1= input(r"Enter selection: _")

    return user_input_1

def endek_update_menu():
    orange = "\033[38;2;238;175;110m"
    reset = "\033[0m"

    print(orange)
    print(fr"""╔═════════════════════════════════════╗
║          EnDek Updates              ║
╠═════════════════════════════════════╣
║        Update Available!!           ║
║ 1 │ update now                      ║
║ 2 │ ← Back                          ║
╚═════════════════════════════════════╝

Select an option (1/2):
""", end="")
    print(reset, end="")
    user_input_1= input(r"Enter selection: _")

    return user_input_1
def endek_themes():
    orange = "\033[38;2;238;175;110m"
    reset = "\033[0m"

    print(orange)
    print(r"""╔═════════════════════════════════════╗
║          EnDek Settings             ║
╠═════════════════════════════════════╣
║                                     ║
║ 1 │ original theme                  ║
║ 2 │ claude code theme               ║
║ 3 │ Custom theme                    ║
║ 4 │ ← Back                          ║
╚═════════════════════════════════════╝

Select an option (1-4):
""", end="")
    print(reset, end="")
    user_input_1= input(r"Enter selection: _")

    return user_input_1

def endek_no_update_menu():
    orange = "\033[38;2;238;175;110m"
    reset = "\033[0m"

    print(orange)
    print(fr"""╔═════════════════════════════════════╗
║          EnDek Updates              ║
╠═════════════════════════════════════╣
║        You are up to date!          ║
║ 1 │ check again                     ║
║ 2 │ force update                    ║
║ 3 │ ← Back                          ║
╚═════════════════════════════════════╝

Select an option (1-3):
""", end="")
    print(reset, end="")
    user_input_1= input(r"Enter selection: _")
    return user_input_1