'''
count a frequency of the character with a hash map
s's character will be added and
t's character will be subtracted

return True if count's min and max value is not a zero
else return False

Time O(n)
Space O(n)
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)

        if len(t) != len(s):
            return False

        for i in range(len(s)):
            count[s[i]] += 1
            count[t[i]] -= 1
            
        if max(count.values()) == 0:
            return True
        return False

