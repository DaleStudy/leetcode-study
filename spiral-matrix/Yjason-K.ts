/**
 * 2차원 배열을 [0][0] 시작으로 시계방향으로 1차원 배열로 변환.
 *
 * @param {number[][]} matrix - 2차원 배열
 * @returns {number[]} 시계 방향으로 1차원으로 펼친 배열
 *
 *
 * - 시간 복잡도: O(n * m)
 *   모든 원소가 한 번씩 방문되므로 행과 열의 곱에 비례합니다.
 *
 * - 공간 복잡도: O(n * m)
 *   방문 배열과 출력 목록이 필요하며, 둘 다 입력 배열의 크기와 같은 추가 메모리가 사용됩니다.
 */
function spiralOrder(matrix: number[][]): number[] {
    // 방분 배열 생성
    const visited: boolean[][] = Array.from({length: matrix.length}, () => Array(matrix[0].length).fill(false));
    // flatten할 배열
    const orderList: number[] = [];
    // 전체 길이
    const totalLength = matrix.length * matrix[0].length;
    // 진행 방향 (우, 하, 좌, 상)
    const directions = [[0,1], [1,0], [0,-1], [-1,0]];

    let i = 0; // 시작 i 좌표
    let j = 0; // 시작 j 좌표
    let directionIndex = 0; // 우방향부터 시작

    while (orderList.length < totalLength) {
        // 현재 위치를 방문 처리 orderList에 추가
        orderList.push(matrix[i][j])
        visited[i][j] = true;

        // 다음 위치
        let nextI = i + directions[directionIndex][0];
        let nextJ = j + directions[directionIndex][1];

        // 다음 위치가 범위 내이고 방문하지 않았다면 그 위치로 이동
        if (nextI >= 0 && nextI < matrix.length && nextJ >= 0 && nextJ < matrix[0].length && !visited[nextI][nextJ]) {
            i = nextI;
            j = nextJ;
        } else {
            // 다음 위치가 범위를 벗어나거나, 방문한 경우 방향 변경
            directionIndex = (directionIndex + 1) % 4;
            i += directions[directionIndex][0];
            j += directions[directionIndex][1];
        }

    }

    return orderList;
}

