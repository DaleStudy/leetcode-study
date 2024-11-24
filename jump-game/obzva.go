/*
풀이 1
- memo 배열을 이용하여 n-1번째 인덱스부터 0번째 인덱스 방향으로 탐색하여 풀이할 수 있습니다
  memo[i] = i번째 인덱스에서 출발했을 때 마지막 인덱스에 도달할 수 있는지 여부

Big O
- N: 주어진 배열 nums의 길이
- Time complexity: O(N)
- Space complexity: O(N)
  - 풀이 2를 이용하면 O(1)으로 최적화할 수 있습니다
*/

func canJump(nums []int) bool {
	n := len(nums)

	if nums[0] == 0 && n > 1 {
		return false
	}

	memo := make([]bool, n)
	memo[n-1] = true

	for i := n - 2; i >= 0; i-- {
		for j := 1; j <= nums[i]; j++ {
			if i+j >= n {
				break
			}
			if memo[i+j] {
				memo[i] = true
				break
			}
		}
	}

	return memo[0]
}

/*
풀이
- 풀이 1을 잘 관찰하면 memo배열의 모든 값을 가지고 있을 필요가 없다는 걸 알 수 있습니다
  memo 배열 대신에, 문제의 조건대로 마지막 인덱스까지 갈 수 있는 가장 좌측의 인덱스만 기록합니다 (leftmost)

Big O
- N: 주어진 배열 nums의 길이
- Time complexity: O(N)
- Space complexity: O(1)
*/

func canJump(nums []int) bool {
	n := len(nums)

	if nums[0] == 0 && n > 1 {
		return false
	}

	leftmost := n - 1

	for i := n - 2; i >= 0; i-- {
		if i+nums[i] >= leftmost {
			leftmost = i
		}
	}

	return leftmost == 0
}
