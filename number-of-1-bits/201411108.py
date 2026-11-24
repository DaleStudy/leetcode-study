# TC: O(log n), n을 계속 2로 나누며 순회
# SC: O(log n), 재귀 호출 스택에 호출 횟수만큼 쌓임
class Solution:
    def hammingWeight(self, n: int) -> int:
        def divideBy2(m: int, acc: int) -> int:
            if m <= 1:
                return acc + 1
            
            if (m % 2 != 0):
                acc += 1
            return divideBy2(m // 2, acc)
        
        result = divideBy2(n, 0)

        return result

