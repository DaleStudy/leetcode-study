// 주어진 배열을 선형 순회 하므로, 시간 복잡도와 공간 복잡도 모두 O(n)일 것으로 생각합니다.

package week01

// 주어진 배열 nums를 순회하며 준비한 맵에 표시를 하되,
// - 키값에 해당하는 값이 없으면 맵의 해당 키값에 true를 저장하고
// - 키값에 해당하는 값이 있으면 즉시 true를 반환.
// - 순회 후에도 반환하지 않은 경우 중복이 발견되지 않았으므로 false를 반환.
func containsDuplicate(nums []int) bool {
	dup := make(map[int]bool, 0)
	for _, n := range nums {
		if _, ok := dup[n]; !ok {
			dup[n] = true
		} else {
			return true
		}
	}

	return false
}
