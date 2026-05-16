# Password Complexity Checker

A Python-based cybersecurity tool that assesses the strength of a password based on common security criteria. 

## How It Works
The program uses Regular Expressions (re) to evaluate a user's password against five standard criteria:
1. Length (minimum 8 characters)
2. Presence of uppercase letters
3. Presence of lowercase letters
4. Presence of numeric digits
5. Presence of special characters

Based on the score, the tool grades the password as *Weak, **Moderate, or **Strong* and provides actionable feedback on how the user can improve their password security.

## Usage
1. Ensure you have Python installed on your system. No external libraries are required.
2. Clone this repository or download the password_checker.py file.
3. Open your terminal or command prompt and run the script:
   ```bash
   python password_checker.py
