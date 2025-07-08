/**
 * <a href="https://leetcode.com/problems/word-search-ii/">week14-5. word-search-ii</a>
 * <li>Description: Given an m x n board of characters and a list of strings words, return all words on the board.</li>
 * <li>Topics: Array, String, Backtracking, Trie, Matrix</li>
 * <li>Time Complexity: O(M*N*4^L), Runtime 446ms   </li>
 * <li>Space Complexity: O(K*L), Memory 44.81MB</li>
 * <li>Note: Refer to answer </li>
 */
class Solution {

    class TrieNode {
        Map<Character, TrieNode> children = new HashMap<>();
        String word = null;
    }

    public List<String> findWords(char[][] board, String[] words) {
        TrieNode root = buildTrie(words);
        List<String> result = new ArrayList<>();

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (root.children.containsKey(board[i][j])) {
                    TrieNode node = root.children.get(board[i][j]);
                    findWord(board, i, j, node, result);
                }
            }
        }

        return result;
    }

    private TrieNode buildTrie(String[] words) {
        TrieNode root = new TrieNode();

        for (String word : words) {
            TrieNode node = root;
            for (char c : word.toCharArray()) {
                node = node.children.computeIfAbsent(c, k -> new TrieNode());
            }
            node.word = word;
        }
        return root;
    }

    private int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    private void findWord(char[][] board, int r, int c, TrieNode node, List<String> result) {
        if (node.word != null) {
            result.add(node.word);
            node.word = null;
        }

        char letter = board[r][c];
        board[r][c] = '#';

        for (int[] direction : directions) {
            int nr = r + direction[0];
            int nc = c + direction[1];

            if (nr < 0 || nr > board.length - 1 || nc < 0 || nc > board[0].length - 1) {
                continue;
            }
            if (node.children.containsKey(board[nr][nc])) {
                TrieNode nextNode = node.children.get(board[nr][nc]);
                findWord(board, nr, nc, nextNode, result);
            }
        }

        board[r][c] = letter;
    }

}

