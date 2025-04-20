/**
 * 주어진 문자열을 복호화하는 경우의 수를 반환하는 함수
 * @param {string} s
 * @return {number}
 */
const numDecodings = function(s) {
    const dp = {};

    function decode(idx) {
        if (s[idx] === '0') {
            return 0;
        }

        if (idx === s.length) {
            return 1;
        }

        if (dp[idx]) {
            return dp[idx];
        }

        let result = 0;
        result += decode(idx + 1); // 현재 문자만 쓰는 경우: 다음 문자부터 탐색
        if (s[idx + 1] && Number(s[idx] + s[idx+1]) <= 26) {
            result += decode(idx + 2); // 현재 문자와 다음 문자 붙여서 쓰는 경우: 다다음 문자부터 탐색
        }

        dp[idx] = result;
        return result;
    }

    return decode(0);
};

// 시간복잡도: O(n) (메모이제이션 안하면 매 인덱스마다 최대 2개의 하위 호출이 발생하여 O(2^n))
// 공간복잡도: O(n)
