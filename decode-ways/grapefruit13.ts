function numDecodings(s: string): number {
    if (s[0]==="0") return 0;

    const dp = new Array(s.length).fill(0);
    dp[0] = 1;

    for (let i=1; i<s.length; i++) {
        if (s[i] !== "0") {
            dp[i] += dp[i-1];
        }

        const two = Number(s[i-1] + s[i]);

        if (10 <= two && two <= 26) {
            if (i === 1) {
                dp[i] += 1;
            } else {
                dp[i] += dp[i-2];
            }
        }
    }
    return dp[s.length - 1];
};
