"""
📚 11. Container With Most Water

📌 문제 요약
- 높이 배열이 주어졌을 때, 두 막대 사이에 담을 수 있는 물의 최대 넓이 구하기
- 넓이 = min(두 높이) × 거리

🎯 핵심 알고리즘
- 패턴: 투 포인터 (Two Pointer)
- 시간복잡도: O(n)
- 공간복잡도: O(1)

💡 핵심 아이디어
1. 양 끝에서 시작 (left = 0, right = n-1)
2. 현재 넓이 계산 후 최댓값 갱신
3. 더 작은 높이 쪽을 이동 → 더 큰 높이를 찾을 가능성!
"""

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            h = min(height[left], height[right])
            w = right - left
            max_area = max(max_area, h * w)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
