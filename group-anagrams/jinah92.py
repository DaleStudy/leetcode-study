# O(N * NlogN) times, O(N) spaces
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = {}
        result = []

        for str in strs: # N 시간 소요
            str_count = {}
            for s in str:
                if not s in str_count:
                    str_count[s] = 1
                else:
                    str_count[s] += 1
            anagrams_keys = []
            for key, val in sorted(str_count.items()): # 최대 N개의 dict items를 배열하므로 NlogN 시간 소요
                anagrams_keys.append(tuple([key, val]))
        
            anagrams_key = tuple(anagrams_keys)
            if tuple(anagrams_keys) not in anagrams_dict:
                anagrams_dict[tuple(anagrams_keys)] = []
            anagrams_dict[tuple(anagrams_keys)].append(str)


        return list(anagrams_dict.values())
