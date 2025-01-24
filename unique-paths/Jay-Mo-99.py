        # 해석
        # grid는 행렬(matrix)처럼 격자의 형태이다.
        # 행이 m개라는 뜻은 좌표 상 (0,0), (1,0), ..., (m-1,0)까지 존재한다는 뜻이다.
        # 열이 n개라는 뜻은 좌표 상 (0,0), (0,1), ..., (0,n-1)까지 존재한다는 뜻이다.
        # 따라서 (0,0)에서 (m-1,n-1)까지의 모든 가능한 경로 수를 구해야 한다.
        #   - 아래로 m-1번 이동하고, 오른쪽으로 n-1번 이동해야 한다.
        #   - 총 이동 횟수는 m-1 + n-1 = m+n-2이다.
        #   - 총 이동 횟수 내부에서 아래로 m-1번  오른쪽으로 (n-1)번의 조합의 경우의 수를 구한다. 
        #   - 예를 들어, 아래로 3번 오른쪽으로 다섯번으로 만들수 있는 모든 경우의 수를 구한다 ^^^>>>>> : ^와 > 가능한 조합을 찾아준다.  
        # 공식: (m+n-2)! / (m-1)! / (n-1)!


        #Big O
        #- N: int m의 크기 
        #- K: int n의 크기

        #Time Complexity: O(M+K) 
        #- for i in range(1,m+1-1): m과 n의 크기의 합에 영향받아 계산 진행 -> O(N+K)

        #Space Complexity: O(1)
        #- up,down1,down2 - 변수와 변수를 업데이트하는 사칙연산은 상수로 여겨져 O(1), 
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        up = 1 #분자
        down1 = 1 #분모 1
        down2=1   #분모 2
        

        for i in range(1,m+n-1):
            up *= i
        for i in range(1,m):
            down1 *= i
        for i in range(1,n):
            down2 *= i

        return int(up/(down1*down2))

