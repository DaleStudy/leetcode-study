/*
풀이
- house robber 문제와 비슷합니다
  이전 풀이 링크: https://github.com/DaleStudy/leetcode-study/pull/576/files#diff-a98dce0d933d299b3b8e2cc345b95a398c894391b7b86b4b85e3c0aea9d0757f
- 첫번째 집을 터는 경우와 안 터는 경우를 나누어 계산합니다
Big O
- N: 주어진 배열 nums의 길이
- Time complexity: O(N)
- Space complexity: O(1)
*/

import "slices"

func rob(nums []int) int {
	n := len(nums)

	if n < 4 {
		return slices.Max(nums)
	} else if n == 4 {
		return max(nums[0]+nums[2], nums[1]+nums[3])
	}

	// rob nums[0] (can't rob nums[1] and nums[n-1])
	robFirst := nums[0]
	ppRobbed := nums[2] // initial value = nums[2] because we can't rob nums[1]
	pRobbed := nums[3]
	pUnrobbed := nums[2]
	for i := 4; i < n-1; i++ { // i < n-1 because we can't rob nums[n-1]
		ppRobbed, pRobbed, pUnrobbed = pRobbed, nums[i]+max(ppRobbed, pUnrobbed), max(pRobbed, pUnrobbed)
	}
	robFirst += max(pRobbed, pUnrobbed)

	// skip nums[0]
	ppRobbed = nums[1]
	pRobbed = nums[2]
	pUnrobbed = nums[1]
	for i := 3; i < n; i++ {
		ppRobbed, pRobbed, pUnrobbed = pRobbed, nums[i]+max(ppRobbed, pUnrobbed), max(pRobbed, pUnrobbed)
	}
	skipFirst := max(pRobbed, pUnrobbed)

	return max(robFirst, skipFirst)
}

func max(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}
