import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Check Length (At least 8 characters)
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("[-] Password should be at least 8 characters long.")

    # Check for Uppercase Letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("[-] Add at least one uppercase letter.")

    # Check for Lowercase Letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("[-] Add at least one lowercase letter.")

    # Check for Numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("[-] Add at least one number.")

    # Check for Special Characters
    if re.search(r"[\W_]", password):
        score += 1
    else:
        feedback.append("[-] Add at least one special character (e.g., !@#$%^&*).")

    # Determine Overall Strength
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

def main():
    print("--- Password Complexity Checker ---")
    password = input("Enter a password to test: ")
    
    strength, feedback = check_password_strength(password)
    
    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Suggestions to improve:")
        for tip in feedback:
            print(tip)

if __name__ == "__main__":
    main()