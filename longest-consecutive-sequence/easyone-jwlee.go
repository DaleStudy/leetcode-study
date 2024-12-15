// 풀이
// You must write an algorithm that runs in O(n) time.
// TC를 O(n) 이내로 해야한다는 것은 sort를 쓰지 말라는 의미.
// map을 사용하고 순회하며 연속이 시작되는 값을 찾고 찾으면 연속되는지 찾기.

// TC
// 순회하는 map안에서 for문을 또 호출하긴 하지만,
// 모든 값이 연속되는 값이라고 했을 때
// 연속이 시작되는 값 외에는 한 번씩 바로 지나가게 되고(n*1), 시작되는 값부터 연속이 끝나는 시점까지 n번이라(1*n)
// O(n+n) 이기 때문에 TC는 O(n)

// SC
// map이 최대로 차지하는 공간은 O(n)

func longestConsecutive(nums []int) int {
	m := make(map[int]bool)
	for _, num := range nums {
		m[num] = true
	}
	length := 1
	maxLength := 0
	for k := range m {
		if _, ok := m[k-1]; !ok {
			i := 1
			for {
				if _, ok := m[k+i]; ok {
					length++
					i++
				} else {
					break
				}
			}
			if maxLength < length {
				maxLength = length
			}
			length = 1
		}
	}
	return maxLength
}
