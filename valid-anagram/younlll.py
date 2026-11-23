class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

	'''
        Time complexity of len(s) and len(t): O(n), O(n)
        Time complexity of comparing len(s) and len(t): O(1)
        Dictionary comparing: O(k)
        Thus, O(n) + O(n) + O(1) + O(k) = O(n)
        '''
        if len(s) != len(t):
            return False

	return Counter(s)==Counter(t)

