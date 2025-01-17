/**
 * 문자열에서 substring 중 panlindrome인 경우의 수를 구하는 함수
 * @param {string} s - 입력 문자열 
 * @returns {number}  -  s문자열에서 찾을수 있는 panlindrome substring의 개수
 * 
 * 시간 복잡도: O(n^2) (n: 문자열 길이)
 *   - 한 번의 외부 루프: 부분 문자열 길이 (\(subLen\)) - O(n)
 *   - 내부 루프: 시작 인덱스 (\(start\)) - O(n)
 *   - 따라서, 총 복잡도는 O(n^2)
 * 
 * 공간 복잡도: O(n^2)
 * - DP 배열 dp[i][j]는 \(n^2\) 크기를 가지며 문자열의 모든 시작과 끝 조합에 대한 정보를 저장합니다.
 */
function countSubstrings(s: string): number {
    const n = s.length; // 문자열 길이
    let result = 0;

    // DP 배열 생성 (dp[i][j] 는 s[i] ~ s[j] 까지가 회문인지 여부를 저장)
    const dp: boolean[][] = Array.from({ length: n }, () => Array(n).fill(false));

    // 1글자 경우
    for (let i = 0; i < n; i++) {
        dp[i][i] = true;
        result++;
    }

    // 2글자 경우
    for (let i = 0; i < n - 1; i++) {
        if (s[i] === s[i + 1]) {
            dp[i][i + 1] = true;
            result++;
        }
    }

    // 3글자 이상인 경우
    for (let subLen = 3; subLen <= n; subLen++) {
        for (let start = 0; start <= n - subLen; start++) {
            const end = start + subLen - 1;
            // 양 끝 문자가 같고, 내부 부분 문자열이 회문이면 true
            if (s[start] === s[end] && dp[start + 1][end - 1]) {
                dp[start][end] = true;
                result++;
            }
        }
    }

    return result;
}
