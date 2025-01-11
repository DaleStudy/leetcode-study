/**
 * 주어진 문자열이 단어 사전에 있는 단어들로 나누어질 수 있는지 확인합니다.
 * 
 *
 * @param {string} s - 확인할 문자열
 * @param {string[]} wordDict - 단어 사전
 * @returns {boolean} 문자열이 단어로 완벽히 나누어질 수 있으면 `true`, 아니면 `false`
 * 
 * 시간 복잡성 O(n * m * k)
 *  - n: 문자열 s 길이
 *  - m: 단어 사전 길이
 *  - k: 단어 사전 내 단어 길이
 * 
 * 공간 복잡성 O(n)
 *  - 메모이제이션(memo) 및 재귀 호출 스택 크기가 문자열 길이 n에 비례.
 */
function wordBreak(s: string, wordDict: string[]): boolean {
    const memo: Record<number, boolean> = {};

    /**
     * @param {number} start - 현재 시작 idx
     * @returns {boolean} 주어진 idx 부터 문자열을 나눌 수 있으면 true
     */
    const dfs = (start: number): boolean => {
        if (start in memo) return memo[start];
        if (start === s.length) return (memo[start] = true);

        for (const word of wordDict) {
            if (s.startsWith(word, start) && dfs(start + word.length)) {
                return (memo[start] = true);
            }
        }

        return (memo[start] = false);
    };

    return dfs(0);
}

