# NOTE: 문제 위치를 잘못 잡음 4주차 find-minimum-in-rotated-sorted-array로 옮겨감
# 삭제는 추후에(이유: github 리뷰 시 diff가 생겨 리뷰가 불편해질 수 있음)
# 7기 풀이
# 시간 복잡도: O(log n)
#  - binary search를 이용했기 때문에 최악의 경우는 log n
# 공간 복잡도: O(1)
#  - 몇 가지 변수만 사용됨
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 양 끝을 먼저 잡아준다
        left, right = 0, len(nums) - 1

        # left보다 right가 클 때 계속 루프를 돈다
        # 이는 left와 right가 같아질 때까지 돈다는 말과 동일하다
        while left < right:
            # 중간 index 계산
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # 중간 index의 값이 오른쪽 index의 값보다 크다는 것은
                # 최소 값이 mid 기준 오른쪽 구역에 존재하기 때문에 left을 mid쪽으로 움직인다.
                # mid의 값 자체는 최소값이 될 수 없기 때문에 left는 이보다 한 칸 옆으로 움직여야 함
                left = mid + 1
            else:
                # 중간 index의 값이 오른쪽 index의 값보다 작다는 것은
                # 최소 값이 mid 기준 왼쪽 구역에 존재하기 때문에 right를 mid쪽으로 움직인다.
                # mid의 값 자체는 최소값이 될 수 있기 때문에 right는 mid 값을 할당한다.
                right = mid

        # left와 right가 같아질 때(최소값을 찾았을 때) 루프 탈출을 하기 때문에
        # nums[left] 또는 nums[right]를 반환 
        return nums[left]


# 7기 풀이
# 시간 복잡도: O(log n)
# - binary search를 하므로 nums의 길이(n)의 로그 값 만큼의 시간 소요
# 공간 복잡도: O(1)
# - 변수 몇 개만 사용
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # 양 끝을 left, right로 설정

        while left <= right:
            mid = (left + right) // 2  # 중간 값 설정

            if target == nums[mid]:
                # 중간 값이 곧 target값이면 중간 index를 return
                return mid
            elif nums[left] <= nums[mid]:
                # left ~ mid 사이가 정렬이 되어 있다면,
                # (비고: 문제 조건 상, sorted list에서 rotate한 상황이므로
                # left와 mid만 비교해도 내부는 sorted 되어 있음
                # 이는 right ~ mid 비교 때와 동일함)
                if nums[left] <= target < nums[mid]:
                    # target이 오름차순이 되어 있는 구간에 있는지 확인
                    # 맞다면 right를 변경
                    right = mid - 1
                else:
                    # 오름차순 쪽이 아닌 곳에 있다면 rotate되어 순서가 뒤틀린 쪽에 있다는 의미라
                    # left를 변경
                    left = mid + 1
            elif nums[mid] <= nums[right]:
                # mid ~ right 사이가 정렬이 되어 있다면,
                # 마찬가지로 오름차순 구간에 target이 존재하는지 아닌지를 판별하여
                # left와 right를 조절한다
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        # while문을 모두 돌았음에도 return이 안되었다는 것은
        # target을 찾지 못했다는 의미이므로 문제 조건에 따라 -1 리턴
        return -1
