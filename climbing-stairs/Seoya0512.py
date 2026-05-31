'''
Approach: Dynamic Programming
- 혼자서 해결하려고 고민을 30분 이상 했으나 실패해서 알고달레 선생님의 블로그 도움을 받았습니다.
- 해당 문제를 통해 동적 계획,Dynamic Programming
- 더 적은 입력에 대한 답을 먼저 구해서 저장해놓고, 더 큰 입력에 대한 답을 구할 때 활용하는 방식에 대해 학습할 수 있었습니다!

Time Complexity: O(n)
- for loop이 n번 순회하며 각 값에 대한 연산 O(n) 발생
Space Complexity: O(n)
- nums 딕셔너리에 각 계단 수에 대한 경우의 수를 저장
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        nums = {1:1, 2:2}
        for i in range(3, n+1):
            nums[i] = nums[i-1] + nums[i-2]
        return nums[n]
