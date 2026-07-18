# [문제 분석]
# nums: 오름차순 정렬, 정수 배열, 중복 없음
# 배열에서 가장 작은 수를 찾아 반환
# 조건: O(log n)으로 작성할 것

# [접근법]
# 정렬된 배열이 주어지고, 배열이 n번 회전한다. 추세가 꺾이는 부분을 찾아 탐색 범위를 좁힌다.
# 배열이 정렬되어 있다는 조건이 있으므로 이진 탐색을 통해 탐색 범위를 좁혀 log n으로 탐색이 가능하다.

# [복잡도]
# 시간 복잡도: O(log n), 이진 탐색을 하므로 log n
# 공간 복잡도: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:

        # 왼쪽/오른쪽 값의 인덱스 계산
        left = 0 
        right = len(nums) - 1

        while left < right:
            # 중간값 인덱스
            mid = (left + right) // 2

            # 중간값과 오른쪽 값을 비교해 추세가 꺾이는지 비교
            if nums[mid] > nums[right]:
                # 추세 안 꺾임, 시작점을 중간값 인덱스 바로 다음으로 옮긴다
                left = mid + 1
            else:
                # 추세 꺾임, 종료지점을 중간값 인덱스로 옮겨준다
                right = mid

        return nums[left]
