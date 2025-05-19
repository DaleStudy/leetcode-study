/**
[문제풀이]
- 이웃되는 알파벳이 이어져야 한다.
- 각 알파벳은 한번만 호출되어야 한다.
- DFS
time: O(N M 4^L), space: O(L)

[회고]
BFS로 풀면 되지 않을까 했지만, 최단경로를 찾는 것이 아니니 안 어울릴 것 같다.
DFS로 풀자는 방법은 맞았지만, 풀이과정이 어려웠다.
다시 풀어보면 좋을 것 같다.
 */

class Solution {
    public boolean exist(char[][] board, String word) {
        int column = board.length;
        int row = board[0].length;
        boolean[][] visited = new boolean[column][row];

        for (int i = 0; i < column; i++) {
            for (int j = 0; j < row; j++) {
                if (board[i][j] == word.charAt(0)) {
                    if (dfs(board, word, visited, i, j, 0)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

    private boolean dfs(char[][] board, String word, boolean[][] visited, int i, int j, int wordIndex) {
        if (wordIndex == word.length()) {
            return true;
        }

        if (isVisited(board, word, visited, i, j, wordIndex)) {
            return false;
        }

        visited[i][j] = true;
        if (dfs(board, word, visited, i + 1, j, wordIndex + 1) || 
            dfs(board, word, visited, i - 1, j, wordIndex + 1) ||
            dfs(board, word, visited, i, j + 1, wordIndex + 1) ||
            dfs(board, word, visited, i, j - 1, wordIndex + 1)
        ) {
            return true;
        }

        visited[i][j] = false;
        return false;
    }

    private boolean isVisited(char[][] board, String word, boolean[][] visited, int i, int j, int wordIndex) {
        return i < 0 ||
            j < 0 ||
            i >= board.length ||
            j >= board[0].length ||
            visited[i][j] ||
            board[i][j] != word.charAt(wordIndex);
    }
}

