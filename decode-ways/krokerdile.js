/**
 * @param {string} s
 * @return {number}
 */
var numDecodings = function(s) {
    const n = s.length;
    const memo = {};

    function dfs(index) {
        if (index === n) return 1;
        if (s[index] === '0') return 0;
        if (memo.hasOwnProperty(index)) return memo[index];

        let count = dfs(index + 1);
        if (index + 1 < n) {
            const twoDigit = parseInt(s.slice(index, index + 2));
            if (twoDigit >= 10 && twoDigit <= 26) {
                count += dfs(index + 2);
            }
        }

        memo[index] = count;
        return count;
    }

    return dfs(0);
};