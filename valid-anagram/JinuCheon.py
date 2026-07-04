# my own solution
# O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = {}
        for ch in s:
            count1[ch] = count1.get(ch, 0) + 1
        
        count2 = {}
        for ch in t:
            count2[ch] = count2.get(ch, 0) + 1

        return count1 == count2
    
# gpt suggestion
### half space
#### O(n)
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        for ch in t:
            count[ch] = count.get(ch, 0) - 1
        return all(v == 0 for v in count.values())
    
### simple solution (What??)
#### O(n)
#### Counter works like my own solution internally. But I'm ganna forgot this, becuase I'm learning now.
from collections import Counter
class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

### using sort
#### O(n log n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
