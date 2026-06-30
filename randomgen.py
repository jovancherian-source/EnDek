import random
symbols = """!@#$%^&*()-_=+[]|;:'",<.>/?~`©®™°§¶†‡¢£¥€₹±×÷√∞≈≠≤≥←→↑↓↔↕⇐⇒⇑⇓★☆✦✧✪✫✬✭✮✯♠♣♥♦♪♫♬♭♮♯✓✔✕✖✗✘☀☁☂☃☄☾☽☕☘☠☢☣⚡⚙⚠⚔⚖✈✉✍✎✏◆◇■□▲△▼▽●○◐◑◒◓◔◕⌘⌥⌫⌦⌨∑∏∫∂∇αβγδεζηθλμπσφω⊕⊗⊥⊂⊃⊆⊇∈∉∪∩≡∝∴∵"""
letters = ['a','b', 'c', 'd', 'e' ,'f', 'g' ,'h','i', 'j', 'k', 'l' , 'm' , 'n', 'o', 'p', 'q' , 'r', 's' ,'t', 'u' ," ", 'v', 'w', 'x', 'y', 'z', '.' ]
generated_encryption_key_one_d = []
def randomgenerator():
    for item in letters:
        while item not in generated_encryption_key_one_d:
            random_symbol = random.choice(symbols)
            if random_symbol not in generated_encryption_key_one_d:
                generated_encryption_key_one_d.append(item)
                generated_encryption_key_one_d.append(random_symbol)
    return  str("".join(generated_encryption_key_one_d))

