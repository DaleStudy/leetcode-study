class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagram = defaultdict(list) 
        # 초기화: 키가 없으면 자동으로 list() 즉, []를 실행해서 값을 만듦

        for word in strs:
            sorted_word = ''.join(sorted(word))
            group_anagram[sorted_word].append(word)

        return list(group_anagram.values())
