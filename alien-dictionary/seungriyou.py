# https://leetcode.com/problems/alien-dictionary/

from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        [Complexity]
            (V = words 내 unique 문자 개수, E = edge 개수, L = words내 모든 문자 개수)
            - TC: O(V + L) (topo sort에 O(V + E) 소요 -> E < L 이므로)
            - SC: O(V + E) (graph)

        [Approach]
            topo sort를 이용하여, words에 포함된 전체 문자 개수와 topo sort 순으로 방문한 문자 개수를 비교하여 결과를 반환한다.
            1) directed graph를 구성할 때, words에서 두 인접한 단어를 비교하며 첫 번째로 다른 문자가 나올 때 graph & indegree를 기록한다. (sorted lexicographically)
               이때, 순서 resolving이 불가능한 경우를 판단하여 빠르게 반환할 수 있다.
               (인접한 두 단어를 순서대로 w1, w2라고 할 때, (1) w2보다 w1이 더 길면서 (2) w2가 w1에 포함되는 경우, w1의 나머지 부분에 있는 문자는 순서를 알 수 없다.)
            2) 이렇게 기록한 graph & indegree를 기반으로 topo sort로 방문한 문자 개수와 전체 문자 개수를 비교하여 cycle이 발생하지 않는지 확인하고,
               cycle이 발생하지 않았다면 결과를 반환, cycle이 발생했다면 빈 문자열을 반환한다.
        """
        from collections import defaultdict, deque

        # directed graph
        graph, indegree = {}, {}
        for word in words:
            for w in word:
                graph[w] = set()
                indegree[w] = 0

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            # 두 인접한 단어를 비교하면서, 첫 번째로 다른 문자가 나올 때 graph & indegree 기록
            for j in range(min(len(w1), len(w2))):
                c1, c2 = w1[j], w2[j]
                # 첫 번째로 다른 문자 발견 시, 기록 후 다음 단어로 넘어가기
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegree[c2] += 1
                    break
                # 순서를 resolve 할 수 없는 경우, 빠르게 리턴   *****
                # ex) words = ["abc", "ab"] (w1 = "abc", w2 = "ab")
                # -> (1) w2보다 w1이 더 길고 (2) w2가 w1에 포함된다면 (=현재 j가 w2의 마지막 문자를 가리키고 있다면)
                #    w1[j + 1] 이후의 문자에 대해서는 순서를 resolve 할 수 없음
                elif len(w1) > len(w2) and j == min(len(w1), len(w2)) - 1:
                    return ""

        # topo sort
        q = deque([w for w, ind in indegree.items() if ind == 0 and w in graph])
        res = []

        while q:
            w = q.popleft()
            res.append(w)

            for nw in graph[w]:
                indegree[nw] -= 1
                if indegree[nw] == 0:
                    q.append(nw)

        return "".join(res) if len(res) == len(graph) else ""
