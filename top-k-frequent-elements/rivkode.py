from typing import List

# Time Complexity O(n log n)
# - traversing for loop takes O(n) to create hash dictionary,
# - and when sorting by sorted function(TimSort) it takes O(nlogn)
# Space Complexity O(n log n)
# - creating hash dictionary takes O(n)
# - and when sorting takes O(n), hash[x] occupy O(1)

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        dic = {}

        for v in nums:
            if v in dic:
                cur = dic[v]
                cur += 1
                dic[v] = cur
            else:
                dic[v] = 1

        reverse_desc = sorted(dic.items(), key=lambda item: item[1], reverse=True)

        n = 0
        result = []
        for v in reverse_desc:
            if n == k:
                break
            
            result.append(v[0])
            n += 1
        
        return result

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
