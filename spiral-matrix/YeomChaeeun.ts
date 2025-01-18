/**
 * 달팽이 알고리즘
 * 알고리즘 복잡도
 * - 시간 복잡도: O(n) - 모든 행렬의 원소의 수 (rows * columns)
 * - 공간 복잡도: O(n) - 결과 저장을 위한 배열
 * @param matrix
 */
function spiralOrder(matrix: number[][]): number[] {
    // 정처기 단골 문제였던 기억이..
    const result: number[] = [];
    let top = 0
    let bottom = matrix.length - 1;
    let left = 0
    let right = matrix[0].length - 1;

    while(top <= bottom && left <= right) { // 순환 조건
        for(let i = left; i <= right; i++) {
            result.push(matrix[top][i])
        }
        top++

        for(let i = top; i <= bottom; i++) {
            result.push(matrix[i][right])
        }
        right--

        if(top <= bottom) {
            for(let i = right; i >= left; i--) {
                result.push(matrix[bottom][i])
            }
            bottom--
        }

        if(left <= right) {
            for(let i = bottom; i >= top; i--) {
                result.push(matrix[i][left])
            }
            left++
        }
    }

    return result
}
