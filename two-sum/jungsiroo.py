class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
		"""
		O(n^2) 보다 빠르게 풀기 위한 방법 : 정렬 후 투포인터 이용
		Tc : O(nlogn)
		Sc : O(n) // queue 생성
		"""
        n = len(nums)
        queue = []

        for i in range(n):
            queue.append([nums[i], i])

        queue.sort()

        start, end = 0, n-1
        sum_ = queue[start][0] + queue[end][0]

        while sum_ != target:
            if sum_ > target:
                end -= 1
            else:
                start += 1
            sum_ = queue[start][0] + queue[end][0]
        
        return [queue[start][1], queue[end][1]]
            
