class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = dict()
        sorted(nums)
        for num in nums:
            if hashmap.get(num, False) == True: 
                return True
            else :
                hashmap[num] = True
        return False
