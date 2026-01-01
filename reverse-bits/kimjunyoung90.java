class Solution {
    public int reverseBits(int n) {

        //1. 이진수 변환
        String binary = toReverseBinary(n);

        //2. 10진수 출력
        int result = toNumber(binary);
        return result;
    }

    private int toNumber(String binary) {
        int result = 0;
        for (int i = binary.length(); i > 0 ; i--) {
            char nChar = binary.charAt(i - 1);
            result += (nChar == '0' ? 0 : 1) * square(32 - i);
        }
        return result;
    }

    private int square(int i) {
        int result = 1;
        for (int j = 0; j < i; j++) {
            result *= 2;
        }
        return result;
    }

    private String toReverseBinary(int n) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 32; i++) {
            sb.append(n % 2);
            n /= 2;
        }
        return sb.toString();
    }
}
