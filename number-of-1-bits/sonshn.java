/**
 * hammingWeight
 * 정수 n의 이진수 표현에서 1의 개수를 반환
 * 
 * 시간 복잡도: O(1)
 * 공간 복잡도: O(1)
 */
public class sonshn {
    public int hammingWeight(int n) {
        int count = 0;

        while (n != 0) {
            count += (n & 1);
            n >>>= 1;
        }

        return count;
    }
}