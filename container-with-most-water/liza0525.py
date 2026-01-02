# 시간 복잡도: O(n)
# - two point 알고리즘을 적용했기 때문에, height의 길이 n만큼의 시간복잡도 사용
# 공간 복잡도: O(1)
# - 입력 리스트 외에 상수 개수의 변수만 사용

class Solution:
    # x의 길이를 변화 시킬 때 높이를 고려하며 변화 시킨다.
    # 이 때 start 또는 end를 옮기는 기준은 각 포인트에서의 높이 중 작은 것을 옮긴다.
    # 왜냐하면, 해당 문제에서 높이를 결정하는 것은 높이가 작은 쪽이며,
    # 높이가 높은 것을 옮겨봤자 가로 길이만 짧아져 오히려 넓이는 축소가 되기 때문이다.
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        result_area = (end - start) * min(height[start], height[end])

        while start < end:
            if height[start] < height[end]:
                # start 쪽의 높이가 낮을 땐 start를 옮김
                start += 1
            else:
                # end 쪽의 높이가 낮을 땐 end를 옮김(같을 때는 뭘 옮겨도 상관 없음)
                end -= 1

            # 옮긴 후의 넒이가, 지금까지 계산한 넓이보다 넓어진 것인지 확인하여 더 큰수를
            # result_area에 저장함
            result_area = max(
                (end - start) * min(height[start], height[end]),
                result_area
            )

        return result_area
