# 시간 복잡도 : o(n)
# 공간 복잡도 o(n)


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}

        for i, n in enumerate(nums):
            if n in hashmap:
                return True
            hashmap[n] = i
        return False


# -------------------------------------------------------------------------------------------------------- #

# 시간 복잡도 : o(n)
# 공간 복잡도 o(n)


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False
