# Time Complexity: O(N + K) - where N is total number of characters in all words, and K is total number of unique character relations (edges) we derive
# Space Complexity: O(N + K) - for graph, in-degree map, and heap

class Solution:
    def alien_order(self, words):
        # adjacency list, u -> set of v
        graph = defaultdict(set)  
        # how many chars come before this one
        in_degree = {}  

        # initialize in_degree with all unique chars
        for word in words:
            for char in word:
                in_degree[char] = 0

        # compare each adjacent pair of words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            # handle invalid case like ["abc", "ab"]
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    # first different char tells us the order
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    # only first different char matters
                    break  

        # topological sort (use min heap for smallest lex order)
        heap = []
        for char in in_degree:
            if in_degree[char] == 0:
                heapq.heappush(heap, char)

        result = []
        while heap:
            char = heapq.heappop(heap)
            result.append(char)
            for neighbor in sorted(graph[char]):
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    heapq.heappush(heap, neighbor)

        # if we added all characters into result, it's valid
        if len(result) == len(in_degree):
            return ''.join(result)
        else:
            return ""
