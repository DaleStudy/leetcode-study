#include <iostream>

class Solution {
	public:
		uint32_t reverseBits(uint32_t n) {
			unsigned int reverse = 0;
			for (int i = 0; i < 32; i++) {
				reverse <<= 1; // 한 비트를 왼쪽으로 당겨서 공간을 만들고
				reverse |= (n & 1); // n의 최하위 비트를 reverse의 최하위 비트에 저장
				n >>= 1; // n의 다음 비트를 최하위 비트로 당겨온다
			}
            return (reverse);
	}
};
