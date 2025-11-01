from typing import (
    List,
)

import heapq
    heap = [c for c in indegree if indegree[c] == 0]
    heapq.heapify(heap)
    res = []
    

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alien_order(self, words: List[str]) -> str:
        # Write your code here
        adj = {c: set() for word in words for c in word}
        indegree = {c: 0 for c in adj}
    
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minlen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ""
            for j in range(minlen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break
        
        while heap:
            c = heapq.heappop(heap)
            res.append(c)
            for nei in adj[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    heapq.heappush(heap, nei)
        
        if len(res) != len(adj):
            return ""
        
        return "".join(res)
