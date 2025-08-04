"""
주어진 정수 배열 nums에서 가장 긴 증가하는 부분 수열의 길이를 구하는 문제

동적 계획법, 이중 포문 풀이 - TC: O(n^2), SC: O(n)

dp[i]: nums[i]로 끝나는 가장 긴 증가 수열의 길이. 초기값은 모두 1 (자기 자신만 있을 때)

오름차순 부분 수열 -> 앞에 있는 수가 뒤에 있는 수보다 작아야 함.
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:  # 오름차순 조건 만족한다면
                    dp[i] = max(dp[i], dp[j] + 1)  # 현재와 nums[j] 뒤에 nums[i]를 붙인 수열 중 더 긴 길이 선택
        return max(dp)  # 가장 긴 증가 수열의 길이
    

"""
주어진 정수 배열 nums에서 가장 긴 증가하는 부분 수열의 길이를 구하는 문제

이분 탐색 풀이 - TC: O(n log n), SC: O(n)

# bisect란?
bisect는 Python의 표준 라이브러리로 정렬된 리스트에 이진 탐색으로 원소를 삽입할 위치를 찾는 모듈.

bisect_left(arr, x):
- x를 삽입할 가장 왼쪽 위치를 반환
= 정렬된 오름차순 배열 arr에서 x를 끼워 넣을 수 있는 가장 왼쪽 위치 (index) 찾아줌
- 같은 값이 있어도 그 앞에 끼워 넣음

bisect_right(arr, x):
- 오른쪽 경계 = 오름차순 정렬된 배열 arr에서, 값 x를 삽입할 가장 오른쪽 위치
- 같은 값이 있으면 그 뒤에 끼워 넣음

해당 문제는 Strictly Increasing 수열이므로 같은 숫자를 허용 x
-> 같은 값이 들어오면 기존 값을 대체해야지, 그 뒤에 추가하면 안되므로 bisect_left 사용한다.
"""
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = []  # 각 길이별 증가 수열의 마지막 값(가장 작은 값)을 저장
        for num in nums:
            idx = bisect.bisect_left(tail, num)
            if idx == len(tail):  # 반환된 idx가 tail의 끝 부분이라면 현재 수열 끝에 추가될 수 있다는 뜻, 즉 num이 tail 안의 모든 값보다 큼
                tail.append(num)  # 수열 길이 늘림
            else:
                tail[idx] = num  # 더 작은 값으로 대체
        return len(tail)
