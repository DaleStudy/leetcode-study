class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 선형 탐색(linear scan) 버전

        # 시간 복잡도: O(n)
        # - 배열 전체를 뒤에서 앞으로 한 칸씩 순회하면서
        #   "회전이 끊기는 지점"을 찾는다.
        # - 최악의 경우 n-1번 비교.

        # 공간 복잡도: O(1)
        # - 추가 변수만 사용.

        # 배열 길이가 1개면 그 값 자체가 최솟값
        min_num = 0
        if len(nums) == 1:
            return nums[0]

        # 뒤에서 앞으로 탐색하면서
        # nums[i] < nums[i-1] 지점(회전이 일어난 지점)을 찾는다.
        # 해당 지점의 nums[i]가 최솟값
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < nums[i - 1]:
                min_num = nums[i]
                break

        return min_num

    def findMinBinarySearch(self, nums: List[int]) -> int:
        # 이진 탐색(binary search) 버전

        # 시간 복잡도: O(log n)
        # - 정렬된 배열이 한 번 회전(rotated)된 형태를 이용해
        #   절반씩 탐색 범위를 줄인다.
        # - mid 기준 왼쪽/오른쪽 어느 쪽이 정렬 상태인지에 따라 탐색 방향 결정

        # 공간 복잡도: O(1)
        # - 포인터(l, h, mid)만 사용

        # l은 1부터 시작하는데,
        # mid-1 비교를 안전하게 하기 위함이다.
        l, h = 1, len(nums) - 1

        while l <= h:
            mid = (l + h) // 2

            # mid가 최솟값이 되는 전형적인 조건:
            # mid 바로 이전 요소가 mid보다 크면 회전 지점
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            # nums[0] < nums[mid] -> 배열 시작점부터 mid까지는 정렬된 상태
            # → 회전 지점은 오른쪽에 있음 -> l을 오른쪽으로 이동
            if nums[0] < nums[mid]:
                l = mid + 1
            else:
                # 그 외의 경우 회전 지점은 왼쪽 구간에 존재
                h = mid - 1

        # 회전이 아예 없는 경우(완전 정렬 상태)
        return nums[0]

    # def findMin(self, nums: List[int]) -> int:
    #     # 파이썬의 내장함수인 min을 이용해도 문제 풀이 가능
    #     # https://wiki.python.org/moin/TimeComplexity애 의하면 min 함수도 O(n)임
    #     return min(nums)


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
