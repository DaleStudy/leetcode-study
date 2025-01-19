from math import comb 

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # mathematic way
        # 중학교 때 배운 최단거리 조합으로 구하기 문제
        # 문제 자체가 오른쪽, 아래밖에 못가기에 최단거리가 될 수 밖에 없음

        """
        TC : O(max(m, n))
        SC : O(1)
        """

        return comb(m+n-2, m-1)
        
