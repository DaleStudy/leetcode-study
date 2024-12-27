// 풀이
// result 가장 오른쪽 값에 num의 값을 추가하면서 왼쪽으로 밀어 reverse 처리.

// TC
// for문은 무조건 32회만 돌기때문에 O(1)

// SC
// 추가적인 공간 사용량은 일정하므로 0(1)

func reverseBits(num uint32) uint32 {
	result := uint32(0)
	for i := 0; i < 32; i++ {
		result <<= 1
		if num%2 == 1 {
			result++
		}
		num >>= 1
	}
	return result
}