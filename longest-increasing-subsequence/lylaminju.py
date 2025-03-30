'''
Dynamic programming 활용

시간복잡도: O(n^2)  - 두 개의 중첩된 반복문이 nums 배열을 탐색함
공간복잡도: O(n)    - dp 배열에 숫자 개수(n)만큼 공간이 필요함
'''

def lengthOfLIS_n2(nums):
    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)  # 이전 LIS 길이에 1 추가

    return max(dp)  # dp 배열의 최대값이 최장 길이


'''
이진탐색 활용

시간복잡도: O(n log n) - 각 숫자에 대해 이진 탐색(bisect_left)을 수행함
공간복잡도: O(n)       - sub 리스트에 최대 n개의 숫자가 저장될 수 있음
'''

from bisect import bisect_left

def lengthOfLIS_nlogn(nums):
    sub = []  # 현재까지 찾은 LIS의 숫자들을 저장

    for num in nums:
        pos = bisect_left(sub, num)  # 삽입 위치를 이진 탐색으로 찾음

        if pos == len(sub):
            sub.append(num)  # 삽입 위치가 sub의 범위 밖이면 숫자 추가
        else:
            sub[pos] = num  # 삽입 위치가 범위 안이면 해당 위치의 숫자를 현재 숫자로 교체

    return len(sub)
