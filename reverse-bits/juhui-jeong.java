/*
 * 시간 복잡도: O(1)
 * 공간 복잡도: O(1)
 */
class Solution {

    public static String toBinaryString(int value) {
        String str = Integer.toBinaryString(value);
        while (str.length() < 32) {
            str = "0" + str;
        }
        return str;
    }

    public int reverseBits(int n) {
        String binaryString = toBinaryString(n);
        String reversed = new StringBuilder(binaryString).reverse().toString();
        
        int result = Integer.parseUnsignedInt(reversed, 2);
        return result;
    }
}
