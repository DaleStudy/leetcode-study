"""
시간복잡도: O(n)
공간복잡도: O(1)

- 만약 현재 숫자가 음수라면, 양수 최대값(pos)과 음수 최소값(neg)을 서로 교환한다.
  - 이유: 음수 * 음수 = 양수이므로, 음수를 만나면 최대값/최소값 후보가 바뀔 수 있다.
- pos와 neg를 nums의 첫 번째 값으로 초기화한다.
    - pos: 현재까지의 곱셈 최대값
    - neg: 현재까지의 곱셈 최소값
    - pos, neg로 이름 붙힌 이유는 nums에 음수가 있을 때 각각 양수와 음수가 될 수 있기 때문이다.
- ans를 nums의 첫 번째 값으로 초기화한다.
  - ans: 현재까지의 최대 곱셈 결과
- nums의 두 번째 원소부터 끝까지 pos와 neg를 갱신한다.
  - pos는 현재 숫자와 pos*현재 숫자 중 큰 값
  - neg는 현재 숫자와 neg*현재 숫자 중 작은 값
- ans를 pos와 비교하여 최대값으로 갱신한다.
- 반복이 끝나면 ans를 반환한다.
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pos = neg = ans = nums[0]
        N = len(nums)

        for i in range(1, N):
            if nums[i] < 0:
                neg, pos = pos, neg

            pos = max(nums[i], nums[i] * pos)
            neg = min(nums[i], nums[i] * neg)

            ans = max(ans, pos)

        return ans
