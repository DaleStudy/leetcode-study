class TrieNode:
    def __init__(self):
        self.children = {}  # 현재 문자에서 갈 수 있는 다음 문자들 저장
        self.word = None    # 이노드에서 끝나는 단어가 있다면 저장
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # 다시풀어볼것. 어려웠음. Trie! 보드로 탐색해야함!(단어로 탐색하는게 아님!)
        # DFS(백트래킹), trie
        # DFS로만 풀면 TLE(시간초과)뜸. trie구조를 이용해야함. 
        
        # Trie루트노드 생성
        root = TrieNode()

        # words 리스트를 기반으로 Trie 생성
        for word in words:
            node = root

            for i in word:

                if i not in node.children:
                    node.children[i] = TrieNode()
                node = node.children[i]
            
            node.word = word    # 단어 끝에서 word 저장

        answer = []

        rows, cols = len(board), len(board[0])

        # DFS
        def dfs(x, y, node):
            c = board[x][y]

            # 현재 문자가 트라이에 없으면 바로 종료
            if c not in node.children:
                return 

            next_node = node.children[c]

            # 단어를 찾으면 answer에 추가하고, 중복방지위해 None처리
            if next_node.word:
                answer.append(next_node.word)
                next_node.word = None   # 중복방지

            board[x][y] = '#'   # 현재위치 '#'로 방문표시

            # 상하좌우 DFS 탐색
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x + dx, y + dy
                # 범위 내에 있고, 아직 방문하지 않은 위치라면 DFS 탐색
                if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] != '#':
                    dfs(nx, ny, next_node)
            
            # DFS 종료 후, 원래 문자로 복구(백트래킹)
            board[x][y] = c # 원상복구

        
        # DFS 시작점(모든 보드 칸을 시작점으로 DFS 탐색)
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root)

        return answer
