/**
 * 풀이
 * - 두 정수를 한 bit씩 더하는 방식으로 풀이합니다
 * - 두 정수에 대해 이진 덧셈을 진행할 때, 해당 자리수의 bit 두 개와 carry를 비교하여 새로운 carry와 해당 자리수의 덧셈 결과를 얻을 수 있습니다 -> adder 함수 참고
 * - 각 비트에 대해 adder 함수를 호출하여 덧셈을 진행합니다
 * - res의 특정 자리에 덧셈 결과를 넣어주는 것이 까다로웠는데, position이라는 일종의 bitmask를 사용하여 해결할 수 있었습니다
 * - 저는 Nand2Tetris 라는 책/강의를 보면서 이 전에 bitwise 산술 연산기를 구현한 적이 있었는데, 그 경험이 큰 도움이 되었습니다
 *   궁금하신 분들께 coursera 강의 링크를 첨부합니다 (무료) (https://www.coursera.org/learn/build-a-computer) (2강에 나옴)
 * 
 * Big O
 * - N: a와 b 중 큰 수의 비트 수 <= 32 (c++ 기준)
 * 
 * - Time complexity: O(N <= 32) = O(1)
 * - Space complexity: O(1)
 */

class Solution {
public:
    // returns {carry, result}
    // carry와 result를 아래와 같은 bool 연산으로 표현할 수 있다는 사실은
    // x, y, c에 대하여 벤 다이어그램을 그려보면 쉽게 파악할 수 있습니다
    pair<bool, bool> adder(bool x, bool y, bool c) {
        return {(x & y) | (x & c) | (y & c), x ^ y ^ c};
    }

    int getSum(int a, int b) {
        bool carry = 0;
        unsigned int res = 0;
        unsigned int position = 1;

        // 32 비트 정수 범위 내에서 덧셈을 진행합니다
        // 32 비트 모두 덧셈을 진행했거나, 더 더할 비트가 없다면 루프를 종료합니다
        while (position && (a || b || carry)) {
            bool lsb_a = a & 1;
            a >>= 1;

            bool lsb_b = b & 1;
            b >>= 1;

            auto [new_carry, new_res] = adder(lsb_a, lsb_b, carry);
            
            carry = new_carry;
            if (new_res) res |= position;

            // position이 unsigned int (32비트)이므로
            // bitwise left shift 연산을 32번 수행하면 0이 됨
            // 1000 0000 0000 0000 0000 0000 0000 0000 => 0000 0000 0000 0000 0000 0000 0000 0000
            // position이 0이 되면 32비트 모두 덧셈을 완료했다는 뜻이므로 loop를 종료함
            position <<= 1;
        }

        return (int) res;
    }
};
