func countSubstrings(s string) int {
    runes := []rune{} // S(n) = O(n)
    for _, c := range s {
        runes = append(runes, c)
        runes = append(runes, '\000')
    }
    ans := 0
    dp := make([]int, len(runes) - 1)
    lastR := -1
    lastMid := -1
    i := 0
    for i != len(dp) { // Manacher T(n) = O(n)
        diff := lastR - i
        deviation := 0
        if diff > 0 {
            deviation = min(diff, dp[lastMid - (i - lastMid)])
        }
        l := i - deviation
        r := i + deviation
        for l != 0 && r + 1 != len(dp) && runes[l - 1] == runes[r + 1] {
            deviation++
            l--
            r++
        }
        dp[i] = deviation
        if r > lastR {
            lastR = r
            lastMid = i
        }
        if runes[i] == '\000' {
            ans += (deviation + 1) >> 1
        } else {
            ans += 1 + (deviation >> 1)
        }
        i++
    }
    return ans
}
