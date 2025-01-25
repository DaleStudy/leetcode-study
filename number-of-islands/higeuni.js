/**
 * @param {character[][]} grid
 * @return {number}
 * 
 * 접근
 * dfs로 접근
 * 
 * 1. 방문한 노드는 0으로 바꿔줘야 함
 * 2. 방문한 노드는 방문여부를 잘 체크해야 함
 * 
 * complexity
 * time: O(m*n)
 * space: O(m*n)
 */
var numIslands = function(grid) {
    let answer = 0;
    const numRows = grid.length;
    const numCols = grid[0].length;
    
    const dr = [-1, 1, 0, 0];
    const dc = [0, 0, -1, 1];
    
    const dfs = (row, col) => {
        if (row < 0 || col < 0 || row >= numRows || col >= numCols || grid[row][col] === '0') return;
        
        grid[row][col] = '0';
        
        for (let i = 0; i < 4; ++i) {
            dfs(row + dr[i], col + dc[i]);
        }
    };
    
    for (let r = 0; r < numRows; ++r) {
        for (let c = 0; c < numCols; ++c) {
            if (grid[r][c] === '1') {
                dfs(r, c);
                answer++;
            }
        }
    }
    
    return answer;
};

