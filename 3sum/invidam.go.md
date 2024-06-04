# Intuition
예전에 풀어봤던 문제였어서 접근법을 알고있었다.

# Approach
1. 정렬을 하여 배열의 대소관계를 일정하게 한다.
2. i,j,k를 설정해야 하는데, i < j < k이도록 한다.
3. i는 맨 앞에서부터 순회한다.
4. j는 i의 뒤부터 순회한다.
5. k는 맨 뒤에서부터 순회한다.
6. 세 인덱스가 가리키는 값들의 합을 비교하여 j와 k를 수정한다.

# Complexity
- Time complexity: $$O(n^2)$$
  - 입력 배열의 길이 n에 대하여, `i`, `j와 k`를 순회한다.

- Space complexity: $$O(n)$$
  - 입력으로 들어온 배열의 길이 n에 대하여, 생성하는 결과 배열의 길이 역시 이와 동일하다.
# Code

```go
func update(i int, j int, k int, sum int, nums []int) (int, int) {
	if sum <= 0 {
		j++
		for j < len(nums) && j >= 1 && nums[j] == nums[j-1] {
			j++
		}
	} else {
		k--
		for k >= 0 && k+1 < len(nums) && nums[k] == nums[k+1] {
			k--
		}
	}

	return j, k
}

func threeSum(nums []int) [][]int {
	var triplets [][]int

	sort.Ints(nums)
	for i := 0; i < len(nums); i++ {
		j, k := i+1, len(nums)-1

		if i != 0 && nums[i-1] == nums[i] {
			continue
		}

		for j < k {
			sum := nums[i] + nums[j] + nums[k]
			if sum == 0 {
				triplets = append(triplets, []int{nums[i], nums[j], nums[k]})
			}
			j, k = update(i, j, k, sum, nums)
		}
	}
	return triplets
}

```