class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count = 0
        
        # 중심(left, right)에서 시작해서 양옆으로 퍼지며 팰린드롬 찾기
        def expand(left: int, right: int):
            # 인덱스 범위를 벗어나지 않고 양쪽 문자가 같으면 팰린드롬 발견
            while left >= 0 and right < len(s) and s[left] == s[right]:
                self.count += 1  # 미츠케타!!!
                left -= 1        # 왼쪽으로 한 칸 확장
                right += 1       # 오른쪽으로 한 칸 확장

        for i in range(len(s)):
            # 홀수 길이 (중심이 i 하나) -> ex."aba"의 'b'
            expand(i, i)
            
            # 짝수 길이 (중심이 i와 i+1 사이) -> ex."abba"의 'bb'
            expand(i, i + 1)
            
        return self.count
 