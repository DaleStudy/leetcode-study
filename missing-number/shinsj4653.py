"""
[문제풀이]
# Inputs
nums -> n개의 중복되지 않는 숫자들 (0 ~ n)

# Outputs
유일하게 0 ~ n 범위에 포함되어 있지 않은 수

# Constraints
n == nums.length
1 <= n <= 10^4
0 <= nums[i] <= n
All the numbers of nums are unique.


# Ideas

O(1) SC, O(n) TC로 할 수 있을까?
-> 처음엔 당연히 사전 쓰면 되겠지했지만, O(1) SC가 안됨

정렬도 nlogn..

길이 : n
0부터 n 까지 합 =>
n = 3

0 1 2 3 -> 6
sum(nums) -> 4
남은 수 : 2

[회고]
이게 맞네
1부터 n 까지 합 공식 -> (n * (n + 1)) // 2

"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)

        total_s = 0

        for i in range(n + 1):
            total_s += i

        return total_s - s

