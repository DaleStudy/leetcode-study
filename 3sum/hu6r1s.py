class Solution:
    """
        1. 3 way for문으로 돌아가면서 0인 합을 찾는 방법
            - O(n^3)으로 시간초과
        2. 투포인터
            - 정렬 후 투포인터를 이용하여 중복 제거와 최적화를 동시에 수행
            - O(n^2)
        공간 복잡도는 둘다 O(1)
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result
