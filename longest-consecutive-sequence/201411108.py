# TC: O(n), set의 원소를 하나씩 확인하기 때문에 O(n)
# SC : O(n), 최대 n개의 원소가 set에 들어갈 수 있기 때문에 O(n)
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        max_len = 0

        for num in nums_set:
            if num - 1 in nums_set: # 이전 숫자가 존재하는(연속 시작점이 있는) 경우에는 continue
                continue
            
            acc = 1
            while num + acc in nums_set:
                acc += 1
            
            max_len = max(max_len, acc)
        
        return max_len

