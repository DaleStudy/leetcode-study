"""
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/description/

Solution:
    - Create a hash table and a list of counters
    - For each string in the input list:
        - Sort the string
        - If the sorted string is in the hash table:
            - Append the string to the corresponding counter list
        - Else:
            - Add the sorted string to the hash table
            - Create a new counter list and append the string
    - Return the list of counters

Time complexity: O(nmlogm)
    - The for loop runs n times
    - The sorted function runs O(mlogm) times
    - m is the length of the longest string in the input list

Space complexity: O(n)
    - The output list has n elements
    - The hash table has n elements
    - The list of counters has n elements    
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_table = dict()
        output = []

        for s in strs:
            count_s = ''.join(sorted(s))
            if count_s in hash_table:
                idx = hash_table[count_s]
                output[idx].append(s)
            else:
                hash_table[count_s] = len(output)
                output.append([s])
                 
        return output

