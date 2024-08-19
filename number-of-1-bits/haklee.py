"""TC: O(log n), SC: O(log n)

n이 2배 커지면 bin(n)의 길이가 1 늘어나고, 이 bin(n) 값을
전부 순회하므로 O(log n).
bin(n)을 리스트로 바꿔서 sum을 했으므로 SC도 O(log n)이 된다.

하지만 n의 크기가 2^31 - 1 이하로 제한되어 있으므로
TC, SC 분석이 크게 의미있진 않음.
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum([i == "1" for i in bin(n)])
