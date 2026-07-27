class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 두 점의 거리가 길어야 하고, 높은 막대기들끼리 있어야 많은 물을 채울 수 있음.
        # 양쪽의 점부터 시작해서 더 줄여볼지 말지를 판단 해 볼 수 있을 것 같음.

        def caculate_water_container(left, right):
            return (right - left) * min(height[left], height[right])

        left = 0
        right = len(height) - 1
        max_water = 0
      
        while left <= right:
            max_water = max(max_water, caculate_water_container(left, right))
            if height[left] > height[right] : 
                right -= 1
            else : 
                left += 1
              
        return max_water
      
