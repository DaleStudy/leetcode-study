/**
 * 인코드 된 메세지를 디코드(decode)하려면, 맵핑의 규칙을 반대로 적용하여 숫자를 다시 알파벳 대문자로 돌려놔야 한다.
 * 예를 들어, 숫자 11106은 1 1 10 6으로 분할하면 AAJF로 디코드할 수도 있고, 11 10 6으로 분할하면 KJF로도 디코드할  
   수 있다.
 * 문자열 타입의 숫자가 주어졌을 때 알파벳 문자열로 디코드할 수 있는 방법의 개수를 구하라.
 * @param {string} s
 * @return {number}
 */
var numDecodings = function(s) {
    const memo = new Map();
    memo.set(s.length, 1);

    function dfs(start) {
        if (memo.has(start)) {
        return memo.get(start);
        }

        // 0으로 시작하면 해석 불가
        if (s[start] === "0") {
        memo.set(start, 0);
        return 0;
        }

        let count = dfs(start + 1); // 한 글자 해석

        // 두 글자 해석 가능한 경우
        if (start + 1 < s.length && parseInt(s.substring(start, start + 2)) <= 26) {
        count += dfs(start + 2);
        }

        memo.set(start, count);
        return count;
    }

    return dfs(0);
};
