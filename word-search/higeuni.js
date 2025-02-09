/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 * 
 * complexity
 * time: O(n * m * 4^l)
 * space: O(n * m)
 */

var exist = function(board, word) {
  word = word.split('');
  const dx = [-1, 1, 0, 0];
  const dy = [0, 0, 1, -1];
  const visited = Array.from({length: board.length}, () => Array(board[0].length).fill(false));

  const dfs = (length, x, y) => {
      if(word.length === length) {
          return true;
      }
      for(let i = 0; i < 4; ++i) {
          const nx = x + dx[i];
          const ny = y + dy[i];
          if(0 <= nx && nx < board[0].length && 0 <= ny && ny < board.length){
              if(board[ny][nx] === word[length] && !visited[ny][nx]) {
                  visited[ny][nx] = true;
                  if(dfs(length + 1, nx, ny)) return true;
                  visited[ny][nx] = false;
              } 
          }
      }
      return false;
  }

  for(let i = 0; i < board.length; ++i){
      for(let j = 0; j < board[0].length; ++j){
          if(board[i][j] === word[0]) {
              visited[i][j] = true;
              if(dfs(1, j, i)) return true;
              visited[i][j] = false;
          }
      }
  }

  return false;
};

