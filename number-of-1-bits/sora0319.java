class Solution {
    public int hammingWeight(int n) {
        int cnt = 0;
        String binary = Integer.toBinaryString(n);

        for(int i = 0; i < binary.length(); i++){
            if(binary.charAt(i) == '1') cnt++;
        }
        return cnt;
    }
}


