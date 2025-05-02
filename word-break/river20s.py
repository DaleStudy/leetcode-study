class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        currentNode = self.root
        for char in word:
            if char not in currentNode.children:
                currentNode.children[char] = TrieNode()
            currentNode = currentNode.children[char]
        currentNode.isEndOfWord = True

# <-- 여기까지 Trie 구현을 위한 TrieNode와 Trie 클래스 
# --> 여기부터 Word Break 문제 푸는 Solution 클래스

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # 1. 트라이 구축
        # wordDict 모든 단어 -> 트라이 넣기
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        
        n = len(s) # 문자열 s의 길이, 나중에 인덱스 끝까지 도달했는지 확인하기 위해 사용함

        # 2. 재귀 함수 정의
        # canBreak(start_index): s[strat_index:] 부분을 분할할 수 있는지 확인
        def canBreak(start_index: int) -> bool:

            # 베이스 케이스
            # 시작 인덱스(start_index)가 문자열 끝에 도달했다면 성공
            if start_index == n:
                return True

            # 현재 start_index부터 시작하는 가능한 모든 단어를 트라이를 이용해 찾고
            # 각 단어에 대해 나머지 부분이 분할 가능한지 재귀적으로 확인
            currentNode = trie.root

            for i in range(start_index, n):
                char = s[i]

                # 현재 문자가 트라이 경로에 없다면 해당 트라이 탐색은 더이상 진행하지 않음
                if char not in currentNode.children:
                    break

                # 트라이의 다음 노드로 이동
                currentNode = currentNode.children[char]

                # 이동한 노드가 단어의 끝이라면
                if currentNode.isEndOfWord:
                    # 나머지 부분 s[i+1:]에 대해서도 분할 가능한지 재귀 호출
                    if canBreak(i + 1):
                        # 나머지 부분 분할 성공 => 전체 분할 가능
                        return True
            # start_index부터 시작하는 모든 가능한 단어 분할을 시도했으나
            # 성공적인 경로를 찾지 못했다면
            return False
    
        # 3. 재귀 함수 호출 시작 
        return canBreak(0)
