/*
# Time Complexity: O(w + m * n * 4^10)
  - trie에 word 하나(최대 길이 10)를 삽입하는 데에는 O(10) = O(1) 이므로, trie 전체를 생성하는 데에는 O(w) (w는 words의 length)
  - dfs 탐색을 하면서, 모든 경로를 탐색 (최대 depth는 10)
# Space Complexity: O(w)
  - trie를 생성하면, 최대 10글자 * w개 문자열 = O(10w) = O(w)
*/
class Solution {

    private class Trie {
        char val;
        boolean ends;
        Map<Character, Trie> children;

        Trie(char val) {
            this.val = val;
            this.children = new HashMap<>();
        }
    }
    public List<String> findWords(char[][] board, String[] words) {
        // Trie 생성 및 세팅
        Trie root = new Trie('.');
        for (String word : words) {
            Trie curr = root;
            for (int i = 0; i < word.length(); i++) {
                char ch = word.charAt(i);
                curr.children.putIfAbsent(ch, new Trie(ch));
                curr = curr.children.get(ch);
            }
            curr.ends = true;
        }

        // trie와 dfs를 사용하여, 단어가 존재하는지 확인
        int m = board.length;
        int n = board[0].length;
        boolean[][] visited = new boolean[m][n];
        StringBuilder sb = new StringBuilder();
        Set<String> ans = new HashSet<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (!root.children.containsKey(board[i][j])) continue;

                visited[i][j] = true;
                sb.append(board[i][j]);
                dfs(m, n, board, visited, i, j, root.children.get(board[i][j]), sb, ans); //
                sb.deleteCharAt(0);
                visited[i][j] = false;
            }
        }

        return ans.stream().collect(Collectors.toList());
    }

    private void dfs(int m, int n, char[][] board, boolean[][] visited, int r, int c, Trie curr, StringBuilder sb, Set<String> ans) {
        if (curr.ends) ans.add(sb.toString());

        int[] dr = {-1, 0, 1, 0};
        int[] dc = {0, 1, 0, -1};

        for (int i = 0; i < 4; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];
            if (nr < 0 || nr >= m || nc < 0 || nc >= n || visited[nr][nc]) continue;
            if (!curr.children.containsKey(board[nr][nc])) continue;

            visited[nr][nc] = true;
            sb.append(board[nr][nc]);
            dfs(m, n, board, visited, nr, nc, curr.children.get(board[nr][nc]), sb, ans);
            sb.deleteCharAt(sb.length() - 1);
            visited[nr][nc] = false;
        }
    }
}
