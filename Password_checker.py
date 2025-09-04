import math

# ---------------- Password Strength ---------------- #

def password_checker(password):
    # Define criteria
    length_error = len(password) < 8
    upper_error = not any(char.isupper() for char in password)
    lower_error = not any(char.islower() for char in password)
    digit_error = not any(char.isdigit() for char in password)
    special_error = not any (char in '[!@#$%^&*(),.?\":{}|<>]' for char in password)

    # Count errors
    errors = [length_error, upper_error, lower_error, digit_error, special_error]
    score = 5 - sum(errors)

    if score == 5:
        strength = "Very strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very weak"

    return strength, errors

# ---------------- Entropy Calculations ---------------- #

def calculate_entropy(password):
    # Count frequency of each unique character
    if not password:
        return 0
    prob = [password.count(char) / len(password) for char in set(password)]
    entropy = -sum(p * math.log2(p) for p in prob)
    # Entropy per character * length of password
    return round(entropy * len(password), 2)

# ---------------- Common Password List ---------------- #

def load_common_passwords(filename="common_passwords.txt"):
    try:
        with open(filename, "r") as f:
            return {line.strip() for line in f}
    except FileNotFoundError:
        return set()


if __name__ == "__main__":
    password = input("Enter a password to check: ")
    strength, errors = password_checker(password)
    print(f"Password strength: {strength}")
    entropy = calculate_entropy(password)
    print(f"Entropy: {entropy} bits")

    common_passwords = load_common_passwords()
    if password in common_passwords:
        print("This is a commonly used password")

    suggestions = []
    if errors[0]: suggestions.append("Make the password at least 8 characters long")
    if errors[1]: suggestions.append("Include at least one uppercase letter")
    if errors[2]: suggestions.append("Include at least one lowercase letter")
    if errors[3]: suggestions.append("Include at least one digit")
    if errors[4]: suggestions.append("Include at least one special character")

    if suggestions:
        print("\nSuggestions to improve your password:")
        for s in suggestions:
            print("- " + s)