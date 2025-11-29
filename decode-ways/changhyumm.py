class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        
        def decode(index):
            # 이미 계산했으면 바로 반환
            if index in memo:
                return memo[index]
            
            # 기저 사례
            ## 끝까지 왔으면 성공
            if index == len(s):
                return 1
            ## 0으로 시작하면 불가능
            if s[index] == '0':
                return 0
            
            # 재귀 계산
            ways = decode(index + 1)
            
            if index + 1 < len(s) and int(s[index:index+2]) <= 26:
                ways += decode(index + 2)
            
            # 메모이제이션
            memo[index] = ways
            return ways
        
        # 시간복잡도, 공간복잡도 O(n)

        return decode(0)
