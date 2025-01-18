"""
	풀이 :
		left, right 커서를 양 끝에 놓고 조건에 따라 반대편으로 이동시키며 물 양 비교
		둘 중 더 높은 높이를 이동시키면 무조건 물의 양이 줄어들기 때문에 더 낮거나 같은 커서를 이동시키며 업데이트
		둘이 만나면 비교 종료


	len(height) : N
	TC : O(N)
		l, r의 이동이 전체 height 개수만큼 일어나므로
	SC : O(1)
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0
        while (l != r) :
            cur_area = (r - l) * min(height[l], height[r])
            max_area =  max(cur_area, max_area)
            if (height[l] >= height[r]) :
                r -= 1
            else :
                l += 1
        return max_area
