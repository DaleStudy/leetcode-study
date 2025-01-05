from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Naive Solution : Sort string

        # 각 단어마다 모두 정렬을 한 뒤 해당 값을 hash로 사용하여 딕셔너리에 추가하는 방법
        # strs[i].length = k
        # Time Complexity : O(n*klog(k))
        # Space Complexity : O(n*k)

        """
        
        n = len(strs)
        word_dict = defaultdict(list)

        for word in strs:
            key = hash(''.join(sorted(word)))
            word_dict[key].append(word)

        ret = []
        for value in word_dict.values():
            ret.append(value)
        return ret
        """

        # Better Solution : Counting 
        
        # anagram 의 특성 중 알파벳 카운트 갯수가 같다는 것을 이용
        # 카운트 갯수를 활용하여 key 값으로 처리
        # Time Complexity : O(n*k)
        # Space Complexity : O(n*k)
        word_dict = defaultdict(list)
        
        for word in strs:
            freq = [0]*26
            for char in word:
                freq[ord(char) - ord('a')] += 1
            word_dict[tuple(freq)].append(word)

        return list(word_dict.values())
        


