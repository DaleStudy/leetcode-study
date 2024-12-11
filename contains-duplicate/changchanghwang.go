// Time complexity, O(n)
// Space complexity, O(n)
// 풀이
// nums 배열을 순회하면서 hashMap에 num을 key로, 존재 여부를 value로 저장한다.
// 만약 이미 존재하는 key라면 true를 반환하고, 순회를 전부 했는데도 중복이 없다면 false를 반환한다.
func containsDuplicate(nums []int) bool {
	hashMap := map[int]bool{}
	for _, num := range nums {
		if hashMap[num] {
			return true
		} 
		hashMap[num] = true
	}
	return false
}
