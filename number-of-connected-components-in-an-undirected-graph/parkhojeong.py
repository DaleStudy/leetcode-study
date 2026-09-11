class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edge_dic = {i: [i] for i in range(n)}

        for edge in edges:
            start, end = sorted(edge)
            edge_dic[start].append(end)
            edge_dic[end].append(start)

        def traverse(idx: int):
            while edge_dic[idx]:
                end = edge_dic[idx].pop()
                traverse(end)

        cnt = 0
        for i in range(n):
            if len(edge_dic[i]) > 0:
                cnt += 1
                traverse(i)

        return cnt

