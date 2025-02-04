/**
 * 깊이 우선 탐색(DFS)을 사용하여 특정 바다에서 올라갈 수 있는 좌표을 저장
 * @param i 현재 위치의 행 (row)
 * @param j 현재 위치의 열 (column)
 * @param visited 방문한 좌표를 저장하는 Set (바다에서 도달할 수 있는 위치를 저장)
 * @param heights 높이 정보가 담긴 2차원 배열
 * 
 * 시간 복잡도: O(m × n)  
 *  - 각 셀은 최대 한 번 방문하며, 총 m × n개의 셀을 탐색함
 * 
 * 공간 복잡도: O(m × n)  
 *  - `visited` Set에 최대 m × n개의 좌표를 저장 가능
 *  - 재귀 호출 스택의 깊이는 O(m + n) (최악의 경우 가장 긴 경로를 따라 탐색)
 */
function dfs(i: number, j: number, visited: Set<string>, heights: number[][]) {
    if (visited.has(`${i},${j}`)) return;
    
    visited.add(`${i},${j}`);

    for (const [di, dj] of [[-1, 0], [1, 0], [0, -1], [0, 1]]) {
        const newI = i + di;
        const newJ = j + dj;

        if (
            newI >= 0 && newI < heights.length && 
            newJ >= 0 && newJ < heights[0].length &&
            heights[newI][newJ] >= heights[i][j]
        ) {
            dfs(newI, newJ, visited, heights);
        }
    }
};

/**
 * 두 바다 모두 도달할 수 있는 좌표를 찾는 함수
 * 
 * @param heights 2차원 배열로 이루어진 지형의 높이 정보
 * @returns 두 바다 모두 도달할 수 있는 좌표 배열
 * 
 * 시간 복잡도: O(m × n)  
 *  - 태평양 및 대서양에서 각각 DFS 수행 → O(m × n)
 *  - 결과를 찾는 이중 루프 → O(m × n)
 * 
 * 공간 복잡도: O(m × n)  
 *  - `pacificSet`과 `atlanticSet`에 최대 O(m × n)개의 좌표 저장
 * 
 */
function pacificAtlantic(heights: number[][]): number[][] {
    if (!heights || heights.length === 0 || heights[0].length === 0) return [];

    const rows = heights.length;
    const cols = heights[0].length;
    
    const pacificSet = new Set<string>();
    const atlanticSet = new Set<string>();

    // 태평양(왼쪽, 위쪽)에서 출발하는 DFS
    for (let i = 0; i < rows; i++) dfs(i, 0, pacificSet, heights);
    for (let j = 0; j < cols; j++) dfs(0, j, pacificSet, heights);

    // 대서양(오른쪽, 아래쪽)에서 출발하는 DFS
    for (let i = 0; i < rows; i++) dfs(i, cols - 1, atlanticSet, heights);
    for (let j = 0; j < cols; j++) dfs(rows - 1, j, atlanticSet, heights);

    const result: number[][] = [];
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            if (pacificSet.has(`${i},${j}`) && atlanticSet.has(`${i},${j}`)) {
                result.push([i, j]);
            }
        }
    }
    
    return result;
};

