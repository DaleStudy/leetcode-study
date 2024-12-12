// 풀이
// map으로 중복된 값이 있는지 체크

// TC
// 중복이 하나도 없는 경우에 최대 n번 조회
// n번 반복시 총 작업의 복잡도는 O(n)

// SC
// n개의 숫자를 저장하면 map이 사용하는 공간은 최대 O(n)

// (+) 정렬을 사용한다면?
// 입력된 배열을 정렬해서 서로 인접한 값을 비교하면 O(1)의 SC로 중복 확인 가능.
// 그러나 정렬을 사용하면 TC가 O(nlogn).

func containsDuplicate(nums []int) bool {
	m := make(map[int]int)
	for _, num := range nums {
		if _, ok := m[num]; ok {
			return true
		}
		m[num] = num
	}
	return false
}
