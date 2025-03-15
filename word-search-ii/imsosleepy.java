// 모든 위치에서 DFS를 실행 or BFS를 돌면서 단어 찾는 경우 모든 경우에 타임아웃이 발생
// 도저히 해결을 못할거 같아서 GPT의 도움을 받음
// Trie를 이용했는데 조금 더 고민해봐야할 듯
class TrieNode {
    Map<Character, TrieNode> children = new HashMap<>();
    String word = null;
}

class Solution {
    public List<String> findWords(char[][] board, String[] words) {
        List<String> result = new ArrayList<>();
        TrieNode root = buildTrie(words);

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                dfs(board, i, j, root, result);
            }
        }
        return result;
    }

    // Trie(트라이) 자료구조를 구축
    private TrieNode buildTrie(String[] words) {
        TrieNode root = new TrieNode();
        for (String word : words) {
            TrieNode node = root;
            for (char c : word.toCharArray()) {
                node.children.putIfAbsent(c, new TrieNode());
                node = node.children.get(c);
            }
            node.word = word; 
        }
        return root;
    }

    // DFS + 백트래킹 탐색
    private void dfs(char[][] board, int i, int j, TrieNode node, List<String> result) {
        char c = board[i][j];
        if (!node.children.containsKey(c)) return; // 현재 문자와 일치하는 것이 Trie에 없으면 종료

        TrieNode nextNode = node.children.get(c);
        if (nextNode.word != null) { // 단어를 찾았으면 결과 리스트에 추가
            result.add(nextNode.word);
            nextNode.word = null; // 중복 방지를 위해 제거
        }

        // 방문 표시 (백트래킹을 위해)
        board[i][j] = '#';

        // 4방향 탐색
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};
        for (int d = 0; d < 4; d++) {
            int x = i + dx[d], y = j + dy[d];
            if (x >= 0 && x < board.length && y >= 0 && y < board[0].length) {
                dfs(board, x, y, nextNode, result);
            }
        }

        // 백트래킹 (원래 문자로 복원)
        board[i][j] = c;

        // **최적화**: 더 이상 자식이 없으면 Trie에서 해당 노드 삭제
        if (nextNode.children.isEmpty()) {
            node.children.remove(c);
        }
    }
}
