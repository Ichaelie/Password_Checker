import re

def check_password_strength(password):
    # Minimum length
    if len(password) < 8:
        return "Weak: Password too short"

    # Regex rules
    if not re.search(r"[A-Z]", password):
        return "Weak: Missing uppercase letter"
    if not re.search(r"[a-z]", password):
        return "Weak: Missing lowercase letter"
    if not re.search(r"[0-9]", password):
        return "Weak: Missing number"
    if not re.search(r"[!@#$%^&*(),.?':{}|<>]", password):
        return "Weak: Missing special character"

    return "Strong password!"

# Main program loop
while True:
    pwd = input("Enter a password to check (or type 'exit' to quit): ")
    if pwd.lower() == "exit":
        break
    print(check_password_strength(pwd))
