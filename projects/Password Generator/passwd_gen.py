import random
import string


def generate_password(length, use_lowercase, use_uppercase, use_digits, use_symbols, exclude_ambiguous):
    characters = []
    if use_lowercase:
        characters.extend(list(string.ascii_lowercase))
    if use_uppercase:
        characters.extend(list(string.ascii_uppercase))
    if use_digits:
        characters.extend(list(string.digits))
    if use_symbols:
        characters.extend(list(string.punctuation))

    if exclude_ambiguous:
        ambiguous_chars = ['l', 'I', '1', 'O', '0']
        characters = [char for char in characters if char not in ambiguous_chars]

    if not characters:
        print("Error: No character types selected!")
        return None

    password = []
    # Ensure at least one of each selected type
    if use_lowercase and any(c in string.ascii_lowercase for c in characters):
        password.append(random.choice([c for c in characters if c in string.ascii_lowercase]))
    if use_uppercase and any(c in string.ascii_uppercase for c in characters):
        password.append(random.choice([c for c in characters if c in string.ascii_uppercase]))
    if use_digits and any(c in string.digits for c in characters):
        password.append(random.choice([c for c in characters if c in string.digits]))
    if use_symbols and any(c in string.punctuation for c in characters):
        password.append(random.choice([c for c in characters if c in string.punctuation]))

    for _ in range(length - len(password)):
        password.append(random.choice(characters))

    random.shuffle(password)
    return "".join(password)


def assess_password_strength(password):
    length = len(password)
    has_lowercase = any(c.islower() for c in password)
    has_uppercase = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = 0
    if length >= 8: score += 1
    if length >= 12: score += 1
    if has_lowercase: score += 1
    if has_uppercase: score += 1
    if has_digit: score += 1
    if has_symbol: score += 1

    if score < 3:
        return "Weak"
    elif score < 5:
        return "Medium"
    else:
        return "Strong"


def get_yes_no(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' or 'n'")


def main():
    print("---------------Password Generator---------------\n")

    # Get password length
    while True:
        try:
            length = int(input("Enter password length (minimum 4): "))
            if length >= 4:
                break
            else:
                print("Password must be at least 4 characters long.")
        except ValueError:
            print("Please enter a valid number.")

    # Get character preferences
    use_lowercase = get_yes_no("Include lowercase letters? (y/n): ")
    use_uppercase = get_yes_no("Include uppercase letters? (y/n): ")
    use_digits = get_yes_no("Include digits? (y/n): ")
    use_symbols = get_yes_no("Include symbols? (y/n): ")
    exclude_ambiguous = get_yes_no("Exclude ambiguous characters (l, I, 1, O, 0)? (y/n): ")

    # If no character types selected, use all
    if not (use_lowercase or use_uppercase or use_digits or use_symbols):
        print("\nNo character types selected. Using all types by default.")
        use_lowercase = use_uppercase = use_digits = use_symbols = True

    # Generate password
    print("\nGenerating password...\n")
    password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_symbols, exclude_ambiguous)

    if password:
        print(f"Generated password: {password}")
        print(f"Password strength: {assess_password_strength(password)}")


if __name__ == "__main__":
    main()