import re

def check_password_strength(password):
    # Check password length
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."
    
    # Check for lowercase letters
    if not re.search("[a-z]", password):
        return "Weak: Password should contain lowercase letters."
    
    # Check for uppercase letters
    if not re.search("[A-Z]", password):
        return "Weak: Password should contain uppercase letters."
    
    # Check for numbers
    if not re.search("[0-9]", password):
        return "Weak: Password should contain numbers."
    
    # Check for special characters
    if not re.search("[!@#$%^&*()]", password):
        return "Weak: Password should contain special characters."
    
    # If all checks pass
    return "Strong: Password meets all criteria."

# Get user input
password = input("Enter a password: ")

# Check password strength
result = check_password_strength(password)
print(result)
