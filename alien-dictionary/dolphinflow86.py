# C is total length of all words, U is number of unique alien letters (<= 26).
# TC: O(C) - comparing adjacent words and processing topological sort graph
# SC: O(1) - unique letters and adjacency list bounded by 26 characters

from collections import deque


class Solution:

    def alienOrder(self, words) -> str:
        adj = {char: set() for word in words for char in word}
        indegree = {char: 0 for word in words for char in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break

        queue = deque([char for char in indegree if indegree[char] == 0])
        result = []

        while queue:
            char = queue.popleft()
            result.append(char)

            for neighbor in adj[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(result) < len(indegree):
            return ""

        return "".join(result)
