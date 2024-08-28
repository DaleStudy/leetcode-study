func countBits(n int) []int {
	var result []int = make([]int, n+1)
	var offset int = 1
	for i := 1; i <= n; i++ {
		if i == offset*2 {
			offset = offset * 2
		}
		result[i] = 1 + result[i-offset]
	}
	return result
}
