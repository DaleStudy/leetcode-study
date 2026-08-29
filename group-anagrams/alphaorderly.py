"""
Time Complexity: O(n * k log k)
Space Complexity: O(n * k)

- Iterate through each word in the input list
- Use a dictionary to group anagrams by their sorted tuple of characters as the key
- For each word, sort its characters and use the resulting tuple as the dictionary key
- Append the word to the appropriate list in the dictionary
- Return a list of the grouped anagrams
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for word in strs:
            d[tuple(sorted(word))].append(word)

        return list(d.values())

"""
Time Complexity: O(n * k)
Space Complexity: O(n * k)

- Iterate through each word in the input list
- Use a dictionary to group anagrams; key is a tuple representing character counts
- For each word, build a character frequency tuple (instead of sorting)
- This tuple serves as a unique identifier for anagrams
- Append the word to the appropriate list in the dictionary
- Return a list of the grouped anagrams
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        def hash(s: str) -> Tuple[int, ...]:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            return tuple(count)

        for word in strs:
            d[hash(word)].append(word)

        return list(d.values())
