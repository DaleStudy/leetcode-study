/*
풀이 1
- 아래와 같은 memo 배열을 만들어서 풀이할 수 있습니다 (참고: Kadane's Algorithm)
  memo[i] = nums[:i] 중에서 nums[i]를 반드시 포함하는 부분 배열의 최대 합

Big O
- N: 주어진 배열 nums의 길이
- Time complexity: O(N)
- Space complexity: O(N)
*/

func maxSubArray(nums []int) int {
	n := len(nums)

	memo := make([]int, n)
	copy(memo, nums)

	maxSum := nums[0]

	for i := 1; i < n; i++ {
		if memo[i-1] > 0 {
			memo[i] += memo[i-1]
		}

		if maxSum < memo[i] {
			maxSum = memo[i]
		}
	}

	return maxSum
}

/*
풀이 2
- 알고리즘의 전개 과정을 보면 O(N)의 공간복잡도를 갖는 memo가 필요하지 않다는 걸 알 수 있습니다
- memo 배열 대신 현재 계산 중인 부분 배열의 합만 계속 갱신합니다

Big O
- N: 주어진 배열 nums의 길이
- Time complexity: O(N)
- Space complexity: O(1)
*/

func maxSubArray(nums []int) int {
    maxSum, currSum := nums[0], nums[0]

    for i := 1; i < len(nums); i++ {
        if currSum > 0 {
            currSum += nums[i]
        } else {
            currSum = nums[i]
        }
        
        if maxSum < currSum {
            maxSum = currSum
        }
    }

    return maxSum
}
