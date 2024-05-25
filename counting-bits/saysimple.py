class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = []

        for i in range(n+1):
            b = bin(i)
            answer.append(int(b.count("1")))

        return answer
