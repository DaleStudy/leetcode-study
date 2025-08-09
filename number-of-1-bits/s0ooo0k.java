class Solution {
    public int hammingWeight(int n) {
        /*
         * 시간복잡도 O(log n)
         */
        int cnt = 0;
        while(n!=0) {
            if(n%2==1) cnt++;
            n = n / 2; 
        }
        return cnt;
    }
}

