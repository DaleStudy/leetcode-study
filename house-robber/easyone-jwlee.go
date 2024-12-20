// 풀이
// dp를 사용하여 현재 털 수 있는 최대한의 돈을 계산
// curr이 prev가 되고, prev였던 값이 새로운 값을 더한 것과 curr 이었던 값의 최대값을 비교한 것이 새로운 curr이 된다.
// 마지막엔 prev와 curr의 최대값을 비교
// 이렇게 하면 털 수 있는 집의 최대값을 계속 가지고 있을 수 있게 됨.

// TC
// O(n)

// SC
// 늘어나지 않는 int 값만 사용했으므로 O(1)

func rob(nums []int) int {
	length := len(nums)

	if length == 1 {
		return nums[0]
	}

	prev := 0
	curr := nums[0]

	for i := 1; i < length; i++ {
		prev, curr = curr, max(nums[i]+prev, curr)
	}

	return max(prev, curr)
}

func max(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}
