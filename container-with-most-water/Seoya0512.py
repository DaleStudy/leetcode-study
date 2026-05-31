'''
이중 For-loop을 사용하면 시간복잡도가 O(n^2)이 되므로 시간초과가 발생
리트코드의 Hint를 참고해 Two Pointer를 사용하는 방식으로 시도했습니다.

Time Complexity: O(n)
- While 루프를 사용해서 인덱스 i와 j가 만날 때까지 반복으로 진행하기에 O(n)

Space Complexity: O(1)
- height 값과, max_area 값 모두 상수 공간을 사용
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_area = 0

        while i < j:
            area = min(height[i], height[j]) * (j-i)
            max_area = max(area, max_area)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            
        return max_area

