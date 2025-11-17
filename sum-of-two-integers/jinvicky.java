class Solution {
    public int getSum(int a, int b) {
        while (b != 0) {

            // 변수 2개와 비트 연산
            // 1.
            int sum = a ^ b;

            // 2.
            int carry = (a & b) << 1;

            /// 3.
            a = sum;
            b = carry; // 한번하고 말면 b는 쓰일 일이 없는데? -> 빠뜨린 반복문이 없는지 확인한다.

        }
        return a;
    }
}
