class Solution:
    """
    [3, 4, 5, 1, 2] -> [2, 3, 4, 5, 1] -> [1, 2, 3, 4, 5]
    1. 큐의 rotate 이용 -> 회전 전의 첫 요소가 회전 후의 요소 비교
    시간복잡도: O(n^2)
    - while 루프가 최대 n번 반복 가능
    - deque.rotate(±1) 연산이 O(n) 시간 소요
    - 따라서 전체는 O(n) * O(n) = O(n^2)
    공간복잡도: O(n)
    - 입력 배열을 deque로 변환 → 추가로 O(n) 공간 사용
    - 나머지는 상수 공간
    """
    """
    def findMin(self, nums: List[int]) -> int:
        nums = deque(nums)
        if len(nums) == 1:
            return nums[0]

        while True:
            cur = nums[0]
            nums.rotate(1)
            if cur < nums[0]:
                nums.rotate(-1)
                return nums[0]
    """

    """
    2. 요소별로 이전 값과 현재 값을 비교하여 작은 값이 나오면 그 값이 첫번쨰 요소, 즉 가장 작은 요소가 됨
    시간복잡도: O(n)
    - 최악의 경우 배열 전체를 한 번 순회해야 함
    - n = len(nums)
    공간복잡도: O(1)
    - 추가로 사용하는 변수는 i와 몇 개의 상수형 변수뿐
    """
    """
    def findMin(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                return nums[i]
        return nums[0]
    """
    """
    3. 이분탐색을 사용하는 방법
    """
    def findMin(self, nums: List[int]) -> int:
        start, end = 1, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[0] < nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return nums[0]
