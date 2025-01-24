/**
 * 2차원 배열을 돌며 0을 적용해야하는 row와 col을 조회 후 다시 2차원 배열을 돌며 0으로 변환
 * @param {number[][]} matrix - 2차원 배열
 * @return
 * 
 * - 시간 복잡도: O(m * n)
 *   - m x n 크기의 배열을 2번 순회
 * 
 * - 공간 복잡도: O(m + n)
 *  - 최대 m(행) +  n(열) 크기의 Set을 사용
 */
function setZeroes(matrix) {
    const m = matrix.length;
    const n = matrix[0].length;

    const rowZeroSet = new Set();
    const colZeroSet = new Set();

    // 배열을 돌며 0으로 바꿔야 할 행과 열을 기록 
    for (let i=0; i < m; i ++) {
        for (let j=0; j < n; j++) {
            if (matrix[i][j] === 0) {
                rowZeroSet.add(i);
                colZeroSet.add(j);
            }
        }
    }

    // 0으로 변경해야 하는 행과 열을 변환 
     for (let i=0; i < m; i ++) {
        for (let j=0; j < n; j++) {
            if (rowZeroSet.has(i) || colZeroSet.has(j)) {
                matrix[i][j] = 0;
            }
        }
    }
}

