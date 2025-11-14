package youngDaLee

func twoSum(nums []int, target int) []int {
	numMap := make(map[int]int)
	for i, num := range nums {
		sub := target - num
		if j, exists := numMap[sub]; exists {
			return []int{j, i}
		}
		numMap[num] = i
	}

	return []int{}
}
