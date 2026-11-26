"""
1비트의 개수 만큼 반복, 최악은 모든 비트가 1
TC : O(log N) 
SC: O(1)
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            # Kernighan's Trick: 가장 오른쪽 1비트를 제거
            n &= n - 1
            ans += 1
        return ans
