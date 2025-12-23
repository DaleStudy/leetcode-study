class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = []
        max_s = 0
        for i in s:
            if i not in h:
                h.append(i)
            else:
                h=h[h.index(i)+1:]
                h.append(i)
                #I reset h=[] but it had problemswith the cases like "dvdf"
                #So I modified it to h=h[h.index(i)+1:]
            max_s = max(max_s, len(h))
        
        return max_s

#O(N^2) time complexity due to "if i not in h" and O(min(m,n)) space complexity where m is the size of the charset and n is the size of the string s.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        start = 0
        max_len = 0
        for i, char in enumerate(s):
            if char in seen and seen[char]>=start:
                start= seen[char]+1    
            seen[char]=i
            max_len = max(max_len, i - start +1)
            
        return max_len
#O(N) time complexity and O(min(m,n)) space complexity where m is the size of the charset and n is the size of the string s.
#Dictionary search and insert operations are O(1) on average. so it is O(N) overall.