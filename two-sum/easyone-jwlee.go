// 풀이
// map의 key에 값, value에 index를 넣어, target-num이 map에 존재할 때를 찾기.
// 오직 하나의 답만 무조건 존재한다고 했기 때문에 찾자마자 return.

// TC
// 가장 마지막 인덱스까지 가서야 값을 구할 수 있었다고 하면, nums의 길이만큼 for문을 한바퀴 돌기때문에 O(n).

// SC
// 중복없이 마지막 인덱스까지 가서 값을 구한다면 들어오는 nums의 길이만큼 map도 공간을 차지하게 되므로 O(n).

func twoSum(nums []int, target int) []int {
	m := make(map[int]int)
	for i, num := range nums {
		if index, ok := m[target-num]; ok {
			return []int{index, i}
		}
		m[num] = i
	}
	return []int{0, 0}
}
