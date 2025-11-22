/**
    풀이 :
        dp를 이용하여 이전 카운팅 값을 계속 더해감.

    복잡도 계산 :
        계단의 수 -> N
        시간 복잡도 : O(N)
        공간 복잡도 : O(N)
*/
class Solution {
    public int climbStairs(int n) {
        if(n < 3) return n;
        
        int[] stairs = new int[n];

        stairs[0] = 1;
        stairs[1] = 2;

        for(int i = 2; i < n; i++) {
            stairs[i] = stairs[i-1] + stairs[i-2];
        }

        return stairs[n-1];
    }
}
