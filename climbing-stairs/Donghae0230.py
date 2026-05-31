# 1스텝 또는 2스텝으로 n개의 계단을 오르는 방법 경우의 수 구하기
# 1계단: 1
# 2계단: 2 , 1 + 1
# 3계단: 2 + 1, 1+1+1, 1+2
# 4계단: 2+2, 1+1+1+1, 2+1+1, 1+2+1, 1+1+2
#  -> 방법: step_n = step_(n-1) + step_(n-2)
# 시간 복잡도: O(n), while문 사용
# 공간 복잡도: O(n), 길이 n인 result 리스트 생성
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            result = [1, 2]
            i = 2
            while i < n:
                result.append(result[i-1] + result[i-2])
                i += 1
            return result[-1]
