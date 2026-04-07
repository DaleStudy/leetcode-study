class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        1.문제: 가장 많은 양의 물을 저장할 수 있는 max value return
        2.조건
        - n: 높이를 의미, 최소 = 5, 최대 = 10^5
        - 원소값 최소 = 0, 최대 = 10^4
        3.풀이
        - 높이는 height[i], height[j] 중에 작은 값, 가로는 abs(i-j)
        - output = 높이 x 가로
        -> 2중 loop 는 O(n^2) 로 TLE 발생.
        -> two pointer 로 O(n) 으로 해결!
        '''

        n = len(height)
        maxArea = 0

        left = 0
        right = n-1

        while left < right:
            curArea = abs(right-left) * min(height[left], height[right])
            maxArea = max(curArea, maxArea)
            
            #height 이 낮은쪽 pointer update
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maxArea
        