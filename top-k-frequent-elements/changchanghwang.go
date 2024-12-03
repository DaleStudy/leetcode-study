// Time: O(nlogn)
// Space: O(n)
func topKFrequent(nums []int, k int) []int {
	hashMap := map[int]int{}
	for _, num := range nums {
		hashMap[num]++
	}

	result := [][]int{}

	for key, value := range hashMap {
		result = append(result, []int{key, value})
	}

	sort.Slice(result, func(i, j int) bool { // go의 sort는 quicksort를 기본적으로 사용한다. O(nlogn)
		return result[i][1] > result[j][1]
	})

	resultNums := []int{}
	for i := 0; i < k; i++ {
		resultNums = append(resultNums, result[i][0])
	}

	return resultNums[:k]
}
