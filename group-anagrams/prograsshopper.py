class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sol 1 -> Time Exceed
        from collections import defaultdict
        word_dict = defaultdict(list)

        for string in strs:
            exist = False
            for elem in word_dict.keys():
                if sorted(elem) == sorted(string):
                    word_dict[elem].append(string)
                    exist = True
                    break
            if not exist:
                word_dict[string] = [string, ]
        result = []
        for elem in word_dict.values():
            result.append(elem)
        return result

        # sol 2
        # Time Complexity O(mn)
        result = defaultdict(list)

        for string in strs:
            key = "".join(sorted(string))
            result[key].append(string)
        return list(result.values())
