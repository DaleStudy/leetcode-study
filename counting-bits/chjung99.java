// time: O(n)
// space: O(n)

class Solution {
    public int[] countBits(int n) {
        int[] ans = new int[n+1];

        if (n >= 1){
            ans[0] = 0;
            ans[1] = 1;
        }
        int fac = 2;
        int prev = 1;

        for (int i = 2; i <= n; i++){
            if (i == fac){
                prev = fac;
                fac *= 2;

                ans[i] = 1;
                continue;
            }

            ans[i] = 1+ ans[i-prev];
        }

        return ans;
    }
}


