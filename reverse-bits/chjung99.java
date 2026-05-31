class Solution {
    public int reverseBits(int n) {
        Integer[] rev = new Integer[32];
        for (int i = 0; i < 32; i++){
            rev[i] = 0;
        }
        int ret = 0;
        int ptr = 0;
        int fac = 1;
        while (n != 0){
            rev[ptr++] = n % 2;
            n = (int) (n/2);
        }
        for (int i = 0; i < 32; i++){
            ret += rev[31-i] * fac;
            fac *= 2;
        }
        return ret;
    }
}

