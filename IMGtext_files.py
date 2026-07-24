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
│ 3 │ Export Key                              │
│ 4 │ Back                                    │
└─────────────────────────────────────────────┘

Enter selection: _""", end="")
    print(reset, end="")
    user_input_1= input()

    return user_input_1