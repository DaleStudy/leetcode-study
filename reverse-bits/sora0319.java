public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        String binary = String.format("%32s", Integer.toBinaryString(n)).replace(' ', '0');
        System.out.println(binary);
        
        StringBuilder sb  = new StringBuilder(binary);
        sb.reverse();
        
        
        return Integer.parseUnsignedInt(sb.toString(),2);
    }
}

