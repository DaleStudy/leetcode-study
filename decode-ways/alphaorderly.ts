function numDecodings(s: string): number {
    const N = s.length;

    if (s[0] == '0') return 0

    let dp = Array(N).fill(0)
    dp[0] = 1

    for (let i = 1;i < N;i += 1) {

        if(s[i] == '0') {
            if (s[i - 1] == '0') return 0
            if (s[i - 1] > '2') return 0

            dp[i] += i == 1 ? 1 : dp[i - 2]
            continue
        }

        dp[i] += dp[i - 1]
        if (s[i - 1] === '1' || (s[i - 1] === '2' && s[i] <= '6')) {
            dp[i] += i == 1 ? 1 : dp[i - 2]
        }
    }

    console.log(dp)

    return dp[dp.length - 1]
};
