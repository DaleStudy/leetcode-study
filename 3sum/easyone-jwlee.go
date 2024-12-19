// 풀이
// 배열을 정렬하고
// two pointer 사용

// TC
// 정렬 O(nlogn) + Two pointer 이중 루프 O(n^2) = O(n^2)

// SC
// Go의 sort.Ints()는 TimSort를 사용.
// Merge Sort와 Insertion Sort의 조합으로 동작.
// 정렬 O(n) + Two pointer O(1) + 결과 배열 O(n) = O(n)

func threeSum(nums []int) [][]int {
	result := [][]int{}
	sort.Ints(nums) // nums를 정렬

	for i := 0; i < len(nums)-2; i++ {
		if i > 0 && nums[i] == nums[i-1] {
			continue // 중복된 값 건너뜀
		}

		left, right := i+1, len(nums)-1
		for left < right {
			sum := nums[i] + nums[left] + nums[right]
			if sum == 0 {
				result = append(result, []int{nums[i], nums[left], nums[right]})
				left++
				right--

				// 중복 제거
				for left < right && nums[left] == nums[left-1] {
					left++
				}
				for left < right && nums[right] == nums[right+1] {
					right--
				}
			} else if sum < 0 {
				left++
			} else {
				right--
			}
		}
	}

	return result
}
