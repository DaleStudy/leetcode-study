class Solution:
    def maxArea(self, height: List[int]) -> int:
            # 시작과 끝 선분을 포인터로 두고
            # 두 선분으로 만들 수 있는 넓이:
            # 너비 = right - left
            # 높이 = min(height[left], height[right])
            # 넓이 = 너비 * 높이의 최대 값을 구하는 문제
            # Time Complexity: O(n)
            # 두 포인터가 한 칸씩만 이동하며 서로 만날 때 루프 종료
            # Space Complexity: O(1)
            n = len(height)
            left = 0 # 왼쪽(시작) 포인터
            right = n - 1 # 오른쪽(끝) 포인터
            max_area = 0

            while left < right:
                # 현재 높이는 두 직선 중 낮은 쪽
                current_height = min(height[left], height[right])
                # 현재 너비는 오른쪽 점과 왼쪽 점의 차
                current_width = right - left
                # 넓이 = 높이 * 너비 
                current_area = current_height * current_width
                # 최대 넓이라면 업데이트
                max_area = max(max_area, current_area)
                # 포인터 이동 후 탐색
                # 둘 중 더 낮은 쪽의 포인터를 안으로 움직여서 넓이 계산 
                # 더 큰 넓이를 찾는 것이 목표, 포인터를 안으로 움직이면 너비는 무조건 감소
                # 높이라도 증가할 가능성이 있어야 하므로 기존 낮은 높이가 늘어날 가능성에 배팅
                # 둘이 같다면 오른쪽 이동(아무쪽이나 가능)
                if height[left] < height[right]:
                    left += 1
                else:
                    right -= 1
            return max_area
