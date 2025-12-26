import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 도착을 위해 실제로 움직여야 하는 칸은 아래로 (m - 1)칸, 오른쪽으로 (n - 1)칸
        # 총 (m + 1) + (n + 1)칸을 움직여야 하는데, 이만큼의 "빈 바구니"가 있다고 가정
        # 빈 바구니의 몇 번 박스에 오른쪽으로 가기/아래로 가기를 넣을 것인가? 의 문제
        # 조합을 통해 둘 중 아무거나를 바구니에 넣는 경우의 수를 구하면, 나머지 칸에 나머지 하나를 다 넣을 수 있다.
        # 따라서 math.comb(m + n - 2, n - 1)도 동일한 결과 반환
        return math.comb(m + n - 2, m - 1)
