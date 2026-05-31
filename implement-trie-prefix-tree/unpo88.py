class Trie:

      def __init__(self):
          self.children = {}
          self.is_end = False

      def insert(self, word: str) -> None:
          node = self
          for c in word:
              if c not in node.children:
                  node.children[c] = Trie()
              node = node.children[c]
          node.is_end = True

      def search(self, word: str) -> bool:
          node = self._find(word)
          return node is not None and node.is_end

      def startsWith(self, prefix: str) -> bool:
          return self._find(prefix) is not None

      def _find(self, s: str):
          node = self
          for c in s:
              if c not in node.children:
                  return None
              node = node.children[c]
          return node


"""
================================================================================
풀이 과정
================================================================================

[문제 이해]
────────────────────────────────────────────────────────────────────────────────
1. Trie(트라이) 자료구조 구현
2. insert(word): 단어 삽입
3. search(word): 정확히 일치하는 단어 있는지
4. startsWith(prefix): prefix로 시작하는 단어 있는지


[1차 시도] 해시맵
────────────────────────────────────────────────────────────────────────────────
5. 처음에 해싱으로 풀었더니 통과는 했는데 startsWith에서 결국 전체 순회 필요
6. 시간복잡도 O(n × m) → 비효율적, 진짜 Trie로 풀어야겠다


[2차 시도] 진짜 Trie
────────────────────────────────────────────────────────────────────────────────
7. 각 노드가 children(자식 노드들)과 is_end(단어 끝 여부)를 가짐

8. 구조 예시: "app", "apple" 삽입 시

        root
         │
         a
         │
         p
         │
         p (is_end: "app")
         │
         l
         │
         e (is_end: "apple")

9. insert: 문자 하나씩 따라가며 노드 생성, 마지막에 is_end = True
10. search: 문자 따라간 후 is_end가 True인지 확인
11. startsWith: 문자 따라갈 수 있으면 True


[복잡도 분석]
────────────────────────────────────────────────────────────────────────────────
12. 시간복잡도: O(m) - 모든 연산
    - m: 단어/prefix 길이

13. 공간복잡도: O(n × m)
    - n: 단어 개수, m: 평균 단어 길이
""" 
