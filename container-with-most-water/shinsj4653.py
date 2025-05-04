"""
[문제풀이]
# Inputs
- height 높이의 정수 배열

# Outputs
- 담을 수 있는 최대 물의 양

# Constraints
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4

# Ideas
- 1. 완탐
결국 기둥 2개로 컨테이너 생성
하지만, n은 10^5 -> 2중 for문 불가능

2. DP ?
최대 물 양을 찾는 것이 문제 조건

특정 구간마다 최대 로 담을 수 있는 물의 양이 겹치는 걸 활용?
height = 1, 8, 6, 2, 5, 4, 8 3 7
dp[i][j]

dp[0][1] = 1
dp[1][2] = 6
dp[2][3] = 2
dp[3][4] = 2
dp[4][5] = 4
dp[5][6] = 4
dp[6][7] = 3
dp[7][8] = 3

dp[0][2] => 0 ~ 2 중 높이 가장 작은 -> 1 * (j - i)
dp[1][3] => 1 ~ 3 중 작은 2

=> 먼가 위 처럼 최소 높이 구하면서 점점 가로길이 늘려가는 식으로 풀면 될 것 같은데 이를 dp를 사용해서 구현하는 법을 모르곘음..

해설 참고
3. 투포인터


[회고]
dp, 이분탐색 도 아닌 것 같다라면, 투포인터 고려해보기
-> dp 로 단정지으니, 구간의 최솟값이나 물 양 중 어느 값을 저장해야하는지, 그리곶 저장한 값을 언제 어떻게 활용할건지..감이 안잡혀서 못 품

"""


class Solution:
    def maxArea(self, height: List[int]) -> int:

        ret = 0
        s, e = 0, len(height) - 1

        while s < e:
            area = (e - s) * min(height[s], height[e])
            ret = max(ret, area)

            if height[s] < height[e]:
                s += 1
            else:
                e -= 1

        return ret


