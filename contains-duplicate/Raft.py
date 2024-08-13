class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        appeared = defaultdict(int)
        for n in nums:
            if appeared[n] > 0:
                return True
            appeared[n] += 1
        
        return False

