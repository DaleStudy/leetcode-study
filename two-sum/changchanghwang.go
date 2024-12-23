// Time: O(n)
// Space: O(n)
func twoSum(nums []int, target int) []int {
	m := make(map[int]int)

	// O(n)
	for i, num := range nums {
		// O(1)
		if j, ok := m[target-num]; ok && j != i { // target = num2 + num1 -> num2 = target - num1 을 이용하여 두 수를 찾는다.
			return []int{j, i}
		}
		m[num] = i // 없다면 현재 수를 키로 하여 인덱스를 저장한다.
	}
	return nil
}
