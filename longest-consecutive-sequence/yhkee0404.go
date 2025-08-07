func longestConsecutive(nums []int) int {
    ans := 0
    sort.Ints(nums)
    i := 0
    for i != len(nums) {
        j := i + 1
        k := 0
        for j != len(nums) {
            diff := nums[j] - nums[j - 1]
            if diff > 1 {
                break
            }
            j++
            if diff == 0 {
                k++
            }
        }
        ans = max(ans, j - i - k)
        i = j
    }
    return ans
}
