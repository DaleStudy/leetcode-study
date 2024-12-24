class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Intuition:
            비트를 역순으로 순회한다.
            answer에는 최대값(2^31)부터 최소값(2^0)으로 감소하는
            방식으로 업데이트한다.

        Time Complexity:
            O(N):
                n을 1번 순회하며 답을 찾으므로,
                O(N)의 시간복잡도가 소요된다.

        Space Complexity:
            O(1):
                answer에 값을 업데이트 하므로, 상수의
                공간복잡도가 소요된다.

        Key takeaway:
            숫자를 binary string으로 만드는 bin() 메소드를
            알게 되었다.
        """
        answer = 0
        for i, bit in enumerate(bin(n)[2:][::-1]):
            answer += int(bit) * 2 ** (31 - i)
        return answer
