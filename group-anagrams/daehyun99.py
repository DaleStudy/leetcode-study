from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c)-ord('a')] += 1

            groups[tuple(count)].append(s)
        return list(groups.values())

"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def decode(s, key, base):
            for c in s:
                key[ord(c) - base] += 1
            result = ""
            for k in key:
                result += ' ' + str(k)
            return result
        keys = {}
        base_key = [0 for i in range(26)]
        base = ord("a")

        for s in strs:
            key = decode(s, base_key.copy(), base)
            temp = keys.get(key, [])
            temp.append(s)
            keys[key] = temp
        results = []
        for val in keys.values():
            results.append(val)
        return results
"""
