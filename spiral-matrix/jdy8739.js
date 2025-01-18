/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    let top = 0;
    let left = 0;
    let bottom = matrix.length - 1;
    let right = matrix[0].length - 1;

    const answer = [];

    while (top <= bottom && left <= right) {
        for (let i = left; i <= right; i++) {
            answer.push(matrix[top][i]);
        }
        top++;

        if (top > bottom) {
            break;
        }

        for (let j = top; j <= bottom; j++) {
            answer.push(matrix[j][right]);
        }
        right--;

        if (left > right) {
            break;
        }

        for (let k = right; k >= left; k--) {
            answer.push(matrix[bottom][k]);
        }
        bottom--;

        for (let l = bottom; l >= top; l--) {
            answer.push(matrix[l][left]);
        }
        left++;
    }

    return answer;
};

// 시간 복잡도 O(m * n)
// 공간 복잡도 O(1)