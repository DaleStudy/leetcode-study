class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_word = True

    def search(self, word: str) -> bool:
        return self._dfs(self.root, word, 0)

    def _dfs(self, node: TrieNode, word: str, index: int) -> bool:
        # 단어 끝에 도달하면 is_end_word 확인
        if index == len(word):
            return node.is_end_word

        char = word[index]

        if char == '.':
            # '.'는 모든 자식 노드 탐색
            for child in node.children.values():
                if self._dfs(child, word, index + 1):
                    return True
            return False
        else:
            # 일반 문자는 해당 자식으로 이동
            if char not in node.children:
                return False
            return self._dfs(node.children[char], word, index + 1)


"""
================================================================================
풀이 과정
================================================================================

[1차 시도] 길이별 그룹화 + 브루트포스 매칭
────────────────────────────────────────────────────────────────────────────────
1. 아이디어: 같은 길이 단어끼리 묶고, 하나씩 패턴 비교
   words = { 3: ["bad", "dad", "mad"] }
   search(".ad") → 모든 길이 3 단어와 비교

2. 문제점: Time Limit Exceeded!
   - 같은 길이 단어가 많으면 O(N × L) 반복
   - LeetCode 테스트케이스에서 시간 초과

3. 더 효율적인 방법 필요 → Trie로 접근

────────────────────────────────────────────────────────────────────────────────
[2차 시도] Trie (트라이) 자료구조
────────────────────────────────────────────────────────────────────────────────
4. Trie 구조 (bad, dad, mad 저장 후):

   root
   ├── 'b' → 'a' → 'd' (is_end_word=True)
   ├── 'd' → 'a' → 'd' (is_end_word=True)
   └── 'm' → 'a' → 'd' (is_end_word=True)

5. 동작 예시:

   search("bad"):
   root → 'b' → 'a' → 'd' → is_end_word=True → True

   search(".ad"):
   root → '.' (모든 자식 탐색)
        → 'b' → 'a' → 'd' → True (첫 번째에서 찾음!)

   search("b.."):
   root → 'b' → '.' (모든 자식)
              → 'a' → '.' (모든 자식)
                    → 'd' → True

6. 왜 Trie가 더 빠른가?
   - 정확한 문자: O(1)로 해당 자식만 탐색
   - '.': 해당 위치에서만 분기, 이후는 다시 좁혀짐
   - 브루트포스: 모든 단어를 처음부터 끝까지 비교

7. 시간복잡도:
   - addWord: O(L) - L은 단어 길이
   - search: O(L) ~ O(26^m) - m은 '.' 개수 (보통 적음)

8. 공간복잡도: O(N × L) - 모든 단어의 문자 저장

9. 구현 포인트:
    - TrieNode 클래스 분리 → 가독성 향상
    - _dfs 재귀로 '.' 처리 → 모든 자식 탐색
    - is_end_word로 단어 끝 표시 → 접두사와 구분
"""
