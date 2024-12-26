// time complexity: O(n)
// space complexity: O(1)
// prefix와 postfix를 이용하여 계산
// 예를 들어, [1, 2, 3, 4] 일 때,
// prefix는 [1, 1, 2, 6] 이고 postfix는 [24, 12, 4, 1] 이다.
// 그리고 서로 곱하면 [24, 12, 8, 6] 이 된다.
func productExceptSelf(nums []int) []int {
	res := make([]int, len(nums))
	for i := range res {
		res[i] = 1
	}

	prefix := 1
	for i := 0; i < len(nums); i++ {
		res[i] = prefix
		prefix *= nums[i]
	}

	postfix := 1
	for i := len(nums) - 1; i >= 0; i-- {
		res[i] *= postfix
		postfix *= nums[i]
	}

	return res
}