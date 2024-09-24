
#  Runtime: 51ms, Memory: 16.83MB
#  Time complexity: O(len(s))
#  Space complexity: O(len(s))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stringArr = []
        maxLength = 0

        for sub in s :
            if sub in stringArr :    
                maxLength = max(maxLength, len(stringArr))
                repeatIdx = stringArr.index(sub)
                stringArr = stringArr[repeatIdx+1 :]

            stringArr.append(sub)
        
        maxLength = max(maxLength, len(stringArr))


        return maxLength
    