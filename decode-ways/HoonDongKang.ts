/**
 * [Problem]: [91] Decode Ways
 *
 * (https://leetcode.com/problems/decode-ways/description/)
 */
function numDecodings(s: string): number {
    //시간복잡도 O(n)
    //공간복잡도 O(n)
    function memoizationFunc(s: string): number {
        const memoization: Record<number, number> = {};

        function dfs(index: number): number {
            if (index in memoization) return memoization[index];
            if (index === s.length) return 1;
            if (s[index] === "0") return 0;

            let result = dfs(index + 1);
            if (index + 1 < s.length && +s.slice(index, index + 2) <= 26) {
                result += dfs(index + 2);
            }

            memoization[index] = result;
            return result;
        }

        return dfs(0);
    }

    //시간복잡도 O(n)
    //공간복잡도 O(1)
    function optimizedFunc(s: string): number {
        let prev2 = 1;
        let prev1 = s[0] === "0" ? 0 : 1;

        for (let i = 1; i < s.length; i++) {
            let curr = 0;

            const one = +s.slice(i, i + 1);
            const two = +s.slice(i - 1, i + 1);

            if (one >= 1 && one <= 9) curr += prev1;
            if (two >= 10 && two <= 26) curr += prev2;

            prev2 = prev1;
            prev1 = curr;
        }

        return prev1;
    }
    return optimizedFunc(s);
}
