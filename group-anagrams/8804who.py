class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        for string in strs:
            sorted_str = ''.join(sorted(string))
            dic[sorted_str].append(string)

        return list(dic.values())