'''
Brainstorm
- brute force: double for-loop O(N^2)
- efficient: use hash map O(N)

plan
1. check the string lengths. Return false if different
2. Initialize the dictionary
3. Check the dictionary
    3-1. If all counts are zero, strings are anagrams. Return True
    3-2. If not, return False
'''
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    
    for char in t:
        if char in count:
            count[char] -= 1
            if count[char] < 0:
                return False
        else:
            return False
    
    return all(x == 0 for x in count.values())

#TC: O(N), SC: O(N) 

#Normal case
print(isAnagram("anagram", "nagaram") == True) 
print(isAnagram("rat", "car") == False) 

#Edge case
print(isAnagram("", "") == True) 


