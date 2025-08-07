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
        result = set()
        nums.sort()

        for i in range(len(nums)):            
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return list(result)
