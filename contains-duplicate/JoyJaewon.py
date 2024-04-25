'''
Brainstrom
- brute force: double for-loop (O^2)
- efficient approach: use set O(N)

Plan
1. Initialize the set
2. Iterate over the array
    2-1. For each element, check if it's in the set. If it is, return True
    2-2. If not, add the num to the set
3. Return False since no duplicates are found
'''

def containsDuplicate(nums):
    num_set=set()
    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)
    return False

#TC: O(N), SC: O(N)

#Normal case
print(containsDuplicate([1, 2, 3, 1]) == True)
print(containsDuplicate([1, 2, 3, 4]) == False)

#Edge case
print(containsDuplicate([1]) == False)
print(containsDuplicate([]) == False) 