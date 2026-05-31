class Solution {
    public int reverseBits(int n) {
        String origin = Integer.toBinaryString(n);
        origin = String.format("%32s", origin).replace(' ', '0');
        String reversed = "";
        for (int i = origin.length() - 1; i >= 0; i--) {
            reversed += origin.charAt(i);
        }
        // System.out.println(origin);
        // System.out.println(reversed);
        int result = Integer.parseInt(reversed, 2);
        // System.out.println(result);
        return result;
    }
}
