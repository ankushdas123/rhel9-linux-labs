# 10_password_checker.py

def check_password_strength(password):
    # Initialize rule flags as False
    has_upper = False
    has_lower = False
    has_digit = False
    
    # Condition: Check if length is at least 8 characters
    length_ok = len(password) >= 8

    # Loop through each character to inspect its type
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    print("\n=========================================")
    print("       PASSWORD STRENGTH REPORT          ")
    print("=========================================")
    print(f"Password Inspected: {password}")
    print("-----------------------------------------")

    # Evaluation: All 4 conditions must be True for a strong password
    if length_ok and has_upper and has_lower and has_digit:
        print("🟢 STATUS: STRONG (🔒 Secure Policy Compliant)")
    else:
        print("🔴 STATUS: WEAK (⚠️ Security Risk Detected!)")
        print("\n[SUGGESTIONS TO IMPROVE]:")
        
        if not length_ok:
            print("❌ Minimum length must be at least 8 characters.")
        if not has_upper:
            print("❌ Add at least one uppercase letter (A-Z).")
        if not has_lower:
            print("❌ Add at least one lowercase letter (a-z).")
        if not has_digit:
            print("❌ Add at least one numeric digit (0-9).")
            
    print("=========================================\n")

# Main execution block
if __name__ == "__main__":
    # Taking live user input
    user_password = input("Enter a password to test security strength: ")
    check_password_strength(user_password)