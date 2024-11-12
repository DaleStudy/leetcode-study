/*
풀이
- 원본 uint32 num에 대하여 LSB부터(가장 오른쪽 bit) 탐색합니다
  LSB % 2 == 1 -> uint32의 새로운 MSB에(가장 왼쪽 bit) 1 추가
		else   ->                                 0 추가
Big O
- Time complexity: O(1)
  - input num에 상관 없이 32번의 반복을 고정적으로 실행합니다
- Space complexity: O(1)
*/

func reverseBits(num uint32) uint32 {
    var res uint32 = 0
    for i := 0; i < 32; i++ {
		// using numerical operators
		// if num % 2 == 1 {
        //     res = res * 2 + 1
        // } else {
        //     res *= 2
        // }
        // num /= 2

		// using bitwise operators
		res = (res << 1) | (num & 1)
		num >>= 1
    }

    return res
}