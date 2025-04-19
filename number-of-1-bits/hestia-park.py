class Solution:
    def hammingWeight(self, n: int) -> int:
        # ans=0
        # # bit=[]
        # moc=n
        # while moc > 0:
        #     nam=moc%2
        #     if nam==1:
        #         ans+=1
        #     moc=int((moc-nam)/2)

        # return ans
        # using Brian Kernighan’s Algorithm
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count


