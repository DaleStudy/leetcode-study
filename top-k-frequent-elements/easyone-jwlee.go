// 풀이
// map으로 입력 숫자들이 각각 몇번 반복되는지 정리
// [][]int를 선언하고 반복된 횟수를 index로, 입력 숫자값을 배열에 append한다.
// 그리고 배열을 역순으로 순회하며 k개의 element를 가진 결과 배열을 만든다.

// TC
// O(n)

// SC
// 모든 숫자가 다르다고 해도 각 숫자는 하나의 하위배열에만 속한다. 따라서 O(n)

func topKFrequent(nums []int, k int) []int {
	m := make(map[int]int)
	for _, num := range nums {
		m[num]++
	}
	a := make([][]int, len(nums)+1)
	for key, num := range m {
		a[num] = append(a[num], key)
	}
	result := make([]int, 0)
	for i := cap(a) - 1; i >= 0; i-- {
		if len(a[i]) > 0 {
			result = append(result, a[i]...)
		}
		if len(result) == k {
			break
		}
	}
	return result
}
