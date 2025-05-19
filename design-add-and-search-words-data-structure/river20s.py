class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
# <<<--- 트라이 자료 구조 사용을 위한 구현 ---<<<
# >>>----------------- 답안 ---------------->>>
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # 추가: word를 자료 구조에 추가
        # 일반적인 트라이 삽입 로직과 같음
        # Time Complexity: O(L),   Space Complexity: O(L)
        # L은 추가할 단어 길이
        currentNode = self.root
        for char in word:
            if char not in currentNode.children:
                currentNode.children[char] = TrieNode()
            currentNode = currentNode.children[char]
        currentNode.isEndOfWord = True

    def search(self, word: str) -> bool:
        # 검색: 자료 구조에 word와 일치하는 문자열이 있으면 True
        # 그렇지 않으면 False 반환
        # 와일드카드 '.'는 어떤 글자도 될 수 있음
        # Time Coplexity: O(M),    Space Complexity: O(M)
        # M은 검색할 단어 길이

        def _dfs_search(node: TrieNode, index_in_search_word: int) -> bool:
            # 재귀를 위한 헬퍼 함수
            # --- 베이스 케이스 ---
            # 검색에 끝에 도달했을 때 트라이 노드가 마지막 노드라면 검색 성공
            if index_in_search_word == len(word):
                return node.isEndOfWord
            
            # 트라이의 현재 노드와 비교해야할 검색어 word의 문자
            char_to_match = word[index_in_search_word]

            # 현재 문자가 알파벳인 경우
            if char_to_match != ".":
                # 자식 노드에 비교할 문자가 없는 경우
                if char_to_match not in node.children:
                    return False
                # 다음 문자에 대한 재귀 호출
                return _dfs_search(node.children[char_to_match], index_in_search_word + 1)

            # 현재 문자가 '.'인 경우
            else:
                # 가능한 모든 자식 노드에 대해 재귀 호출
                for child_node in node.children.values():
                    if _dfs_search(child_node, index_in_search_word + 1):
                        return True # 하나라도 성공하면 True
                return False
        # 최초 재귀 호출
        return _dfs_search(self.root, 0)
