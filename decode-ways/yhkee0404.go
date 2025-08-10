func numDecodings(s string) int {
    dp := make([]int, len(s) + 1)
    dp[0] = 1
    const cnt = rune('Z') - rune('A') + 1
    for i, c := range s {
        a := 0
        if i != 0 {
            b := (rune(s[i - 1]) - rune('0')) * 10 + rune(c) - rune('0')
            if b > 9 && b <= cnt {
                a += dp[i - 1]
            }
        }
        b := rune(c) - rune('0')
        if b != 0 && b < cnt {
            a += dp[i]
        }
        dp[i + 1] = a
    }
    return dp[len(s)]
}
