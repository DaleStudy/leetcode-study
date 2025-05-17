class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        시간복잡도: O(log n) - 이진 탐색
        공간복잡도: O(1) - 추가 메모리 없음
        """
        
        # 이진탐색
        left = 0
        right = len(nums) - 1

        while left < right:
            # 중간 인덱스
            mid = (left+right)//2

            # 최소값이 오른쪽에 있음
            if nums[mid] > nums[right]:
                left = mid + 1
            # 최소값이 왼쪽(중간포함)에 있음
            else:
                right = mid

        # 최종 최소값
        return nums[left]
