class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 애너그램은 원래의 모든 글자를 정확히 한 번 사용하여 다른 단어나 구절의 글자를 재배열하여 형성된 단어나 구절입니다.
        return sorted(s) == sorted(t)

