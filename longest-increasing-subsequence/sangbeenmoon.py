# hint 를 보고 해결.
# DP 로도 풀 수 있음.

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seq = []


        for num in nums:
            if len(seq) == 0:
                seq.append(num)
                continue

            i = 0
            
            while seq[i] < num:
                i = i + 1

                if i > len(seq) - 1:
                    break
            
            if i > len(seq) - 1:
                seq.append(num)
            else:
                seq[i] = num
    
        return len(seq)
