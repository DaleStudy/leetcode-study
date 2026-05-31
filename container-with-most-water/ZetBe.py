'''
문제: 컨테이너 최대 물 담기
풀이: 양쪽 끝에서 시작하여 더 작은 쪽의 포인터를 이동시키며 최대 넓이를 계산
시간복잡도: O(n)
공간복잡도: O(1)
사용한 자료구조: 투 포인터
'''


class Solution:
    def maxArea(self, height: List[int]) -> int:
        r, l = len(height)-1, 0
        answer = (r-l)*(min(height[r], height[l]))
        while r > l:
            answer = max(answer, (r-l)*(min(height[r], height[l])))
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
        return answer
    


