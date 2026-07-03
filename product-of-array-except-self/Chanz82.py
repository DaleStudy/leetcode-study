class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # 공간 복잡도 : 2개의 list를 사용하므로 O(2n)=O(n)
        # 시간 복잡도 : nums를 세번 순회 o(n)
        n = len(nums)
        left = [1] * n
        right = [1] * n

        for idx in range(1, n):
            left[idx] = left[idx-1] * nums[idx-1]
        
        for idx in range(n-2, -1, -1):
            right[idx] = right[idx+1] * nums[idx+1]
        
        return [left[i] * right[i] for i in range(n)]
