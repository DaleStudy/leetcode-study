# idea : -
# Time Complexity : O(n log n) since counting?
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            ans.append(bin(i)[2:].count("1"))
        return ans

# TODO: O(n)?



