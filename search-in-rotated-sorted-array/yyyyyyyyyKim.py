class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # 회전된 정렬 배열에서 이진탐색(시간복잡도 O(log n))
        left = 0
        right = len(nums)-1
        
        while left <= right:
            mid = (left+right)//2

            if nums[mid] == target:
                return mid
        
            # 왼쪽 정렬
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            # 오른쪽 정렬
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        # 탐색 후에도 타켓을 발견하지 못했다면 -1 반환
        return -1
