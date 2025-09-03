import random
import string


def generate_password():
    get_lowercase = string.ascii_lowercase
    expected_all_chr = get_lowercase
    random_pass_chr = []
    generated_password = random_pass_chr

    while True:
        try:
            expected_pass_length = int(
                input('Enter the desired password length: ').strip())
            if expected_pass_length < 6:
                print('Password must be at least 6 characters long.')
                continue

        except ValueError:
            print('Enter valid digits')
        else:
            break
    while True:
        include_uppercase = input(
            'Include uppercase latter? (yes/no): ').strip().lower()
        match include_uppercase.lower():
            case 'yes':
                get_uppercase = string.ascii_uppercase
                expected_all_chr += get_uppercase
                random_pass_chr.append(random.choice(get_uppercase))
                break
            case 'no':
                break
            case _:
                print('No match: yes/no')
    while True:
        include_special = input(
            'Include special characters? (yes/no): ').strip().lower()
        match include_special:
            case 'yes':
                get_special = string.punctuation
                expected_all_chr += get_special
                random_pass_chr.append(random.choice(get_special))
                break
            case 'no':
                break
            case _:
                print('No match')
    while True:
        include_digits = input('Include digits? (yes/no): ').strip().lower()
        match include_digits:
            case 'yes':
                get_digit = string.digits
                expected_all_chr += get_digit
                random_pass_chr.append(random.choice(get_digit))
                break
            case 'no':
                break
            case _:
                print('No match: yes/no')

    password_len = expected_pass_length - len(random_pass_chr)
    for _ in range(password_len):
        get_chr = random.choice(expected_all_chr)
        generated_password.append(get_chr)

    print(f"Generated password is: {''.join(generated_password)}")


generate_password()
