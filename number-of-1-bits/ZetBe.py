'''
문제: 정수 n이 주어졌을 때, n의 이진 표현에서 1의 개수를 반환하는 함수를 작성하세요.
풀이: 2의 거듭제곱 수들을 미리 계산해두고, n에서 큰 수부터 빼가며 1의 개수를 세는 방식으로 풀이
시간복잡도: O(log n)
    2의 거듭제곱 수들을 미리 계산하는데 O(log n)이 걸리고, n에서 큰 수부터 빼가며 1의 개수를 세는 데도 O(log n)이 걸리므로 전체 시간복잡도는 O(log n)이다.
공간복잡도: O(log n)
    2의 거듭제곱 수들을 저장하는 리스트를 사용하므로 전체 공간복잡도는 O(log n)이다.
사용한 자료구조: 리스트
'''


class Solution:
    def hammingWeight(self, n: int) -> int:
        b = []
        now = 1
        answ = 0
        for i in range(35):
            b.append(now)
            now *= 2

        num = n
        for i in range(34, -1, -1):
            if num >= b[i]:
                num -= b[i]
                answ += 1
        return answ
    

