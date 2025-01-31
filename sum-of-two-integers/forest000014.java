/*
# Time Complexity: O(n)
# Space Complexity: O(1)

음...... bit manipulation을 최대한 활용해서 했습니다.
이진법의 덧셈/뺄셈을 손으로 계산한다면, carry/borrow 개념을 활용해서 수행할 텐데, 이 과정을 그대로 코드로 옮겨보았습니다.
++은 increment operator이고, -는 unary minus operator로만 썼으니, 문제의 조건인 +, - operator를 쓰지 말라는 제약사항은 지켰다고 주장하고 싶습니다.
그런데 이렇게 지저분하게 구현하는 것은 출제자의 의도에 부합하지 않는 것 같네요. Dale님의 풀이를 보니 훨씬 간결하던데, 좀 더 공부해봐야 할 것 같습니다.
*/

class Solution {
    public int getSum(int a, int b) {
        if (a >= 0 && b >= 0) {
            return sum(a, b);
        } else if (a <= 0 && b <= 0) {
            return -sum(-a, -b);
        } else if (a < 0) {
            if (-a >= b) {
                return -subtract(-a, b);
            } else {
                return subtract(b, -a);
            }
        } else {
            if (a >= -b) {
                return subtract(a, -b);
            } else {
                return -subtract(-b, a);
            }
        }
    }

    public int sum(int a, int b) {
        int sum = 0;
        int carry = 0;
        int bit = 0;
        int digit = 0;

        while (a > 0 || b > 0) {
            if (((a & 1) & (b & 1) & (carry & 1)) == 1) {
                carry = 1;
                bit = 1;
            } else if (((a & 1) | (b & 1) | (carry & 1)) == 1) {
                if (((a & 1) ^ (b & 1) ^ (carry & 1)) == 0) {
                    carry = 1;
                    bit = 0;
                } else {
                    carry = 0;
                    bit = 1;
                }
            } else {
                carry = 0;
                bit = 0;
            }

            sum |= (bit << digit);

            a >>= 1;
            b >>= 1;
            digit++;
        }

        if (carry == 1) {
            sum |= (1 << digit);
        }

        return sum;
    }

    public int subtract(int a, int b) {
        int sub = 0;
        int borrow = 0;
        int bit = 0;
        int digit = 0;

        while (a > 0) {
            if (borrow == 1) {
                if ((a & 1) == (b & 1)) {
                    borrow = 1;
                    bit = 1;
                } else if ((a & 1) == 1) {
                    borrow = 0;
                    bit = 0;
                } else {
                    borrow = 1;
                    bit = 0;
                }
            } else {
                if ((a & 1) == (b & 1)) {
                    borrow = 0;
                    bit = 0;
                } else if ((a & 1) == 1) {
                    borrow = 0;
                    bit = 1;
                } else {
                    borrow = 1;
                    bit = 1;
                }
            }

            sub |= (bit << digit);

            digit++;
            a >>= 1;
            b >>= 1;
        }

        return sub;
    }
}
