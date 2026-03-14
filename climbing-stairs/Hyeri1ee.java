import java.util.*;

class Solution {
    public int climbStairs(int n) {
        int[] steps = new int[n+1];
        if (n == 1) return 1;
        if (n == 2) return 2;
        if (n == 3) return 3;
        steps[1] = 1; steps[2] = 2;//2, 1+1
        steps[3] = 3;
        for(int i = 4;i < n+1; i++){
            steps[i] = steps[i-1] + steps[i-2];
        }
        /*
        steps[4] = 
        1+1+1+1
        1+2+1
        2+2
        2+1+1
        1+1+2
        */

        return steps[n];
        

    }
}