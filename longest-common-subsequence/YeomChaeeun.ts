/**
 * 가장 긴 공통 부분 수열 구하기
 * 알고리즘 복잡도
 * - 시간 복잡도: O(m*n)
 * - 공간 복잡도: O(m*n)
 * @param text1
 * @param text2
 */
function longestCommonSubsequence(text1: string, text2: string): number {
    let dp: number[][] = Array(text1.length + 1).fill(0)
        .map(() => Array(text2.length + 1).fill(0));

    for(let i = 1; i <= text1.length; i++) {
        for(let j = 1; j <= text2.length; j++) {
            if(text1[i-1] === text2[j-1]) {
                dp[i][j] = dp[i-1][j-1] + 1;
            } else {
                dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
            }
        }
    }

    return dp[text1.length][text2.length];
}
