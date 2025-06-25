def is_palindrome(s):
    if isinstance(s, int):
        s = str(s)  # Convert integer to string

    if not isinstance(s, str):
        return False #Return false if input is not string or int
    
    return s == s[::-1]

print(is_palindrome(121))  # True
print(is_palindrome("heleh"))  # False