"""
    풀이 :
        최초 시작 시 nums[left]가 nums[right]보다 작은 경우는 n만큼 rotate된 상태(원래 자신)
            같은 경우는 len(nums) == 1인 경우
        mid와 right의 값을 비교해서 mid의 값이 작다면 mid부터 right까지는 정렬되있으므로 좌측에 최솟값 존재
            -> right = mid - 1
        반대의 경우는 최솟값이 우측에 있으므로 left = mid + 1

    - left, mid, right을 적절히 할당할 수 있도록 수식 구현 잘할 것
    - mid가 최솟값일 경우에 대한 예외처리

    nums의 길이 : n

    TC : O(logN)
        반씩 나눠서 탐색하므로 log2N
    
    SC : O(1)
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        if nums[left] <= nums[right] :
            return nums[left]
        while (nums[right] < nums[left]):
            mid = (left + right) // 2
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] < nums[right] :
                right = mid - 1
            else :
                left = mid + 1
        return nums[left]
