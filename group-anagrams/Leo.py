class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            ans[str(sorted(s))].append(s)

        return list(ans.values())

        ## TC: O(n * klogk), SC: O(n * k), where n is len(strs) and k is len(longest_s)

        # ans = {}

        # for s in strs:
        #     sorted_s = ''.join(sorted(s))

        #     if sorted_s not in ans:
        #         ans[sorted_s] = []

        #     ans[sorted_s].append(s)

        # return list(ans.values())
