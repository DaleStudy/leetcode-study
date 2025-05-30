/**
 * @param {number[][]} heights
 * @return {number[][]}
 */
const pacificAtlantic = function (heights) {
    // 각 cell에서 시작해서 바다로 뻗어나가는 것 말고
    // 바다에서 시작해서 각 cell이 바다로 흘러올 수 있는지 확인한 후
    // 두 바다에 모두 흘러갈 수 있는 cell만 filter

    const rows = heights.length;
    const cols = heights[0].length;

    // 각 바다에 도달 가능한지 여부를 담는 visited를 만듦
    const pacific = Array.from({ length: rows }, () => Array(cols).fill(false));
    const atlantic = Array.from({ length: rows }, () => Array(cols).fill(false));

    const direction = [[0, 1], [0, -1], [1, 0], [-1, 0]];

    // 순회
    function bfs(r, c, visited) {
        visited[r][c] = true;

        const queue = [[r, c]];

        while (queue.length) {
            const [r, c] = queue.shift();

            for (const [dr, dc] of direction) {
                const nr = r + dr;
                const nc = c + dc;

                // 나보다 height가 크고, 방문한 적 없으면, 큐에 담기
                if (0 <= nr && nr < rows && 0 <= nc && nc < cols
                    && !visited[nr][nc]
                    && heights[nr][nc] >= heights[r][c]
                ) {
                    queue.push([nr, nc]);
                    visited[nr][nc] = true;
                }
            }
        }
    }

    // 바다에서 시작해서 거꾸로 탐색
    for (let r = 0; r < rows; r++) {
        bfs(r, 0, pacific); // left
        bfs(r, cols - 1, atlantic); // right
    }

    for (let c = 0; c < cols; c++) {
        bfs(0, c, pacific); // top
        bfs(rows - 1, c, atlantic); // bottom
    }

    // 태평양, 대서양으로 모두 flow할 수 있는 cell 찾기
    const result = [];

    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (pacific[r][c] && atlantic[r][c]) {
                result.push([r, c]);
            }
        }
    }

    return result;
};

// 시간복잡도: O(m*n)
// 공간복잡도: O(m*n)
