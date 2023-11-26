def has_lowerchar(password):
    return any(char.islower() for char in password)

def has_upperchar(password):
    return any(char.isupper() for char in password)

def has_digit(password):
    return any(char.isdigit() for char in password)

def has_special_char(password):
    special_char = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']
    for char in password:
        if char in special_char:
            return True
        
def password_check(password):
    score = min(max(len(password) // 8, 1), 4)

    complexity = has_lowerchar(password) + has_upperchar(password) + has_digit(password) + has_special_char(password)

    total_score = score + complexity

    strength_info = {
        'length': score,
        'complexity': complexity,
        'total-score': total_score,
        'time_to_crack': estimated_time_to_crack(total_score)
    }

    return strength_info

def estimated_time_to_crack(score):
    if score <= 4:
        return "Less than a second"
    elif score == 5:
        return "Minutes to hours"
    elif score == 6:
        return "Days to months"
    elif score == 7:
        return "Months to years"
    elif score == 8:
        return "Centuries or more"
    
input_password = input("Enter Your Password: ")
result = password_check(input_password)

print("Password Strength Analysis:")
print(f"Length: {result['length']}/4")
print(f"Complexity: {result['complexity']}/4")
print(f"Total Score: {result['total_score']}/8")
print(f"Estimated Time to Brute Force: {result['time_to_crack']}")
