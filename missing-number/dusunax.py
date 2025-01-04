'''
# 268. Missing Number

A. iterative approach: sort the array and find the missing number.
B. XOR approach: use XOR to find the missing number.
    - a ^ a = 0, a ^ 0 = a

## Time and Space Complexity

### A. Iterative Approach

```
TC: O(n log n)
SC: O(1)
```

#### TC is O(n):
- sorting the array. = O(n log n)
- iterating through the array just once to find the missing number. = O(n)

#### SC is O(1):
- no extra space is used. = O(1)

### B. XOR Approach

```
TC: O(n)
SC: O(1)
```

#### TC is O(n):
- iterating through the array just once to find the missing number. = O(n)

#### SC is O(1):
- no extra space is used. = O(1)

'''
class Solution:
    '''
    A. Iterative Approach
    '''
    def missingNumberIterative(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        for i in range(n):
            if nums[i] != i:
                return i
        return n
    
    '''
    B. XOR Approach
    '''
    def missingNumberXOR(self, nums: List[int]) -> int:
        n = len(nums)
        xor_nums = 0

        for i in range(n + 1):
            if i < n:
                xor_nums ^= nums[i]
            xor_nums ^= i

        return xor_nums
