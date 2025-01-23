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

