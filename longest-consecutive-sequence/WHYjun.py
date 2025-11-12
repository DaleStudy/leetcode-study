import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # remove duplicates by using set
        numsSet = set(nums)
        
        if len(numsSet) == 0 or len(numsSet) == 1:
            return len(numsSet)

        # Use priority queue to sort in O(n)
        pq = heapq.heapify(list(numsSet))
        
        prev = heapq.heappop(pq)
        answer, count = 1, 1
        for i in range(len(numsSet) - 1):
            popped = heapq.heappop(pq)
            if prev + 1 == popped:
                count += 1
            else:
                count = 1
            
            prev = popped
            answer = max(answer, count)
    
        return answer

    def longestConsecutiveUsingSetOnly(self, nums: List[int]) -> int:
        # remove duplicates by using set
        numsSet = set(nums)

        answer = 0

        for num in numsSet:
            # continue if it's not the longest consecutive
            if num - 1 in numsSet:
                continue
            else:
                count = 1
                while num + count in numsSet:
                    count += 1
                answer = max(answer, count)

        return answer
