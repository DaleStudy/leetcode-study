'''
문제: 최대 부분 배열의 합을 구하는 문제
풀이: 
    1. 배열의 모든 수가 음수인 경우, 가장 큰 수를 반환
    2. 배열의 처음부터 양수가 나올 때까지 인덱스를 이동
    3. 양수가 나온 이후부터는 현재 합이 양수인 동안은 계속 더하고, 음수가 되면 다시 양수를 찾음
    4. 매 단계마다 최대 합을 갱신
시간복잡도: O(n)
    배열을 한 번 순회하며 최대 부분 배열의 합을 계산하므로 전체 시간복잡도는 O(n)이다.
공간복잡도: O(1)
    추가적인 공간을 사용하지 않으므로 전체 공간복잡도는 O(1)이다.
'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        answ = 0
        if max(nums) <= 0:
            return max(nums)
        i = 0
        while nums[i] < 0:
            i += 1
        now = 0
        while i < n:
            if now > 0 and i < n:
                now += nums[i]
                i += 1
            else:
                while now <= 0 and i < n:
                    now = nums[i]
                    i += 1
            answ = max(answ, now)

        return answ

