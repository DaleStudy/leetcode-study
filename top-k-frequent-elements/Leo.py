class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_dict = collections.Counter(nums)
        freq = num_dict.most_common()
        ans = []

        for key, val in freq:
            if k == 0:
                break

            ans.append(key)
            k -= 1

        return ans

        ## TC: O(n * logn), SC: O(n)
