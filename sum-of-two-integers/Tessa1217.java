/** +, - 부호 쓰지 않고 두 수의 합 구하기 */
class Solution {

    // 비트 연산으로 계산 수행
    public int getSum(int a, int b) {
        while (b != 0) {
            // 왼쪽 쉬프트하여 자리 올림에 대한 계산 수행
            int bit = (a & b) << 1;
            // XOR 연산으로 자리 올림 없는 덧셈 수행
            a = a ^ b;
            b = bit;
        }
        return a;
    }

    /**
     * 풀리기는 하지만, 이런 식은 편법일 것 같은...?
     * Class Integer 내부에 sum 연산: Adds two integers together as per the + operator.
     * + operator 쓴다고 되어있음...
     * */
//    public int getSum(int a, int b) {
//        return Integer.sum(a, b);
//    }

}

