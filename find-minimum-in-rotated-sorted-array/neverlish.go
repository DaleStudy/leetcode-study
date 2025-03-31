// 시간복잡도: O(n)
// 공간복잡도: O(1)

func findMin(nums []int) int {
	result := nums[0]

	for i := 1; i < len(nums)-1; i++ {
		if nums[i] < nums[i-1] {
			result = nums[i]
		}
	}
	return result

}
