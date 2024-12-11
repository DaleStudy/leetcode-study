'''
# Leetcode 128. Longest Consecutive Sequence

keep time complexity O(n) by iterating through the set and accessing elements in O(1) time. ⚖️

## Time and Space Complexity
```
TC: O(n)
SC: O(n)
```

### TC is O(n):
- iterating through the set. O(n)
- accessing elements in the set. O(1)
- while loop incrementing `current_num` while `current_num + 1 in nums_set`. O(1)

### SC is O(n):
- creating a set from the list of numbers. O(n)
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums) # O(n)
        longest_sequence = 0

        for num in nums_set: # O(n)
            if (num - 1) not in nums_set:
                current_num = num
                current_sequence = 1
            
                while current_num + 1 in nums_set: # O(1) 
                    current_num += 1
                    current_sequence += 1

                longest_sequence = max(current_sequence, longest_sequence)

        return longest_sequence

