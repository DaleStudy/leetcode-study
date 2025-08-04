func twoSum(nums []int, target int) []int {
    indices := make(map[int]int)
    for i, num := range nums {
        j, ok := indices[target - num]
        if ok {
            return []int{j, i}
        }
        indices[num] = i
    }
    return []int{}
}
