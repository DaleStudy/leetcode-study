""" 
Constraints:
1. 1 <= strs.length <= 10^4
2. 0 <= strs[i].length <= 100
3. strs[i] consists of lowercase English letters.

Time Complexity: O(N * K * log K)
- N은 입력 문자열의 개수 (strs의 길이)
- K는 가장 긴 문자열의 길이
- 각 문자열을 정렬하는데 K * log K가 필요하고
- 이걸 N개의 문자열에 대해 수행

Space Complexity: O(N * K)
- N개의 문자열을 저장해야 함
- 각 문자열의 길이는 최대 K
- anagram_dict에 모든 문자열을 저장하기 때문
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        
        for s in strs:
            sorted_str = ''.join(sorted(s))
            
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str].append(s)
            else:
                anagram_dict[sorted_str] = [s]
        
        return list(anagram_dict.values())

