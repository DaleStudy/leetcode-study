class Solution:
    def findMin(self, nums: list[int]) -> int:
        """
        정렬된 리스트에서 n번 돌아간 상태에서 기존의 첫번째 값 (가장 작은)을 찾는 함수

        방법:
        Hint2의 Can you think of an algorithm which has O(logN) search complexity?
        에서 binary search!

        Args:
            nums (list[int]): n번 돌아간 정수 리스트

        Returns:
            int: 최초 정렬된 리스트의 첫번째 값
        """
        if nums[0] <= nums[-1]:
            return nums[0]
        start, end = 0, len(nums) - 1
        while start < end:
            if start == end:
                break
            mid = start + (end - start) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
        return nums[start]
