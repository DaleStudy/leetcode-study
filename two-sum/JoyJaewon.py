'''
Brainstorm
- Brute force: double for-loop / recursion - O(N^2)
- Two Pointer: O(nlogn) - sorting
- Efficient approach: use hashmap to go through the array once O(N)

Plan
1. Initialize the dictionary
2. Iterate over the array
    2-1. For each number, calculate the complement
    2-2. check if the complement exists in the dictionary
        2-3. Return the indices if it exists
    2-4. If not, add the current number and its index to the dictionary
'''

def twoSum(nums, target):
    memo = {}  
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in memo:           
            return [memo[diff], i]
        memo[nums[i]] = i 

#TC:O(N), SC:O(N)

#Normal case
print(twoSum([2, 7, 11, 15], 9) == [0, 1])
print(twoSum([3, 2, 4], 6) == [1, 2])

#Edge case
print(twoSum([1, 2], 3) == [0, 1])
print(twoSum([1, 5, 10], 20) == None) 

