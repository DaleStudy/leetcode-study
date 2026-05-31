/**
    비트 연산을 통해, 1의 개수를 구하는 방식
    숫자 n -> N
    시간 복잡도 : O(logN)
    공간 복잡도 : O(1)
 */
class Solution2 {
    public int hammingWeight(int n) {
        int count = 0;
        long bit = 1;
        while(bit <= n) {
            if((n & bit) > 0) {
                count++;
            }
            bit <<= 1;
        }
        return count;
    }
}

/**
    Integer.bitCount() 메소드를 통해, 1의 개수를 구하는 방식
    시간 복잡도 : O(1)
    공간 복잡도 : O(1)
 */
class Solution {
    public int hammingWeight(int n) {
        return Integer.bitCount(n);
    }
}
