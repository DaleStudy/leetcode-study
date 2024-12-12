package contains_duplicate

import "sort"

/*
1. 문제

	주어진 int 배열 nums에 숫자가 중복되는 경우가 한 번이라도 있으면 true, 그렇지 않으면 false 를 리턴

2. 풀이

	고유값만 저장하는 set(go 에서는 map)의 성질을 활용하여
	nums를 순회하며 set에 값이 있는지 없는지 체크하여
	숫자가 중복되는 경우를 체크

3. 분석
  - 시간 복잡도: O(N)
    nums 탐색: O(N)
    배열 nums의 모든 원소를 단 한 번 순회
    map 삽입, 탐색: O(1)
    map의 내부 구현은 해시 테이블.
    O(N)보다 작아 무시됨
  - 공간 복잡도: O(N)
    최악의 경우라도 사용공간은 nums 의 크기만큼 + nums의 모든 원소를 포함한 map
*/
func containsDuplicate(nums []int) bool {
	seen := map[int]int{}

	for _, n := range nums {
		if _, ok := seen[n]; ok {
			return true
		}

		seen[n] = 1
	}

	return false
}

func containsDuplicate_SortedApproach(nums []int) bool {
	// early exit for small slices
	if len(nums) < 2 {
		return false
	}

	// sort in ascending order and check adjacent elements
	sort.Ints(nums)
	for i := 1; i < len(nums); i++ {
		if nums[i] == nums[i-1] {
			return true
		}
	}

	return false
}
