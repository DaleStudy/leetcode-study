from typing import List

# Time Complexity O(n log n)
# - traversing for loop takes O(n) to create hash dictionary,
# - and when sorting by sorted function(TimSort) it takes O(nlogn)
# Space Complexity O(n log n)
# - creating hash dictionary takes O(n)
# - and when sorting takes O(n), hash[x] occupy O(1)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = dict()

        # for loop nums to set count for each element in hash(dictionary)
        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1

        # sort (TimSort), using lambda function to set a sorting key which is a count
        return sorted(hash, key=lambda x: hash[x], reverse=True)[:k]

if __name__ == "__main__":
    solution = Solution()

    # test case
    nums_list = [
        [1,1,1,2,2,3], # [1, 2]
        [1] # [1]
    ]
    k_list = [2, 1]

    for i in range(2):
        nums = nums_list[i]
        k = k_list[i]
        result = solution.topKFrequent(nums, k)
        print(f"start{i}")
        print(f"input : {nums}, {k}")
        print(f"result : {result}")
