class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Naive - 완전탐색
        n = len(height)
        
        """
        모든 조합을 계산한 후 최댓값 리턴
        Tc : O(n^2)
        Sc : O(1)
        
        ret = 0

        for i in range(n-1):
            for j in range(i+1, n):
                w = j - i
                h = min(height[i], height[j])
                ret = max(ret, w*h)
        return ret
        """

        # Better Solution
        """
        투 포인터를 활용한 방법
        포인터를 움직일 때는 더 작은 값을 가진 쪽이 한칸 움직여 그 높이를 높이는 방향 쪽으로 진행

        Tc : O(n)
        Sc : O(1)

        """
        left, right = 0, n-1
        ret = 0
        
        while left < right:
            w = right - left
            h = min(height[left], height[right])
            ret = max(ret, h*w)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return ret
            
        
