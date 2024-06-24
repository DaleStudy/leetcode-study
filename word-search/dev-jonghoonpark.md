- https://leetcode.com/problems/word-search/
- https://algorithm.jonghoonpark.com/2024/06/23/leetcode-79

## TC, SC

`board` 의 길이를 `w`, `board[i]`의 길이를 `h`, 단어의 길이를 `n` 이라고 하였을 때.
시간 복잡도는 `O(w * h * n)` 이다. 공간 복잡도는 `O(n)`이다.

## 풀이

```java
class Solution {
    public boolean exist(char[][] board, String word) {
        char[] chars = word.toCharArray();
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (dfs(board, chars, i, j, 0, word.length() - 1)) {
                    return true;
                }
            }
        }

        return false;
    }

    public boolean dfs(char[][] board, char[] chars, int i, int j, int pointer, int end) {
        if (i < 0 || i > board.length - 1 || j < 0 || j > board[0].length - 1 || board[i][j] != chars[pointer]) {
            return false;
        }

        if(pointer == end) {
            return true;
        }

        int next = pointer + 1;
        char temp = board[i][j];
        board[i][j] = ' ';
        boolean result = dfs(board, chars, i + 1, j, next, end)
                || dfs(board, chars, i - 1, j, next, end)
                || dfs(board, chars, i, j + 1, next, end)
                || dfs(board, chars, i, j - 1, next, end);
        if(!result) {
            board[i][j] = temp;
        }
        return result;
    }
}
```
