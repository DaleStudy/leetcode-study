"""
	/풀이 봐도 잘 이해 못해서 추가 코멘트/
	nums[i]가 그 전까지 subarray의 합 total보다 작은 음수인 케이스는 어떻게 되는거지 고민했는데
	ex) total : -1, nums[i] = -2
	어차피 -1인 시점에 maxTotal이 업데이트 됐으므로 total은 nums[i]부터 더하기 시작한다는 의미로 -2로 설정한다는 것을 깨달음
	따라서 이전까지 subarray의 합만 음수 양수 체크
	
	TC : for문 한번
		=> O(N)
	SC : 추가적인 배열 등 메모리 쓰지 않으므로
		=> O(1)
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = nums[0]
        maxTotal = nums[0]
        for i in range(1, len(nums)) :
            if (total < 0) :
                total = nums[i]
            else :
                total += nums[i]
            maxTotal = max(total, maxTotal)
        return (maxTotal)
