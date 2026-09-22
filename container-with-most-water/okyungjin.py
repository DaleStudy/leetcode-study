"""
문제:
    - 담을 수 있는 최대 물의 양(최대 면적)을 구한다.
    - i번째 수직선은 height[i] 높이를 가진다.
    - x축과 선택한 두 수직선이 담는 물의 양이 최대가 되도록한다.

접근법:
    1. 좌측, 우측 포인터 `left`, `right`를 선언하여 기둥을 움직인다.
    2. 좌우 기둥의 높이를 비교해서 높이가 낮은 기둥의 x좌표를 한칸 안쪽으로 움직인다.
        포인터를 바깥쪽에서 안쪽으로 이동할 때 가로의 길이가 줄어든다.
        따라서 낮은 기둥을 버려야 `max_area`를 갱신할 수 있는 가능성이 생긴다.
    3. 두 포인터가 만나거나 좌우가 역전되면 탐색을 종료한다.

복잡도:
    시간 복잡도: O(n)
    공간 복잡도: O(1)

실패했던 접근법:
    1. 2중 for: TLE
    2. 가장 높은 기둥을 고정축으로 하고 나머지 하나의 기둥을 찾도록: [1,2,1] 입력에서 실패
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        max_area = 0

        while left < right:
            if height[left] < height[right]:
                area = height[left] * (right - left)
                left += 1
            else:
                area = height[right] * (right - left)
                right -= 1
            
            if area > max_area:
                max_area = area

        return max_area
