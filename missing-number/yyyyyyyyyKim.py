class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # 시간복잡도 O(n), 공간복잡도 O(1)
        # n = nums의 길이
        # 0부터 n까지 총합 = (n*(n+1))//2
        # 총합에서 nums의 합을 빼면 빠진 수를 구할 수 있음
        return (len(nums)*(len(nums)+1))//2 - sum(nums)
