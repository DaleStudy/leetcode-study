// Time: O(nlogn)
// Space: O(n)
// 풀이
// hashMap에 num을 key로, count를 value로 저장한다.
// hashMap을 배열로 만들어 count순으로 정렬한다.
// 정렬된 배열에서 앞에서부터 k개만 뽑아내서 반환한다.
func topKFrequent(nums []int, k int) []int {
	hashMap := map[int]int{}
	for _, num := range nums {
		hashMap[num]++
	}

	result := [][]int{}

	for num, count := range hashMap {
		result = append(result, []int{num, count})
	}

	sort.Slice(result, func(i, j int) bool { // go의 sort는 quicksort를 기본적으로 사용한다. O(nlogn)
		return result[i][1] > result[j][1]
	})

	resultNums := make([]int, 0, k)
	for i := 0; i < k; i++ {
		resultNums = append(resultNums, result[i][0])
	}

	return resultNums
}
