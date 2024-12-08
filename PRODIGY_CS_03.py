import re

def check_password_strength(password):
    """
    Check the strength of a password based on predefined criteria.
    
    :param password: str - The password to check.
    :return: tuple (str, str) - Strength level and feedback message.
    """
    # Criteria for password complexity
    criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "numbers": bool(re.search(r"\d", password)),
        "special_characters": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }

    # Calculate the number of criteria met
    score = sum(criteria.values())

    # Determine strength and feedback
    if score == 5:
        strength = "Strong"
        feedback = "Your password is strong. Well done!"
    elif score == 4:
        strength = "Moderate"
        feedback = "Your password is good but could be stronger. Consider adding more complexity."
    elif score == 3:
        strength = "Weak"
        feedback = "Your password is weak. Consider adding uppercase letters, numbers, or special characters."
    else:
        strength = "Very Weak"
        feedback = "Your password is very weak. It should be at least 8 characters long and include a mix of letters, numbers, and special characters."

    return strength, feedback

def main():
    print("Password Complexity Checker")
    password = input("Enter a password to check its strength: ")

    strength, feedback = check_password_strength(password)
    print(f"\nPassword Strength: {strength}")
    print(f"Feedback: {feedback}")

if __name__ == "__main__":
    main()
