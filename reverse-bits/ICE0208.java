class Solution2 {
    public int reverseBits(int n) {
        int result = 0;

        for (int i = 0; i < 32; i++) {
            int lastBit = n & 1; // 가장 오른쪽 비트 추출

            result <<= 1;        // 새 비트를 넣을 자리 확보
            result |= lastBit;   // 추출한 비트를 오른쪽 끝에 추가

            n >>>= 1;            // 처리한 비트를 버림.
        }

        return result;
    }
}

class Solution {
    public int reverseBits(int n) {
        String binary = String.format("%32s", Integer.toBinaryString(n))
                .replace(' ', '0');

        String reversed = new StringBuilder(binary)
                .reverse()
                .toString();

        return Integer.parseUnsignedInt(reversed, 2);
    }
}
