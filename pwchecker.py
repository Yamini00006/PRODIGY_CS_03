import math
import string

def password_strength(password):
    feedback = []
    strength_score = 0

    length = len(password)
    if length < 8:
        feedback.append("Too short: Use at least 8 characters.")
    elif 8 <= length < 12:
        feedback.append("Good length: Consider using more than 12 characters for better security.")
        strength_score += 1
    else:
        feedback.append("Great length: Your password is sufficiently long.")
        strength_score += 2

    # Criteria: Uppercase and Lowercase Letters
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    if has_upper and has_lower:
        feedback.append("Good mix of uppercase and lowercase letters.")
        strength_score += 2
    else:
        feedback.append("Add a mix of uppercase and lowercase letters for better security.")

    has_numbers = any(char.isdigit() for char in password)
    if has_numbers:
        feedback.append("Great! Your password includes numbers.")
        strength_score += 1
    else:
        feedback.append("Include numbers to make your password stronger.")

    special_chars = set(string.punctuation)
    has_special = any(char in special_chars for char in password)
    if has_special:
        feedback.append("Nice! Your password includes special characters.")
        strength_score += 2
    else:
        feedback.append("Add special characters (e.g., !, @, #) for better security.")

    unique_chars = len(set(password))
    entropy = math.log2(unique_chars ** length)
    if entropy < 50:
        feedback.append("Low entropy: Your password might be easy to guess. Avoid repeating patterns.")
    elif 50 <= entropy < 70:
        feedback.append("Moderate entropy: Good, but there’s room for improvement.")
        strength_score += 1
    else:
        feedback.append("High entropy: Your password is very strong.")
        strength_score += 2

    if strength_score <= 4:
        feedback.append("Overall Strength: Weak. Consider revising your password based on the suggestions.")
    elif 5 <= strength_score <= 7:
        feedback.append("Overall Strength: Moderate. A few tweaks could make it stronger.")
    else:
        feedback.append("Overall Strength: Strong. Great job!")

    return feedback

def main():
    print("Password Strength Assessment Tool\n")
    password = input("Enter your password: ")
    feedback = password_strength(password)

    print("\nFeedback:")
    for item in feedback:
        print(f"- {item}")

if __name__ == "__main__":
    main()
