func isAnagram(s string, t string) bool {
    sRune := []rune(s)
    tRune := []rune(t)
    sort.Slice(sRune, func(i, j int) bool {
        return sRune[i] < sRune[j]
    })
    sort.Slice(tRune, func(i, j int) bool {
        return tRune[i] < tRune[j]
    })
    return string(sRune) == string(tRune)
}
