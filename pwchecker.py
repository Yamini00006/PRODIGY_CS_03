import math
import string
import matplotlib.pyplot as plt

def password_strength(password):
    criteria = {
        "Length": 0,
        "Upper/Lower Mix": 0,
        "Numbers": 0,
        "Special Characters": 0,
        "Entropy": 0
    }
    strength_score = 0

    length = len(password)
    if length >= 8:
        if 8 <= length < 12:
            criteria["Length"] = 1
        else:
            criteria["Length"] = 2
        strength_score += criteria["Length"]

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    if has_upper and has_lower:
        criteria["Upper/Lower Mix"] = 2
        strength_score += 2

    has_numbers = any(char.isdigit() for char in password)
    if has_numbers:
        criteria["Numbers"] = 1
        strength_score += 1

    special_chars = set(string.punctuation)
    has_special = any(char in special_chars for char in password)
    if has_special:
        criteria["Special Characters"] = 2
        strength_score += 2

    unique_chars = len(set(password))
    entropy = math.log2(unique_chars ** length) if length > 0 else 0
    if entropy >= 50:
        if 50 <= entropy < 70:
            criteria["Entropy"] = 1
        else:
            criteria["Entropy"] = 2
        strength_score += criteria["Entropy"]

    max_score = sum(criteria.values())
    strength_percentage = (strength_score / max_score) * 100 if max_score > 0 else 0

    return criteria, strength_percentage

def visualize_strength(criteria, strength_percentage):
    labels = list(criteria.keys())
    scores = list(criteria.values())

    plt.figure(figsize=(8, 5))
    plt.bar(labels, scores, color=['blue', 'green', 'orange', 'purple', 'red'])
    plt.title(f"Password Strength: {strength_percentage:.2f}%")
    plt.xlabel("Criteria")
    plt.ylabel("Score")
    plt.ylim(0, 2) 
    plt.axhline(y=1, color='gray', linestyle='--', linewidth=0.7, label='Moderate Threshold')
    plt.axhline(y=2, color='black', linestyle='--', linewidth=0.7, label='Maximum Threshold')
    plt.legend(loc='upper right')
    plt.show()

def main():
    print("Password Strength Assessment Tool\n")
    password = input("Enter your password: ")
    criteria, strength_percentage = password_strength(password)

    print(f"\nYour Password Strength: {strength_percentage:.2f}%")
    visualize_strength(criteria, strength_percentage)

if __name__ == "__main__":
    main()
