class Solution {
    /*
     * 시간복잡도 O(n)
     * 공간복잡도 O(n)
    */
    public int climbStairs(int n) {
        int[] piv = new int[n+1];
        piv[0]=1;
        piv[1]=2;

        for(int i=2; i<n; i++) {
            piv[i]=piv[i-1]+piv[i-2];
        }
        return piv[n-1];
    }
}