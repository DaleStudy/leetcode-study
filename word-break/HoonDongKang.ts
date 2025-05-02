/**
 * [Problem]: [139] Word Break
 * (https://leetcode.com/problems/word-break/description/)
 */
function wordBreak(s: string, wordDict: string[]): boolean {
    //시간복잡도: O(n^2)
    //공간복잡도: O(n)
    function dfsFunc(s: string, wordDict: string[]): boolean {
        let wordSet = new Set(wordDict);
        let memo = new Map<number, boolean>();

        function dfs(start: number): boolean {
            if (start === s.length) return true;
            if (memo.has(start)) return memo.get(start)!;

            for (let end = start + 1; end <= s.length; end++) {
                const word = s.slice(start, end);

                if (wordSet.has(word) && dfs(end)) {
                    memo.set(start, true);
                    return true;
                }
            }

            memo.set(start, false);
            return false;
        }

        return dfs(0);
    }

    //시간복잡도: O(n^2)
    //공간복잡도: O(n)
    function dpFunc(s: string, wordDict: string[]): boolean {
        const wordSet = new Set(wordDict);
        const dp = new Array(s.length + 1).fill(false);
        dp[0] = true;

        for (let end = 1; end <= s.length; end++) {
            for (let start = 0; start < end; start++) {
                const isExists = wordSet.has(s.slice(start, end));
                if (isExists && dp[start]) {
                    dp[end] = true;
                    break;
                }
            }
        }
        return dp[s.length];
    }
    return dpFunc(s, wordDict);
}
