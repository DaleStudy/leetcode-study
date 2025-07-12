/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
const rotate = function (matrix) {
    const n = matrix.length;

    // 상하좌우 겉에서부터 한 겹씩 안으로 진입
    for (let layer = 0; layer < Math.floor(n / 2); layer++) {

        // layer 위의 각 칸들을 rotate
        // 하나를 rotate했을 때 연쇄적으로 rotate되는 규칙을 이용해
        // 네 칸 rotate하는 걸 x번 반복함

        // x = n - 2 * layer - 1
        // 전체 배열 크기 n에서 layer만큼 안쪽으로 들어가야 하는데
        // 상하, 좌우만큼 들어가야 하니까 2를 곱함
        // 1을 안 빼면 이미 rotate한 자리를 다시 rotate하므로 빼줌

        for (let i = 0; i < n - 2 * layer - 1; i++) {
            const top = layer;
            const bottom = n - 1 - layer;
            const left = top;
            const right = bottom;

            const topLeft = matrix[top][left + i];
            matrix[top][left + i] = matrix[bottom - i][left];
            matrix[bottom - i][left] = matrix[bottom][right - i];
            matrix[bottom][right - i] = matrix[top + i][right];
            matrix[top + i][right] = topLeft;
        }
    }
};

// 시간복잡도: O(n^2)
// 공간복잡도: O(1)

// 참고로 중첩 구조를 다음과 같이 바꿔도 됨
const top = 0;
const bottom = n - 1;

while (top < bototm) {
  const left = top;
  const right = bottom;
  
  for (let i = top; i < bottom; i ++) {
    // rotate
  }

  top++;
  bottom--;
}
