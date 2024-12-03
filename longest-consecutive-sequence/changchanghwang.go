// time complexity: O(n)
// space complexity: O(n)
// 풀이
// 1. map에 nums의 모든 요소를 저장한다.
// 2. map을 순회하면서 num-1이 존재하는지 확인한다.
// 3. num-1이 존재하면 continue
// 4. num-1이 존재하지 않으면 consecutiveCount를 1로 초기화하고 num+1이 존재하는지 (연속적으로 숫자가 증가하는게 있는지) 확인한다.
// 5. num+1이 존재하면 consecutiveCount를 1 증가시키고 num을 1 증가시켜 다음 수를 찾는다.
// 6. num+1이 존재하지 않으면 현재까지의 consecutiveCount와 maxConsecutiveCount를 비교하여 maxConsecutiveCount를 갱신한다.
func longestConsecutive(nums []int) int {
	numMap := make(map[int]bool)

	for _, num := range nums {
		numMap[num] = true
	}

	maxConsecutiveCount := 0

	for num := range numMap {
		if numMap[num-1] {
			continue
		}
		consecutiveCount := 1
		for numMap[num+1] {
			num++
			consecutiveCount++
		}
		if consecutiveCount > maxConsecutiveCount {
			maxConsecutiveCount = consecutiveCount
		}
	}

	return maxConsecutiveCount
}