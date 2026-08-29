from functools import cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        @cache
        def finding(start):
            # 문자열 끝까지 단어들로 나누는 데 성공한 경우
            if start == len(s):
                return True

            # start부터 시작하는 모든 부분 문자열을 확인한다.
            for end in range(start + 1, len(s) + 1):
                current_word = s[start:end]

                # 현재 단어가 사전에 있고,
                # 나머지 문자열도 나눌 수 있다면 바로 종료한다.
                if current_word in word_set and finding(end):
                    return True

            # 어떤 방식으로도 나눌 수 없는 경우
            return False

        return finding(0)
