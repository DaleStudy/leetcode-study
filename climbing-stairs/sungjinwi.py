'''
	- 달레스터디 풀이 참고함
    풀이 : 
		n번째 계단을 오르기 위해서는 n-1 또는 n-2에 있다가 올라오는 수 밖에 없으므로 f(n-1) + f(n-2)의 값
        dp 배열로 풀 수도 있지만 두 개의 변수에 업데이트 하는 식으로 풀이
        
    TC :
		for문으로 인해 O(N)
        
    SC :
		O(1)
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3 :
            return (n)
        prv, cur = 1, 2
        for _ in range(3, n + 1) :
            prv, cur = cur, prv + cur
        return (cur)
