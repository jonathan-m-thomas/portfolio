def is_palindrome(s: str) -> bool:
    # Initialize pointers
    left = 0
    right = len(s) - 1
    
    # Loop until pointers cross
    while left < right:
        # Check if characters at pointers are the same
        if s[left] != s[right]:
            return False
        # Move pointers towards the center
        left += 1
        right -= 1
    
    # If the loop completes, it's a palindrome
    return True

str = "racecar"
print("Is ", str, " a palindrome?")
print(is_palindrome(str))