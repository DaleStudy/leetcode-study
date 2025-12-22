'''
문제: 최장 증가 부분 수열
풀이: 이분 탐색을 활용하여 증가하는 수열을 유지하며 길이를 계산, 새로운 수가 기존 수열의 마지막 수보다 크면 추가, 그렇지 않으면 이분 탐색으로 적절한 위치를 찾아 교체
시간복잡도: O(n log n)
공간복잡도: O(n)
사용한 자료구조: 리스트
'''


from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        answer = [nums[0]]
        for i in range(1, len(nums)):
            if answer[-1] < nums[i]:
                answer.append(nums[i])
            else:
                now = bisect_left(answer, nums[i])
                answer[now] = nums[i]

        return len(answer)
        


