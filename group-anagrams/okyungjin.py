'''
[복잡도]
n: strs의 길이, k: 각 문자열의 최대 길이

시간 복잡도: O(n * k log k)
공간 복잡도: O(n * k)
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map: dict[str, List[str]] = {}

        for s in strs:
            key = ''.join(sorted(s))

            if key in anagram_map:
                anagram_map[key].append(s)
            else:
                anagram_map[key] = [s]

        return list(anagram_map.values())
