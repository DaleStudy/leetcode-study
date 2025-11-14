class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        answer = 0
        while num_set:
            num = num_set.pop()
            l, r = 1, 1
            
            while num - l in num_set:
                num_set.remove(num-l)
                l += 1
            
            while num + r in num_set:
                num_set.remove(num+r)
                r += 1
            
            answer = max(answer, l+r-1)
        return answer
        