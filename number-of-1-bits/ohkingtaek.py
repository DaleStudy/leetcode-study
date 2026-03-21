from collections import Counter

class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        - 시간복잡도: O(n)
        - 공간복잡도: O(n)
        문자열을 이진수로 변환하고, 1의 개수를 세기
        """
        return Counter(bin(n)[2:])["1"]