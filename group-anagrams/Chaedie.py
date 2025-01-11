"""
Solution: 
    1) hash map 에 sorted_word를 키로, 해당 sorted_word 에 해당하는 요소들을 밸류로 넣습니다.
Time: O(n^2 logn)= O(n) * O(nlogn)
Space: O(n)
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_words = defaultdict(list)
        # dict = {sorted_word: [word, word]}

        for i in range(len(strs)):
            word = strs[i]
            sorted_word = "".join(sorted(word))
            anagram_words[sorted_word].append(word)

        result = []
        for arr in anagram_words.values():
            result.append(arr)
        return result
