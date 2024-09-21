# 시간복잡도: O(N)
# 공간복잡도: O(N)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        answer = 0

        while l < r:

            if height[l] < height[r]:
                answer = max(answer, (r - l) * height[l])
                l += 1
            else:
                answer = max(answer, (r - l) * height[r])
                r -= 1

        return answer
