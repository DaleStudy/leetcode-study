import java.util.*;

//시간복잡도 : O(n), 공간복잡도 : O(n)
//이전 두 값만 필요하기에, 공간복잡도는 O(1)까지 최적화가 가능.

class Solution {
    public int climbStairs(int n) {
        if(n<=2){
            return n;
        }

        int[] dp =new int[n+1];
        dp[1]=1;
        dp[2]=2;

        for(int i=3;i<n+1;i++){
            dp[i]=dp[i-1]+dp[i-2];
        }

        return dp[n];

    }
}
