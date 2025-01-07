'''
# 49. Group Anagrams

use **hash map** to solve the problem.

## Time and Space Complexity
```
TC: O(N * K * Log(K))
SC: O(N * K)
```

## TC is O(N * K * Log(K)):
- iterating through the list of strings and sorting each string. = O(N * K * Log(K))

## SC is O(N * K):
- using a hash map to store the sorted strings. = O(N * K)
'''
class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      result = defaultdict(list)
      
      for str in strs: # TC: O(N)
          sorted_key = ''.join(sorted(str)) # sorting 👉 TC: O(K * Log(K))
          result[sorted_key].append(str) # TC: O(1) on average
      
      return list(result.values())

