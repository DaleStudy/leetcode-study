// Time complexity: O(n)
// Space complexity: O(n)
func topKFrequent(nums []int, k int) []int {
	countByNum := map[int]int{}
	numsByCount := map[int][]int{}
	max := 0

	for _, num := range nums {
		countByNum[num]++
		if countByNum[num] > max {
			max = countByNum[num]
		}
	}

	for num, count := range countByNum {
		if _, ok := numsByCount[count]; ok {
			numsByCount[count] = append(numsByCount[count], num)
		} else {
			numsByCount[count] = []int{num}
		}
	}

	result := []int{}
	for i := max; i >= 0; i-- {
		nums := numsByCount[i]
		result = append(result, nums...)
		if len(result) >= k {
			break
		}
	}

	return result[:k]
}
