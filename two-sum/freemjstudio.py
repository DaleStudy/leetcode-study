class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        hashmap = dict()
        for i in range(len(nums)):
            current_num = nums[i]
            diff = target - current_num
            if diff in hashmap.keys():
                return [i, hashmap[diff]]
            hashmap[current_num] = i # store the index of current num

        return answer
