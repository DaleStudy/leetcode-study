var numDecodings = function(s) {
    if (s[0] === '0') return 0;

    const n = s.length;
    const dp = new Array(n + 1).fill(0);
    dp[0] = 1; // 빈 문자열. 계단의 첫 시작부분에 1을 넣어주는 것 처럼
    dp[1] = 1; // 첫 글자가 0이 아님은 위에서 확인
    //위 두 값이 기반이 되어 각 자리에 대한 

    for (let i = 2; i <= n; i++) {
        const one = Number(s.slice(i - 1, i));   // 한 글자
        const two = Number(s.slice(i - 2, i));   // 두 글자

        if (one >= 1 && one <= 9) {
            dp[i] += dp[i - 1];
        }
        if (two >= 10 && two <= 26) { //두자리수 일 때는 dp[i-2]도 더해준다.
            dp[i] += dp[i - 2];
        }
        // 각 자리의 값(dp[i])은, 1글자 디코딩 시 바로 전 자리(dp[i-1])의 값과, 2글자 디코딩 시 두 자리 전(dp[i-2])의 값을 더해서 만든다. dp[i]는 도착지의 개념같은 것

    }

    return dp[n];
};

//시간 복잡도: O(n)
//공간 복잡도: O(n)
