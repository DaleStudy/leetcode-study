# 시간복잡도: O(N*AlogA) A: 0<= strs[i]의 길이 <= 100
# 공간복잡도: O(N)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for anagram in strs:
            key = str(sorted(anagram))
            groups.setdefault(key, []).append(anagram)

        return list(groups.values())
