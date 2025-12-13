'''
Docstring for find-minimum-in-rotated-sorted-array.ZetBe
문제: 회전된 정렬 배열에서 최솟값을 찾으시오.
풀이: 이진 탐색을 사용하여 회전된 배열에서 최솟값을 효율적으로 찾습니다.
시간 복잡도: O(log n), n은 배열의 길이입니다. 이진 탐색을 사용하여 절반씩 탐색 범위를 줄이므로 전체 시간 복잡도는 O(log n)입니다.
공간 복잡도: O(1), 추가적인 공간을 사용하지 않으므로 공간 복잡도는 O(1)입니다.
사용한 자료구조: 배열
추가로, while문 내부에서 무조건 리턴하기 떄문에, while문 이후 도달하는 경우는 없다.
'''


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if nums[0] <= nums[n-1]:
            return nums[0]

        r, l = 0, n-1

        while r < l:
            now = (r+l)//2
            if now < n-1 and nums[now] > nums[now+1]:
                return nums[now+1]
            
            if now < n-1 and nums[0] > nums[now] <= nums[now+1]:
                l = now
            elif now < n-1 and nums[0] <= nums[now] <= nums[now+1]:
                r = now
            

