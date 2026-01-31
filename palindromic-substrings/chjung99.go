func countSubstrings(s string) int {
    ans := 0
    n := len(s)

    for i := 0; i < n; i++ {
        for j := i+1; j <= n; j++ {
            if (isPalindrom(s[i:j])) {
                ans++
            }
        }
    }
    return ans
}

func isPalindrom(s string) bool {
    var rev []byte
    n := len(s)
    for i := n-1; i >= 0; i-- {
        rev = append(rev, s[i])
    }
    return string(rev) == s
}


