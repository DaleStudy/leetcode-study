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
