class Solution:
    def hammingWeight(self, n: int) -> int:
        # n을 2진수로 변환한 문자열에서 1의 갯수를 반환 
        return len(list(filter(lambda x: x == "1", bin(n)[2:])))
