class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 시간복잡도 O(n2)으로 타임아웃
        # max_amount = 0
        # for i in range(len(height) - 1):
        #     for j in range(i + 1, len(height)):
        #         amount = (j-i) * min(height[i], height[j])
        #         max_amount = max(amount, max_amount)
        # return max_amount
        
        # 투포인터 활용
        # 시간복잡도 O(n)
        max_amount = 0
        left = 0
        right = len(height) - 1
        while left < right:
            amount = (right - left) * min(height[left], height[right])
            max_amount = max(amount, max_amount)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_amount
