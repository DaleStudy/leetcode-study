'''
주어진 문자열 s를 공백으로 구분된 단어 시퀀스로 분할할 수 있는지 확인하는 문제임 
이때 모든 단어는 주어진 사전(wordDict)에 포함되어야 함

Example 1.의 예를 들면
  dp = [True,   False,  False,  False,  False,  False,  False,  False,  False]
인덱스:    0        1       2       3       4       5       6       7       8
의미:     ""       "l"    "le"   "lee"   "leet" "leetc" "leetco" "leetcod" "leetcode"
가능한 단어 길이:   l=1~4    l=1~4   l=1~4    l=4    l=1~4   l=1~4   l=1~4    l=4        

dp[i]가 True가 되는 조건:
dp[i-l]이 True이고, s[i-l:i]가 사전에 있는 단어일 때
예시에서 i=4와 i=8에서 조건이 충족되어 True로 변경됨

'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)  # 단어 검색을 빠르게 하기 위해 집합으로 변환
        if not word_set:          # 사전이 비어있으면 항상 False
            return False
        
        max_len = max(len(word) for word in word_set)  # 사전에서 가장 긴 단어의 길이 구분
        dp = [False] * (len(s) + 1)  # dp[i]는 문자열 s의 첫 i글자가 분할 가능한지 여부를 저장
        dp[0] = True  # 빈 문자열은 항상 분할 가능하므로 True
        
        for i in range(1, len(s) + 1):  # 문자열의 모든 위치를 순회함
            for l in range(1, max_len + 1):   # 단어 길이를 1부터 max_len까지 확인함
                if i < l:  # 현재 위치보다 단어 길이가 길면 패스
                    break
                if dp[i - l] and s[i-l:i] in word_set:  # 이전 위치가 True이고, 현재 부분 문자열이 사전에 있으면 True로 표시함
                    dp[i] = True
                    break  # 하나라도 성공하면 더 확인할 필요 없음
        
        return dp[-1]  # 최종 결과 반환
