class Solution {
    public int reverseBits(int n) {
        int result = 0;
        for(int i = 0; i < 32; i++) {
            result <<= 1;   //왼쪽 이동
            result |= (n & 1); //마지막 비트 붙이기
            n >>= 1;    // 오른쪽 이동
        }
        return result;
    }
}
