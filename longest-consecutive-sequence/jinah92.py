class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result, last = 0, None
        candidates = []

        for num in sorted(set(nums)):
            if last is None or last + 1 == num:
                result += 1
            else:
                candidates.append(result)
                result = 1
            last = num
            
        if result is not 0:
            candidates.append(result)

        return max(candidates) if len(candidates) > 0 else 0

