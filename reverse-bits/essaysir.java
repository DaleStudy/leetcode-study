class Solution {
    public int reverseBits(int n) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 32; i++) {
            sb.append((n >>> i) & 1);   // i번째 비트를 꺼내서 뒤에 붙임
        }
        return Integer.parseUnsignedInt(sb.toString(), 2);  // 2진 문자열 → int
    }
}
