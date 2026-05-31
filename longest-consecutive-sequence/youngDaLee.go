package youngDaLee

func longestConsecutive(nums []int) int {
	numSet := make(map[int]bool)
	for _, num := range nums {
		numSet[num] = true
	}

	longestStreak := 0

	for num := range numSet {
		if !numSet[num-1] {
			currentNum := num
			currentStreak := 1

			for numSet[currentNum+1] {
				currentNum++
				currentStreak++
			}

			if currentStreak > longestStreak {
				longestStreak = currentStreak
			}
		}
	}

	return longestStreak
}
