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


# 7기 풀이
# 시간 복잡도: O(n)
# - two point 알고리즘을 이용하기 때문에 heights 변수의 길이인 n에 시간복잡도가 정해짐
# 공간 복잡도: O(1)
# - 몇 개의 변수만 사용함
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 양 끝 포인터 지정
        start, end = 0, len(height) - 1

        # max_area는 현재 포인터들을 이용했을 때의 넓이 계산
        # 이때 높이는 작은 쪽으로 선택하여 계산해야 함
        max_area = min(height[start], height[end]) * (end - start)

        # start가 end보다 작을 때 루프 돌기
        while start < end:
            # 문제의 핵심 아이디어는, 높이가 큰 쪽을 움직이면 얻을 수 있는 최선이 현재보다 클 수 없다.
            # 이는, start의 높이와 end의 높이 중 큰 쪽의 포인터를 고정하여 움직여야 한다는 것
            # (물의 높이는 작은 쪽에 의해 정해지는데, 큰 쪽 포인터를 움직이면 x 길이만 짧아지게 되어 오히려 넓이이 줄어듦)
            if height[start] < height[end]:
                # start 쪽의 높이가 낮으면 start를 움직임
                start += 1
            else:
                # end 쪽의 높이가 낮으면 end를 움직임
                end -= 1

            # 포인터를 옮기고 난 후의 넓이를 계산하여, 기존의 max_area와 비교하여 큰 쪽으로 업데이트
            curr_area = min(height[start], height[end]) * (end - start)
            max_area = max(max_area, curr_area)
        
        return max_area
