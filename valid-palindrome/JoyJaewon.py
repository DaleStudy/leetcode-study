'''
Brainstorm
- Brute force: double for-loop O(N^2)
- Efficient: two pointer O(N)

Plan
1. Preprocess the input data (lowercase, remove non-alphanumeric char)
2. Use two pointers to check for palindrome
'''
#Version 1
def isPalindrome(s):
    filtered_chars = [c.lower() for c in s if c.isalnum()]
    left, right = 0, len(filtered_chars) - 1

    while left < right:
        if filtered_chars[left] != filtered_chars[right]:
            return False
        left, right = left + 1, right - 1
    
    return True


#Version 2
def isPalindrome2(s):
    filtered_chars = [c.lower() for c in s if c.isalnum()]
    return filtered_chars == filtered_chars[::-1]


#TC: O(N), SC: O(N)

#Normal case
print(isPalindrome("A man, a plan, a canal: Panama") == True) 
print(isPalindrome("race a car") == False) 

#Edge case
print(isPalindrome("") == True) 
print(isPalindrome(" ") == True) 
print(isPalindrome("a.") == True) 

