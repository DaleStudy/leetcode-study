'''
# Leetcode 347. Top K Frequent Elements

use **Counter** to count the frequency of each element in the list 🚀
use **sorted()** to sort the elements by their frequency in descending order.

## Time and Space Complexity

```
TC: O(n log n)
SC: O(n)
```

### TC is O(n log n):
- iterating through the list just once to count the frequency of each element. = O(n)
- sorting the elements by their frequency in descending order. = O(n log n)

### SC is O(n):
- using a Counter to store the frequency of each element. = O(n)
- sorted() creates a new list that holds the elements of frequency_map. = O(n)
- result list that holds the top k frequent elements. = O(k)
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = Counter(nums) # TC: O(n), SC: O(n)
        sorted_frequencies = sorted(frequency_map.items(), key=lambda x: x[1], reverse=True) # TC: O(n log n), SC: O(n)
        
        result = [] # SC: O(k)
        for e in sorted_frequencies: # TC: O(k)
            result.append(e[0])

        return result[0:k]
