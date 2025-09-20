class Solution {
    public int reverseBits(int n) {
        int[] stack_n = new int[32];
        int i = 0;
        while(i < 32){
            stack_n[i] = n % 2;
            n /= 2;
            i++;
        }

        int result = 0;
        int scale = 1;

        for(int j=31;j>0;j--){
            result += stack_n[j] * scale;
            scale *= 2;
        }

        return result;
    }
}
