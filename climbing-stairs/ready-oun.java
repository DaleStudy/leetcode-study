class Solution {
    public int climbStairs(int n) {
        if (n <= 2) return n; // base cases 

        int first = 1; // f(1)
        int second = 2; // f(2)

        // bottom-up dp: s to n 
        for (int i = 3; i <= n; i++) {
            int current = first + second; // f(i) = f(i-1) + f(i-2) 
            first = second; // 
            second = current; 
        }
        return second; 
    }
}

/**
    Fibonacci-like DP problem -> f(n) = f(n-1) + f(n-2)
    (n 번째 칸에 오르는 방법의 개수) = (n-1 번째 칸에 오르는 방법의 개수) + (n-2 번째 칸에 오르는 방법의 개수)
    - Time Complexity: O(n) 
        loop from 3 to n once 
    - Space Complexity: O(1)
        only 2 var are used 
 */
