class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_index = 0
        right_index = len(nums) -1

        while left_index <= right_index:
            mid_index = (left_index + right_index) // 2

            if nums[mid_index] == target:
                return mid_index
            
            # 왼쪽 절반 정렬 확인
            if (nums[left_index] <= nums[mid_index]):
                if (nums[left_index] <= target < nums[mid_index]):
                    right_index = mid_index -1 
                else:
                    left_index = mid_index + 1
            
            # 오른쪽 절반 정렬 확인
            else:
                if (nums[mid_index] < target <= nums[right_index]):
                    left_index = mid_index + 1 
                else:
                    right_index = mid_index -1 
            
        return -1
