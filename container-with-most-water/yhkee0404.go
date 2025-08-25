func maxArea(height []int) int {
    ans := 0
    i, j := 0, len(height) - 1
    for i < j { 
        dh := height[i] - height[j]
        dx := j - i
        k := j
        if dh == 0 {
            i++
            j--
        } else if dh > 0 {
            j--
        } else {
            k = i
            i++
        }
        ans = max(ans, dx * height[k])
    }
    return ans
}