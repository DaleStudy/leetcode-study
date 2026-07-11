/**
 * [풀이 개요]
 * - 시간복잡도 : O(1)
 * - 공간복잡도 : O(1)
 */
class Solution {
    public int hammingWeight(int n) {
        return Integer.bitCount(n);
    }
    
    /** 참고
    @IntrinsicCandidate
    public static int bitCount(int i) {
        // HD, Figure 5-2
        i = i - ((i >>> 1) & 0x55555555);
        i = (i & 0x33333333) + ((i >>> 2) & 0x33333333);
        i = (i + (i >>> 4)) & 0x0f0f0f0f;
        i = i + (i >>> 8);
        i = i + (i >>> 16);
        return i & 0x3f;
    }
    */

    /** 
     * [문제 풀이 아이디어]
     * - 10진수를 2진수로 표현했을 때 1의 갯 수를 세야함.
     * - 10진수를 2로 나눈 몫이 0이 될 때까지 나누고, 각각의 나머지를 역으로 적으면 2진수가 됨.
     * - 따라서 각 나눗셈의 나머지가 1인 경우를 카운트 할 수 있음
     * - 진법 변환 예시
     *   - 10 % 2 = 5, 0 - 2^0
     *   - 5  % 2 = 2, 1 - 2^1
     *   - 2  % 2 = 1, 0 - 2^2
     *   - 1  % 2 = 0, 1 - 2^3
     *   - 10 => 1010 
     * - int는 32비트 자료형으로 최대 32번 반복하므로 시간복잡도는 상수시간으로 봐도 무방, O(1)
     * - 별도 공간이 유의미한 공간할당을 하고 있지 않으므로 공간복잡도는 0(1)
     */
    public int hammingWeight(int n) {
        int count = 0;
        while(n > 0) {
            count += n % 2;
            n /= 2; 
        }
        return count;
    }
}
