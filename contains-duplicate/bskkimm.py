from collections import defaultdict
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # [1,2,3,1]

        # [1,1,1,3,3,4,3,2,4,2]

        # add element to a dict
        # if a same value appears, then return True
        # if a for loop ends without disruption, return False

        dict = defaultdict(bool)

        for num in nums:
            if dict[num]:
                return True
            else:
                dict[num] = True

        return False