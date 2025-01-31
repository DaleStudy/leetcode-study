'''
TC : O(logn)
	비트연산이 n을 2로 나누는 것과 같으므로 로그 시간복잡도를 갖는다
SC : O(1)
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n != 0:
            if n & 1 == 1:
                cnt += 1
            n >>= 1
        return cnt
