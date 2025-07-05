class Solution:
    def countBits(self, n: int) -> List[int]:
        # 시간복잡도 O(n), 공간복잡도 O(n)
        
        # 0으로 초기화
        answer = [0]*(n+1)

        for i in range(1,n+1):
            # i//2(마지막비트를제외한부분)의 1의 개수 + i의 마지막비트(홀수면 1, 짝수면 0)
            answer[i] = answer[i//2] + (i&1)

        return answer
