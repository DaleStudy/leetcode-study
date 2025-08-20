from collections import defaultdict

class Solution:
    """
    1. 정렬된 값이 딕셔너리에 있으면 리스트 형식으로 삽입
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_strs = defaultdict(list)
        
        for word in strs:
            dict_strs[str(sorted(word))].append(word)
        return list(dict_strs.values())
