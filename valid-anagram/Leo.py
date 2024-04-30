class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        counter_dict = collections.defaultdict(int)

        for i in s:
            counter_dict[i] += 1

        for i in t:
            counter_dict[i] -= 1

        for val in counter_dict.values():
            if val != 0:
                return False

        return True
        # TC:O(n), SC: O(len(s or t))
        # return sorted(s) == sorted(t) ## O(nlogn)
