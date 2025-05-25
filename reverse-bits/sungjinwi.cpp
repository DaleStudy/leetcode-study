/*
    풀이 :
        n & 1 -> n의 오른쪽 첫번째 비트 -> ans에 더한다
        n >> 1 & 1 -> n의 오른쪽 두번째 비트 -> ans를 << 1 해준뒤 더한다
        ...

        n의 오른쪽 끝자리부터 ans에 더해져서 << 연산에 의해 좌측으로 가기 때문에 비트를 뒤집을 수 있다

    TC : O(1)
        32번

    SC : O(1)
s*/

#include <stdint.h>

class Solution {
    public:
        uint32_t reverseBits(uint32_t n) {
            uint32_t ans = 0;
    
            for (int i = 0; i < 32; i++) {
                ans <<= 1;
                ans += n & 1;
                n >>= 1;
            }
            return ans;
        }
    };
