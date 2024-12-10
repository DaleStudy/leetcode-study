import heapq
class Solution(object):
    # Time complexity: O(nlogn)

    # Iterate through all numbers, generate frequency dictionary.
    # create max heap with frequency.
    # pop k items from the heap
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        freq_dict = {}
        for i in nums:
            if i in freq_dict:
                freq_dict[i] += 1
            else:
                freq_dict[i] = 1
        
        my_heap = []
        for key, value in freq_dict.items():
            heapq.heappush(my_heap, (-value, key))
        
        answer = []
        for i in range(k):
            freq, number = heapq.heappop(my_heap)
            answer.append(number)
        
        return answer