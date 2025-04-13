// 시간 복잡도 O(n) - n은 계단의 개수
// 공간 복잡도 O(1) - 상수 공간 사용
class Solution{
    public int climbStairs(int n){
        // 피보나치
        int prev1 = 1; // 0번째 계단
        int prev2 = 1; // 1번째 계단

        for(int i=2; i<=n; i++){
            int current = prev1 + prev2;
            prev1 = prev2;
            prev2 = current;
        }
        return prev2;
    }
}
