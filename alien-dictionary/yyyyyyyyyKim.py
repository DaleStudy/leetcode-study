"""
LintCode 892. Alien Dictionary
https://www.lintcode.com/problem/892/
https://leetcode.com/problems/alien-dictionary/

summary:
외계인 단어 목록이 사전 순으로 정렬되어 있을 때,
단어 간의 비교를 통해 문자의 순서를 유추해 전체 외계인 알파벳 순서를 구하는 문제
"""
from typing import (
    List,
)

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alien_order(self, words: List[str]) -> str:
        
        # 무조건다시풀어볼것. 어려움어려움.
        # DFS기반 후위순회(post-order) 위상 정렬
        # 시간복잡도 O(N*L+V+E), 공간복잡도 O(V+E)
        # V = 등장한 문자의 수(최대26개), E = 간선수(문자간순서), N = 단어수, L = 각 단어의 평균 길이
        
        # 그래프 만들기(문자별 연결 정보)
        graph = {}

        # visited
        # 0: 방문 안함
        # 1: 방문 중(현재 탐색 중)
        # 2: 방문 완료(사이클 없음 확인 완료)
        visited = {}
        answer = []

        # 노드 초기화(모든 문자 그래프에 넣기)
        for word in words:
            for i in word:
                if i not in graph:  # 없으면 넣기(중복방지)
                    graph[i] = []

        # 문자 간선 설정
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            min_len = min(len(w1), len(w2))

            # 앞단어가 뒷단어의 접두사인데 더 길면 잘못된 입력이므로 '' 반환
            if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
                return ''

            for j in range(min_len):
                c1 = w1[j]
                c2 = w2[j]
                # c1과 c2가 다른 문자이고 c1에 c2가 없으면 c1의 그래프에 c2 추가
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].append(c2)
                    break

        # 자식 노드가 여러 개일 경우, 사전순 탐색을 위해 자식 노드 정렬
        for i in graph:
            graph[i].sort()

        # DFS 함수
        def dfs(node):
            # visited.get(node, 0) : 방문하지 않은 경우 기본값 0 반환
            if visited.get(node, 0) == 1:
                return False    # 사이클 발생
            if visited.get(node, 0) == 2:
                return True     # 방문 완료
            
            # 방문 중 표시
            visited[node] = 1

            # 인접 노드(다음문자) 탐색
            for i in graph[node]:
                if not dfs(i):
                    return False

            # 탐색 완료(방문 완료)
            visited[node] = 2
            answer.append(node)
            
            return True

        # 모든 노드 dfs 탐색
        for i in graph:
            if visited.get(i, 0) == 0:
                if not dfs(i):
                    return ''   # 사이클이면 잘못된 입력


        # post-order니까 역순으로 반환
        return ''.join(reversed(answer))
