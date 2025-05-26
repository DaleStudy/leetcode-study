public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        String intStr = String.valueOf(n);
        String binStr = String.format("%32s", Integer.toBinaryString(n)).replace(" ", "0");

        String reversedBinStr = "";
        for (int i = 31; i >= 0; i--) {
            reversedBinStr += binStr.charAt(i);
        }

        Integer reversedInt = Integer.parseUnsignedInt(reversedBinStr, 2);
        return reversedInt;
    }
}
