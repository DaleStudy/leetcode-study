/**
 * TC : O(1)
 *   - carry가 매번 발생해도 int primitives의 비트 수가 32이므로 최대 32번 반복
 * SC : O(1)
 */
class Solution {
    public int getSum(int a, int b) {
        while(b != 0) {
            int carry = (a & b) << 1;
            a = a ^ b;
            b = carry;
        }
        return a;
    }
}
