class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # 투포인터(two pointer) : 시간복잡도 O(n)
        left, right = 0, len(height)-1
        answer = 0

        while left < right:
            width = right - left    # 인덱스 차이가 두 벽 사이의 거리(너비)
            h = min(height[left], height[right])    # 더 낮은 벽을 기준으로 물을 채울 수 있음(높이)

            answer = max(answer, width * h) # 최대 넓이 업데이트

            # 포인터 이동(더 낮은 값을 가진 포인터를 이동)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return answer
