class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        for n in nums:
            if n in count:
                count[n] +=1
            else:
                count[n] =1      
                # count.items()를 횟수 큰 순으로 정렬
        freq = sorted(count.items(), key=lambda x: x[1], reverse=True)

        result = []
        for x in freq[:k]:
            result.append(x[0])
        return result
    
    
