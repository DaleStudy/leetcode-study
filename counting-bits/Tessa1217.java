class Solution {

    // 시간복잡도: O(n)
    public int[] countBits(int n) {
        int[] bitsArray = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            // Shift 연산자 사용
            // i&1 => 마지막 비트가 0인지 1인지 확인
            bitsArray[i] = bitsArray[i >> 1] + (i & 1);
        }
        return bitsArray;
    }
}

