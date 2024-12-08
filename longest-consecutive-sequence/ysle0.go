package longest_consecutive_sequence

import "slices"

/*
 1. 문제
    주어진 int 배열 nums에서 찾을 수 있는 가장 긴 연속된 원소의 길이 구하기

 2. 풀이
    모든 수의 중복을 제거하고, 오름차순으로 정렬하여 연속된 원소의 부분을 찾기 위해서
    배열을 순회하여 인덱스 고정~전진하며 다음 원소가 연속된 원소인지 체크를 반복

3. 분석

  - 시간 복잡도: O(N logN)
    배열 정렬 O(N logN)
    중복된 원소를 제거해주는 slices.Compact(nums): O(N)
    2중 포문은 for 문 순회 index 를 같이 쓰므로 O(N)

  - 공간 복잡도: O(N)
*/
func longestConsecutive(nums []int) int {
	if len(nums) == 0 {
		return 0
	}

	if len(nums) == 1 {
		return 1
	}

	slices.Sort(nums)
	nums = slices.Compact(nums)
	// 중복을 제거하고 나서도 1개면 최장연속수는 1
	if len(nums) == 1 {
		return 1
	}

	cons := map[int]int{}
	cursor := 0
	for cursor < len(nums)-1 {
		cons[cursor] = 1
		wasConsecutive := false

		// cursor 는 고정하고, innerCursor 를 돌림
		innerCursor := cursor
		for innerCursor+1 < len(nums) &&
			nums[innerCursor]+1 == nums[innerCursor+1] {

			cons[cursor]++
			innerCursor++
			wasConsecutive = true
		}

		if wasConsecutive {
			cursor = innerCursor
		}
		cursor++
	}

	//tmp := make([]int, 0, len(cons))
	tmp := make([]int, 0, len(cons))
	for _, v := range cons {
		tmp = append(tmp, v)
	}

	slices.SortFunc(
		tmp,
		func(a, b int) int {
			return b - a
		})
	return tmp[0]
}
