func topKFrequent(nums []int, k int) []int {
	m := make(map[int]int)
	for _, num := range nums {
		m[num]++
	}
	a := make([][]int, len(nums)+1)
	for key, num := range m {
		a[num] = append(a[num], key)
	}
	result := make([]int, 0)
	for i := cap(a) - 1; i >= 0; i-- {
		if len(a[i]) > 0 {
			result = append(result, a[i]...)
		}
		if len(result) == k {
			break
		}
	}
	return result
}
