class Solution {
    public int getSum(int a, int b) {
        /**
        1.operator 을 쓰지않고 two sum 구하는 문제
        2.constraints
        - without using operators + and -
        - value min = -1000, max = 1000
        3.solution
        -bit 연산
         */
         while (b != 0) {
            int carry = (a & b) << 1; // 자리 올림
            a = a ^ b;                // 자리 올림 없는 합
            b = carry;                // 다음에 더할 carry
        }
        return a;
    }
}
