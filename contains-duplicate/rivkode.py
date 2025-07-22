
# Time complexity: O(n)
# The process of traversing a list to generate a set is proportional to the length of the input list.
# Space complexity: O(n)
# The size of the set for storing deduplicated elements is proportional to the length of the input list.

class Solution:
    def containsDuplicate(self, nums):
        list_num = len(nums)
        set_num = len(set(nums))

        if list_num != set_num:
            return True
        else:
            return False

if __name__ == "__main__":
    solution = Solution()

    # test case
    test_string = [
        [1,2,3,1],  # True
        [1,2,3,4], # False
        [1,1,1,3,3,4,3,2,4,2],  # True
    ]

    for index, test in enumerate(test_string):
        print(f"start {index} test")
        print(f"input : {test}")
        print(f"Is valid palindrome ? {solution.containsDuplicate(test)}\n")
