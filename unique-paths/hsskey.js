/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {
    let row = new Array(n).fill(1);

    for (let i = 0; i < m - 1; i++) {
        const newRow = new Array(n).fill(1);

        for (let j = n - 2; j >= 0; j--) {
            newRow[j] = newRow[j + 1] + row[j];
        }

        row = newRow;
    }

    return row[0];
};
