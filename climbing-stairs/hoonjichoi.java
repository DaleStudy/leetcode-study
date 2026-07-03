/*
f(45) = f(44) + f(43)
f(44) = f(43) + f(42)
.
.
.
f(3) = f(2) + f(1)
f(2) = 2
f(1) = 1
*/
class Solution {
    public int climbStairs(int n) {
        if (n <= 2) return n;

        int prev = 1;
        int result = 2;
        int temp = 0;
        for (int i = 2; i < n ; i++) {
            temp = result;
            result += prev;
            prev = temp;
        }     
        return result;
    }
}