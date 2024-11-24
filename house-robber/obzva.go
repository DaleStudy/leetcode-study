/*
풀이 1
- DP를 이용하여 풀이합니다
  아래 배열 두 개를 이용합니다
  robbed[i]: i번째 집을 털면서 구한 rob(nums[:i+1])의 최대값
  unrobbed[i]: i번째 집을 안 털면서 구한 rob(nums[:i+1])의 최대값
  두 배열을 이용하여 아래와 같은 점화식을 세울 수 있습니다
  robbed[i] = nums[i] + max(robbed[i-2], unrobbed[i-1])
  unrobbed[i] = max(robbed[i-1], unrobbed[i-1])
Big O
- N: nums의 길이
- Time complexity: O(N)
- Space complexity: O(N)
*/

func rob(nums []int) int {
	n := len(nums)

	if n == 1 {
		return nums[0]
	}

	robbed := make([]int, n)
	robbed[0] = nums[0]
	robbed[1] = nums[1]

	unrobbed := make([]int, n)
	unrobbed[1] = nums[0]

	for i := 2; i < n; i++ {
		robbed[i] = nums[i] + max(robbed[i-2], unrobbed[i-1])
		unrobbed[i] = max(robbed[i-1], unrobbed[i-1])
	}

	return max(robbed[n-1], unrobbed[n-1])
}

/*
풀이 2
- 풀이 1과 동일한데, memoization을 위해 배열을 사용하지 않습니다
  robbed[i], unrobbed[i] 계산에는 robbed[i-2], robbed[i-1], unrobbed[i-1]만 있어도 충분하기 때문입니다
Big O
- N: nums의 길이
- Time complexity: O(N)
- Space complexity: O(1)
*/

func rob(nums []int) int {
	n := len(nums)

	if n == 1 {
		return nums[0]
	}

	ppRobbed := nums[0]  // robbed[i-2]에 해당
	pRobbed := nums[1]   // robbed[i-1]에 해당
	pUnrobbed := nums[0] // unrobbed[i-1]에 해당

	for i := 2; i < n; i++ {
		ppRobbed, pRobbed, pUnrobbed = pRobbed, nums[i]+max(ppRobbed, pUnrobbed), max(pRobbed, pUnrobbed)
	}

	return max(pRobbed, pUnrobbed)
}

func max(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}
