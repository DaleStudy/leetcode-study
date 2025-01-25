var uniquePaths = function (m, n) {
    const cache = new Map();

    const dfs = (row, col) => {
        const cacheKey = `${row}-${col}`;

        if (cache.has(cacheKey)) {
            return cache.get(cacheKey);
        }

        if (row === m - 1 && col === n - 1) {
            return 1;
        }

        let count = 0;

        if (row < m - 1) {
            count += dfs(row + 1, col);
        }

        if (col < n - 1) {
            count += dfs(row, col + 1);
        }

        cache.set(cacheKey, count);

        return count;
    }

    return dfs(0, 0);
};

// 시간복잡도 O(m * n)
// 공간복잡도 O(m * n) - 1 (matrix[m][n]에 대한 캐시는 포함되지 않으므로)

var uniquePaths = function(m, n) {
    const matrix = [];

    for (let i=0; i<m; i++) {
        const row = new Array(n).fill(1);
        matrix.push(row);
    }

    for (let j=1; j<matrix.length; j++) {
        for (let k=1; k<matrix[0].length; k++) {
            matrix[j][k] = matrix[j - 1][k] + matrix[j][k - 1];
        }
    }

    return matrix[m - 1][n - 1];
};

// 시간복잡도 O(m * n)
// 공간복잡도 O(m * n)

var uniquePaths = function(m, n) {
    const row = new Array(n).fill(1);

    for (let i=1; i<m; i++) {
        let left = 1;
        
        for (let j=1; j<n; j++) {
            row[j] += left;
            left = row[j];
        }
    }

    return row[n - 1];
};

// 시간복잡도 O(m * n)
// 공간복잡도 (n)
