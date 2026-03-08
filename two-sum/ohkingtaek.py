class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
	nums를 앞에서부터 하나씩 보면서 현재 값(nums[i])과 더해서 target이 되는 값이 뒤쪽 배열에 있는지 확인합니다.
        있으면 그 값의 index를 찾아서 같이 반환합니다.
	"""
        dp = []
        for i in range(len(nums)):
            if (target - nums[i]) in nums[i+1:]:
                return [i, nums[i+1:].index(target - nums[i]) + i+1]

