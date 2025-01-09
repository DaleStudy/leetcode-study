# Big-O 예측
# Time : O(n^2) 최악의 경우 wordDict의 개수의 제곱만큼
# Space : O(n^2) 최악의 경우 a에 wordDict의 개수의 제곱만큼

# 쉽게 접근한 풀이
# 맨 앞의 것을 처리할 수 있는 것을 다 고르기 (startswith)
# 그들을 했을 때의 결과를 가지고 다음 것으로 동일하게 반복 진행하기.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        a = [[s]]
        i = 1
        s_list = None
        duplicate_dict = {}
        while True:
            s_list = a[-1]
            a.append([])
            for s in s_list:
                for word in wordDict:
                    if s.startswith(word):
                        surplus_word = s[len(word):]
                        if surplus_word not in duplicate_dict:
                            a[-1].append(surplus_word)
                            duplicate_dict[surplus_word] = 1
            # a[-1] = list(set(a[-1]))
            if "" in a[-1]:
                return True
            if not a[-1]:
                return False
            i += 1

